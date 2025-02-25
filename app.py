from flask import Flask, redirect
from flask_cors import CORS
from src.main.rest.InfoEndpoint import info_endpoint
from src.main.rest.MessageEndpoint import message_endpoint 
from flasgger import Swagger

app = Flask(__name__)
CORS(app)

swagger_config = {
    "swagger": "2.0",
    "info": {
        "title": "AI Backend PoC",
        "description": "This is the backend for a proof of concept of a system using some tools of AI",
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
    "specs_route": "/apidocs/",
    "title" : "AI Backend",
    'hide_top_bar': True
}

swagger = Swagger(app, config=swagger_config)

app.register_blueprint(info_endpoint)
app.register_blueprint(message_endpoint) 

@app.route('/')
def index():
    return redirect('/apidocs')

if __name__ == '__main__':
    app.run()
