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
		cur.execute("SELECT bus_stop_code,description,latitude, longitude, road_name from STOPS where latitude != 0 LIMIT 100")
	else:
		cur.execute("SELECT bus_stop_code,description,latitude, longitude, road_name from STOPS where bus_stop_code = '" + code + "'")

	rows = cur.fetchall()
	data = []

	for row in rows:
		data.append({'code':row[0],'description':row[1],'latitude':row[2],'longitude':row[3]})

	return data

def get_bus_stops_by_name(name=None):
	data = []
	if name != None:
		cur.execute("SELECT bus_stop_code,description,latitude, longitude, road_name from STOPS where description LIKE '" + name + "%'")

		rows = cur.fetchall()
		
		for row in rows:
			data.append({'code':row[0],'description':row[1],'latitude':row[2],'longitude':row[3]})

	return data
	
def get_bus_stops_details(path=None):
	data = []
	if path != None:
		cur.execute("SELECT bus_stop_code,description,latitude, longitude, road_name from STOPS where bus_stop_code IN " + path )

		rows = cur.fetchall()
		
		for row in rows:
			data.append({'code':row[0],'description':row[1],'latitude':row[2],'longitude':row[3]})

	return data
		
def get_routes():
	cur.execute("SELECT service_no, direction, distance,stop_sequence, sun_last_bus, wd_last_bus, sat_last_bus, bus_stop_code, operator, sat_first_bus, sun_first_bus, wd_first_bus from ROUTES")
	
	rows = cur.fetchall()
	data = []

	for row in rows:
		data.append({'service_no':row[0],'direction':row[1],'distance':row[2],'stop_sequence':row[3],'sun_last_bus':row[4],'wd_last_bus':row[5],'sat_last_bus':row[6],'bus_stop_code':row[7],'operator':row[8],'sat_first_bus':row[9],'sun_first_bus':row[10],'wd_last_bus':row[5],'wd_first_bus':row[11]})
		
	return data

