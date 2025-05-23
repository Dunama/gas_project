from flask import Blueprint, render_template, url_for, session
import os
import json 
from datetime import datetime

records_bp = Blueprint('records', __name__)
SALES_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__),'../../../sales_records.json'))

def get_all_sales():
    '''get all sales records'''
    try:
        with open(SALES_FILE, 'r')as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def generate_sale_id():
    '''generates a sales id for every sales'''
    sales = get_all_sales()
    if not sales:
        return 'SALE-1'
    last_id = max([int(sale['id'].split('-')[1]) for sale in sales])
    return f'SALE-{last_id + 1}'

def record_sales(customer_id, kg_bought, price_per_kg, total_amount):
    sale = {
        'id': generate_sale_id(),
        'customer_id': customer_id,
        'price_per_kg': price_per_kg,
        'kg_bought': kg_bought,
        'total_amount': total_amount,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    # load existing sales
    sales = get_all_sales()
    
    # add new sales
    sales.append(sale)

    # save to file
    with open(SALES_FILE, 'w')as f:
        json.dump(sales, f, indent=2)
    return sale

# route for the records
@records_bp.route('/admin/records')
def records():
    '''view sales history'''
    sales = get_all_sales()
    return render_template('records.html', sales=sales)
    