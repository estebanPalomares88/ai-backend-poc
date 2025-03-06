from flask import Blueprint, jsonify,request
from flasgger import swag_from

message_endpoint = Blueprint('message_endpoint', __name__)  

@message_endpoint.route('/message', methods=['POST', 'PUT', 'PATCH', 'DELETE'])  
@swag_from({
    'tags': ['Message'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'example': 'Hello, World!'
                    }
                },
                'required': ['message']
            }
        }
    ],
    'responses': {
        '200': {
            'description': 'Successful response',
            'schema': {
                'type': 'object',
                'properties': {
                    'data': {
                        'type': 'string',
                        'example': 'Hello, World!'
                    },
                    'method': {
                        'type': 'string',
                        'example': 'POST'
                    }
                }
            }
        },
        '400': {
            'description': 'Bad request',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {
                        'type': 'string',
                        'example': 'Request body is mandatory'
                    }
                }
            }
        },
        '500': {
            'description': 'Internal server error',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {
                        'type': 'string',
                        'example': 'Internal server error'
                    }
                }
            }
        }
    }
})
def message():
    try:
        data = request.get_json()
        if data is None:
            return {"error": "Request body is mandatory"}, 400
        message = data.get('message')
        if message is None:
            return {"error": "Message field is mandatory"}, 400
        response = {"data": message,
                    "method": request.method}
        return response, 200
    except Exception as e:
        return {"error": str(e)}, 500