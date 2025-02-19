from flask import Flask
from flask_cors import CORS
from src.main.rest.InfoEndpoint import info_endpoint

app = Flask(__name__)
CORS(app)

app.register_blueprint(info_endpoint)

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
