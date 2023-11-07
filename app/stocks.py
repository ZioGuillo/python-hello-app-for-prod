import os
from flask import Flask, request, jsonify, Blueprint
import requests

app = Flask(__name__)
stocks_app = Blueprint('stocks_app', __name__)

# Replace 'YOUR_API_KEY' with your Alpha Vantage API key

ALPHA_VANTAGE_API_KEY = os.environ.get('ALPHA_VANTAGE_API_KEY')
if ALPHA_VANTAGE_API_KEY is None:
    raise Exception("API key not found in environment variables.")

ALPHA_VANTAGE_BASE_URL = 'https://www.alphavantage.co/query'

# example: http://127.0.0.1:5000/stocks/get_stock_price?symbol=AAPL

@stocks_app.route('/get_stock_price', methods=['GET'])
def get_stock_price():
    stock_symbol = request.args.get('symbol')

    if not stock_symbol:
        return jsonify({"error": "Stock symbol is required."}), 400

    # Make a request to Alpha Vantage to get the stock price
    endpoint = f"{ALPHA_VANTAGE_BASE_URL}"
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': stock_symbol,
        'interval': '1min',
        'apikey': ALPHA_VANTAGE_API_KEY
    }

    response = requests.get(endpoint, params=params)
    data = response.json()

    if "Time Series (1min)" in data:
        # Extract the latest stock price from the response
        latest_data = data["Time Series (1min)"]
        latest_timestamp = list(latest_data.keys())[0]
        latest_price = latest_data[latest_timestamp]['1. open']

        return jsonify({"symbol": stock_symbol, "price": latest_price})
    else:
        return jsonify({"error": "Unable to fetch stock price."}), 500
    
# example : http://127.0.0.1:5000/stocks/get_stock_data/TIME_SERIES_INTRADAY?symbol=NKE&interval=1min

@stocks_app.route('/get_stock_data/<endpoint>', methods=['GET'])
def get_stock_data(endpoint):
    # Remove the 'endpoint' parameter, as it's now part of the URL
    request_args = request.args.copy()

    # Construct the full Alpha Vantage API endpoint
    full_endpoint = f"{ALPHA_VANTAGE_BASE_URL}?function={endpoint}"

    # Add your API key to the request
    request_args['apikey'] = ALPHA_VANTAGE_API_KEY

    # Make a request to Alpha Vantage using the constructed endpoint and query parameters
    response = requests.get(full_endpoint, params=request_args)
    data = response.json()

    return jsonify(data)

if __name__ == '__main__':
    app.run()