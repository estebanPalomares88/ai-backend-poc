from flask import Flask, redirect
from flask_cors import CORS
from src.main.rest.InfoEndpoint import info_endpoint
from flasgger import Swagger

app = Flask(__name__)
CORS(app)
swagger = Swagger(app)

app.register_blueprint(info_endpoint)

@app.route('/')
def index():
    return redirect('/apidocs')

if __name__ == '__main__':
    app.run()
