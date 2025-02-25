from flask import Blueprint
from flasgger import swag_from

message_endpoint = Blueprint('message_endpoint', __name__)  

@message_endpoint.route('/message', methods=['POST', 'PUT', 'PATCH', 'DELETE'])  
@swag_from({
    'tags': ['Message']
})
def message():
    try:
        return {"message": "Hello World!"}, 200
    except Exception as e:
        return {"error": str(e)}, 500