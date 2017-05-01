import db
import dijkstra as dij
import json
from pprint import pprint
from DynamicRoutes import DynamicRoutes

#Connect to the postgres database
dr = DynamicRoutes()

if __name__ == '__main__':
	pprint(dij.execute('99041','99009'))
	pprint(dr.get_bus_stops_details(dij.get_path_details(dij.execute('99041','99009'))))
	