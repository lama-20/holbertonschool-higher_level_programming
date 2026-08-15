from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json():
    with open('products.json', 'r') as file:
        return json.load(file)


def read_csv():
    with open('products.csv', 'r') as file:
        return list(csv.DictReader(file))


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template(
            'product_display.html',
            products=[],
            error='Wrong source'
        )

    if source == 'json':
        data = read_json()
    else:
        data = read_csv()

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
