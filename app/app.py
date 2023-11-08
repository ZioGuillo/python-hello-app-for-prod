import random, requests
from flask import Flask, request, jsonify
from stocks import stocks_app

app = Flask(__name__)

@app.route('/')
def hello_world():
    data = b'Hello, World!'
    status = '200 OK'
    response_headers = [
      ('Content-type', 'text/plain'),
      ('Content-Length', str(len(data)))
    ]
    return data, status, response_headers

@app.get('/health')
def health():
    return {"status" : "UP"}
  
@app.route('/random')
def get_random_numbers():
    numbers = [random.randint(1, 99) for _ in range(6)]
    response = {
        "data": {"random_number": numbers},
        "message": "success"
    }
    return jsonify(response)

@app.route('/randomball')
def get_random_numbersball():
    numbers_1to69 = [random.randint(1, 69) for _ in range(5)]
    number_1to26 = random.randint(1, 26)
    response = {
        "data": {
            "Lottery": numbers_1to69,
            "Mega": number_1to26
        },
        "message": "success"
    }
    
    return jsonify(response)

# Stocks Functions

# Register the blueprint from the stocks module
app.register_blueprint(stocks_app, url_prefix='/stocks')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)