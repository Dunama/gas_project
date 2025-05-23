from flask import request, render_template, Blueprint
from .records import record_sales
# Create a Blueprint for gas conversion routes
users_sales_bp = Blueprint('users_sales', __name__)

# Path to the price file - should match the path in pricing.py
price_file = 'gas_price.txt'
def _get_current_price():
    '''
    Read the current gas price from the file
    Returns: float - the current price per kg of gas
    '''
    try:
        with open(price_file, "r") as f:
            price_str = f.read().strip()
            return float(price_str)
    except (FileNotFoundError, ValueError):
        # Return a default price if file doesn't exist or contains invalid data
        return float(0.0)

@users_sales_bp.route('/users/sales', methods=['GET', 'POST'])
def users_sales():
    '''
    converts gas value to amount or kg based on users input
    '''
    amount = None
    kg = None
    price_per_kg = _get_current_price()
    if request.method == 'POST':
        calc_type = request.form.get('calculation-type')
        if calc_type == 'amount':
            try:
                amount = float(request.form.get('amount', 0))
                kg = round(amount / price_per_kg, 2)
                customer_id = request.form.get('customer_id','user')
                record_sales(customer_id,total_amount=amount, price_per_kg=price_per_kg, kg_bought=kg)
            except ValueError:
                amount = None
        elif calc_type == 'kilogram':
            try:
                kg = float(request.form.get('kilogram', 0))
                amount = round(kg * price_per_kg, 2)
                customer_id = request.form.get('customer_id','user')
                record_sales(customer_id, total_amount=amount, price_per_kg=price_per_kg, kg_bought=kg)
            except ValueError:
                kg = None
    return render_template('users_sales.html', kg=kg, amount=amount, current_price=price_per_kg)