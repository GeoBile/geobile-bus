import psycopg2

conn = None
cur = None

def connect():
	print 'Connect db...'
	global conn
	conn = psycopg2.connect(database = "geobile_db", user = "postgres", password = "root", host = "127.0.0.1", port = "5432")
	print "Opened database successfully"
	global cur
	cur = conn.cursor()
	
def get_bus_stops(code=None):
	if code == None:
		cur.execute("SELECT bus_stop_code,description,latitude, longitude, road_name from STOPS where latitude != 0")
	else:
		cur.execute("SELECT bus_stop_code,description,latitude, longitude, road_name from STOPS where bus_stop_code = '" + code + "'")

	rows = cur.fetchall()
	data = []

	for row in rows:
		data.append({'code':row[0],'description':row[1],'latitude':row[2],'longitude':row[3]})

	return data
