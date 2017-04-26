import db
import dijkstra as dij
import json
from pprint import pprint


#Connect to the postgres database
db.connect()

if __name__ == '__main__':
	pprint(dij.execute('99041','99009'))
	pprint(db.get_bus_stops_details(dij.get_path_details(dij.execute('99041','99009'))))
	