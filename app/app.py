from flask import Flask
from flask import jsonify
import db
import dijkstra
import json
from functools import wraps
from flask import redirect, request, current_app
import dijkstra as dij

#Connect to the postgres database
db.connect()

#run te web server
app = Flask(__name__)

api= "/api/v1"

def support_jsonp(f):
    """Wraps JSONified output for JSONP"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            content = str(callback) + '(' + str(f().data) + ')'
            return current_app.response_class(content, mimetype='application/json')
        else:
            return f(*args, **kwargs)
    return decorated_function

@app.route(api + '/stops',methods=['GET'])	
@support_jsonp
def get_stops():
	name = request.args.get('name')
	if name != None:
		return jsonify(db.get_bus_stops_by_name(name))
	else:
		return jsonify(db.get_bus_stops())

@app.route(api + '/stops/code/<code>',methods=['GET'])
@support_jsonp
def get_stops_by_code(code):
	return jsonify(db.get_bus_stops(code))


@app.route(api + '/routes',methods=['GET'])	
@support_jsonp
def get_routes():
	return jsonify(db.get_routes())
	
@app.route(api + '/path/shortest',methods=['GET'])	
@support_jsonp
def get_shortest_path():
	source = request.args.get('from')
	target = request.args.get('to')
	return jsonify(db.get_bus_stops_details(dij.get_path_details(dij.execute(source,target))))
	
if __name__ == '__main__':
    app.run()