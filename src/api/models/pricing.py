from flask import Flask,  Blueprint, render_template, request, redirect, url_for
from .admin_sales import _get_current_price, price_file
pricing_bp = Blueprint('pricing',__name__)




def save_new_price(price):
    '''save gas price to file'''
    with open(price_file, "w") as f:
        f.write(price)

# routes for the gas price
@pricing_bp.route('/admin/pricing', methods=['GET', 'POST'])
def pricing():
    error = None
    if request.method == 'POST':
        new_price = request.form['new_price']
        try:
                # we convert the price(number) into a float
                price = float(new_price)
                save_new_price(str(price))
                return redirect(url_for('pricing.pricing'))
        except ValueError:
            error = 'Please enter a valid number'
    price = _get_current_price()
    return render_template('pricing.html', current_price=price, error=error)
