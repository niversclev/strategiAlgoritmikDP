from flask import Flask, render_template, request
from Algoritma import Barang, knapsack

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/knapsack')
def knapsack():
    hasil = None
    items = []

    if request.method == 'POST':
        kapasitas = int(request.form['kapasitas'])

        # Ambil semua barang yang dikirim dari form
        index = 0
        while True:
            nama = request.form.get(f'nama_{index}')
            berat = request.form.get(f'berat_{index}')
            profit = request.form.get(f'profit_{index}')
            if not nama:
                break
            items.append(Barang(nama, berat, profit))
            index += 1

        hasil = knapsack(items, kapasitas)
    return render_template('knapsack.html',hasil=hasil, items=items)

if __name__ == '__main__':
    app.run(debug=True)
