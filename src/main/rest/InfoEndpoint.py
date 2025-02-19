import datetime
from flask import Blueprint, jsonify, request
import geocoder
import pytz
from timezonefinder import TimezoneFinder
import secrets


info_endpoint = Blueprint('info_endpoint', __name__)


@info_endpoint.route('/info', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def info():
    try:
        location = geocoder.ip('me').city
        latlng = geocoder.ip('me').latlng
        timezone_str = TimezoneFinder().timezone_at(lng=latlng[1], lat=latlng[0])
        timezone = pytz.timezone(timezone_str)
        print(timezone)
        date = datetime.datetime.now(pytz.utc).astimezone(timezone)
        tz = date.tzname()
        print(tz)
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

        if not request.data:
            return response, 200
        data = request.json
        response["data"] = data
        return response, 200
    except Exception as e:
        return {"error" : str(e)}, 500
