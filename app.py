from flask import Flask, render_template, request, url_for, redirect
from Algoritma import Barang, knapsack 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index')
def index_redirect():
    return redirect(url_for('index'))

@app.route('/knapsack', methods=['GET', 'POST'])
def knapsack_page():
    hasil = None
    items = []

    if request.method == 'POST':
        try:
            kapasitas = int(request.form['kapasitas'])
            
            index = 0
            while True:
                nama = request.form.get(f'nama_{index}')
                berat = request.form.get(f'berat_{index}')
                profit = request.form.get(f'profit_{index}')
                
                if not nama or not berat or not profit:
                    break
                    
                items.append(Barang(nama, int(berat), int(profit)))
                index += 1

            if items:
                hasil = knapsack(items, kapasitas)
        except Exception as e:
            print(f"Error: {str(e)}")
            return render_template('knapsack.html', error=str(e))

    return render_template('knapsack.html', hasil=hasil, items=items)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')