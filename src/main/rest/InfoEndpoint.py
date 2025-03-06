import datetime
from flask import Blueprint, jsonify, request
import geocoder
import pytz
from timezonefinder import TimezoneFinder
import secrets
from flasgger import swag_from


info_endpoint = Blueprint('info_endpoint', __name__)


@info_endpoint.route('/info', methods=['GET'])
@swag_from({
    'tags': ['Info'],
    'responses': {
        200: {
            'description': 'Successful response',
            'examples': {
                'application/json': {
                    "method": "GET",
                    "date": "2025-02-20T12:34:56.789Z",
                    "server time zone": "UTC",
                    "server location": "New York",
                    "request ip": "192.168.1.1",
                    "token genrated": "abcdef1234567890"
                }
            }
        },
        500: {
            'description': 'Internal server error',
            'examples': {
                'application/json': {
                    "error": "Error message"
                }
            }
        }
    }
})
def info():
    try:
        location = geocoder.ip('me').city
        latlng = geocoder.ip('me').latlng
        timezone_str = TimezoneFinder().timezone_at(lng=latlng[1], lat=latlng[0])
        timezone = pytz.timezone(timezone_str)
        date = datetime.datetime.now(pytz.utc).astimezone(timezone)
        tz = date.tzname()
        request_ip = request.remote_addr
        token = secrets.token_hex(16)

        response = {
            "method" : request.method,
            "date" : date.isoformat(),
            "server time zone" : tz,
            "server location" : location,
            "request ip" : request_ip,
            "token genrated" : token
        }
        return response, 200
    except Exception as e:
        return {"error" : str(e)}, 500
