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

if __name__ == '__main__':
    app.run()