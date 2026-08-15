from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json():
    with open('products.json', 'r') as file:
        return json.load(file)


def read_csv():
    with open('products.csv', 'r') as file:
        return list(csv.DictReader(file))


def read_sql():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')

    products = [dict(row) for row in cursor.fetchall()]

    conn.close()

    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv', 'sql']:
        return render_template(
            'product_display.html',
            products=[],
            error='Wrong source'
        )

    try:
        if source == 'json':
            data = read_json()
        elif source == 'csv':
            data = read_csv()
        else:
            data = read_sql()

    except (sqlite3.Error, OSError, json.JSONDecodeError) as error:
        return render_template(
            'product_display.html',
            products=[],
            error=f'Database error: {error}'
        )

    if product_id is not None:
        found_product = None

        for product in data:
            if str(product['id']) == str(product_id):
                found_product = product
                break

        if found_product is None:
            return render_template(
                'product_display.html',
                products=[],
                error='Product not found'
            )

        data = [found_product]

    return render_template(
        'product_display.html',
        products=data,
        error=None
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
