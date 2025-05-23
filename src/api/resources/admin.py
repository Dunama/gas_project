from flask_restful import Resource, Api, reqparse
from flask import Blueprint
from src.db.models.admin import Admin
from src.db.core import db
from werkzeug.security import generate_password_hash
from datetime import datetime

admin_bp = Blueprint("admin",__name__)
api = Api(admin_bp)

AdminParser = reqparse.RequestParser()
AdminParser.add_argument('card_number', type=str, required=True, help='card number is required')  
AdminParser.add_argument('password', type=str, required=True, help='password is required') 

UpdateAdminParser = reqparse.RequestParser()
UpdateAdminParser.add_argument('card_number', type=str, required=True, help='card number is missing')
UpdateAdminParser.add_argument('password', type=str, required=True, help='password is missing')
# for single admin 
class AdminResource(Resource):
    #  to get all admin
    def get(self):
        '''get all admin'''
        admins =  Admin.query.all()
        if not admins:
            return {'message':'No admin found'},404
        
        admin_list = []
        for admin in admins:
            admin_list.append({
                'id':admin.id,
                'card_number': admin.card_number,
                'created_at': admin.created_at.strftime("%Y-%m-%d %H:%M:%S")
                })
        return {'admin':admin_list},200
    
    #  to post admin
    def post(self):
        '''create admin'''
        args = AdminParser.parse_args()
        hashed_password = generate_password_hash(args['password'])
        if Admin.query.filter_by(card_number=args['card_number']).first():
            return {"message": "Admin already exists"}, 400
        new_admin = Admin(
            card_number=args['card_number'],
            password=hashed_password,
            created_at=datetime.utcnow()
        )
        db.session.add(new_admin)
        db.session.commit()
        return {
            'message': 'user created successfully',
            'admin': {
                'id': new_admin.id,
                'card_number': new_admin.card_number,
                'created_at': new_admin.created_at.strftime("%Y-%m-%d %H:%M:%S")
            }
        }, 201
   
# # for single admin
class AdminList(Resource):
    def get(self, admin_id):
        '''get a single admin'''
        admin = Admin.query.get(admin_id)
        if not admin:
            return {'message':'Admin not found'},404
        admin_data ={
            'id':admin.id,
            'card_number':admin.card_number,
            'created_at':admin.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }
        return{'admin':admin_data},200
    
    def put(self, admin_id):
        '''update a single admin'''
        args = UpdateAdminParser.parse_args()
        admin = Admin.query.get(admin_id)
        if not admin:
            return {'message': 'Admin not found'},404
        if args.get('card_number') is None:
            admin.card_number = args['card_number']
        if args.get('password') is not None:
            admin.password = generate_password_hash(args['password'])

        db.session.commit()
        admin_update ={
            'id': admin.id,
            'card_number':admin.card_number
        }
        return {"admin":admin_update},200
    
    def delete(self, admin_id):
        '''delete an admin'''
        admin = Admin.query.get(admin_id)
        if not admin:
            return {'message':'Admin not found in database'}
        
        delete_admin ={
            'id': admin.id,
            'card_number': admin.card_number
        }
        db.session.delete(admin)
        db.session.commit()
        return {'message': 'Admin has been deleted successfully', 'Deleted':delete_admin},200
# register routes
api.add_resource(AdminList, '/admin/<int:admin_id>')
api.add_resource(AdminResource, '/admin')