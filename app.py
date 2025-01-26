from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    hello = '<html><body>Hello, World!</body></html>'
    return hello

@app.route('/healthcheck')
def health():
    health = 'healthy'
    return health

if __name__ == "__main__":
    app.run(debug=True)