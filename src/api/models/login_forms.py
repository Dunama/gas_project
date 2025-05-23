from flask import Blueprint, render_template, request, redirect, url_for, session
login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login_form():
    ''''route for logins'''
    error = None

    if request.method == 'POST':
        card_number = request.form.get('card_number')
        password = request.form.get('password')

        if card_number == '001' and password == '001':
            session['customer_id'] = card_number
            return redirect(url_for('login.dashboard'))
            
        
        elif card_number == '002' and password == '002':
            session['customer_id'] = card_number
            return redirect(url_for('users_sales.users_sales'))
        
   
        error = 'Invalid Username or Password'
    return render_template('users_login.html', error=error)

@login_bp.route('/dashboard', methods=['GET'])
def dashboard():
    '''route for dashboard'''
    return render_template('dashboard.html')