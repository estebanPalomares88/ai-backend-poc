from flask import Flask, redirect
from flask_cors import CORS
from src.main.rest.InfoEndpoint import info_endpoint
from flasgger import Swagger

app = Flask(__name__)
CORS(app)

swagger_config = {
    "swagger": "2.0",
    "info": {
        "title": "AI Backend PoC",
        "description": "API documentation",
        "version": "1.0.0"
    },
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,  
            "model_filter": lambda tag: True,  
        }
    ],
    "headers": [], 
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}

swagger = Swagger(app, config=swagger_config)

app.register_blueprint(info_endpoint)

@app.route('/')
def index():
    return redirect('/apidocs')

if __name__ == '__main__':
    app.run()
