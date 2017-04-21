from flask import Flask
from flask import jsonify
import db
import json

#Connect to the postgres database
db.connect()

#run te web server
app = Flask(__name__)

api= "/api/v1"

@app.route(api + '/stops')	
def get_stops():
	return jsonify(db.get_bus_stops())

@app.route(api + '/stops/<code>')	
def get_stops_by_code(code):
	return jsonify(db.get_bus_stops(code))
	
if __name__ == '__main__':
    app.run()