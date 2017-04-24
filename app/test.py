import db
import dijkstra as dij
import json
from pprint import pprint


#Connect to the postgres database
db.connect()

if __name__ == '__main__':
	pprint(dij.execute('9022','99009'))
	