import random
from flask import Flask

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
  
@app.route('/random')
def get_random_numbers():
    numbers = [random.randint(1, 99) for _ in range(6)]
    response = {
        "data": {"random_number": numbers},
        "message": "success"
    }
    return response

if __name__ == '__main__':
    app.run()