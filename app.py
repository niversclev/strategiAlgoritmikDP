from flask import Flask, render_template, request
from Algoritma import Barang, knapsack 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/knapsack', methods=['GET', 'POST'])
def knapsack_page():
    hasil = None
    items = []

    if request.method == 'POST':
        kapasitas = int(request.form['kapasitas'])

        index = 0
        while True:
            nama = request.form.get(f'nama_{index}')
            berat = request.form.get(f'berat_{index}')
            profit = request.form.get(f'profit_{index}')
            if not nama:
                break
            items.append(Barang(nama, berat, profit))
            index += 1

        hasil = knapsack(items, kapasitas)  # sekarang ini aman

    return render_template('knapsack.html', hasil=hasil, items=items)
