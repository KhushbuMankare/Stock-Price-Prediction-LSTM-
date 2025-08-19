from flask import Flask, render_template, request
from model import predict_stock_price

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    plot_url = None
    if request.method == 'POST':
        ticker = request.form['ticker'].upper()
        try:
            prediction, plot_url = predict_stock_price(ticker)
        except Exception as e:
            prediction = f"Error: {e}"

    return render_template('index.html', prediction=prediction, plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)
