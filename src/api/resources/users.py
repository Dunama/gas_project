from flask import request
from flask_restful import Resource, Api, reqparse
from flask import Blueprint
from src.db.models.users import Users
from src.db.core import db
from werkzeug.security import generate_password_hash


users_bp = Blueprint("users",__name__)
api = Api(users_bp)
# for posting user
Userparser = reqparse.RequestParser()
Userparser.add_argument('card_number', type=str, required=True, help='card number is missing')
Userparser.add_argument('password', type=str, required=True, help ='password is required')


class UsersResource(Resource):
    def get(self):
        '''get all users'''
        users =  Users.query.all()
        if not users:
            return {'message':'No user found'},404
        
        user_list = []
        for user in users:
            user_list.append({
                'id': user.id,
                'card_number': user.card_number
            })
        return {'users': user_list},200
    
    def post(self):
        '''create users'''
        args = Userparser.parse_args()
        hashed_password = generate_password_hash(args['password'])
        new_user = Users(
            card_number=args['card_number'],
            password=hashed_password
        )
        if Users.query.filter_by(password=new_user.password).first():
            return {'message':'User already exists'},400
        db.session.add(new_user)
        db.session.commit()
        return {
            'message':'User created successfully',
            'user':{
                'id': new_user.id,
                'card_number': new_user.card_number
            }
        },201
        
class UsersList(Resource):
    def get(self, user_id):
        '''get a single user'''
        user = Users.query.get(user_id)
        if not user:
            return{'message':'User not found'},404
        user_data ={
            'id':user.id,
            'card_number':user.card_number
        }
        return {"message":user_data}
    
    def put(self, user_id):
        '''Update an existing user'''
        args = Userparser.parse_args()
        user =  Users.get(user_id)
        if not user:
           return {'message':'User not found'},404
       
        if args['card_number'] is None:
           user.card_number = 'card_number'
        if args['password'] is None:
           user.password = generate_password_hash(user.password)

        db.session.commit()

    def delete(self, user_id):
        user = Users.query.get(user_id)
        if not user:
            return {'message':'User not found'}
        db.session.delete(user)
        db.session.commit()
        return {'message':'user deleted successfully',
                'user':{
                    'id':user.id,
                    'card_number':user.card_number
                }}

# register routes
api.add_resource(UsersList, '/users/<int:user_id>')
api.add_resource(UsersResource, '/users')