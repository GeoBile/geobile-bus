import db
import json
import heapq


#Connect to the postgres database
db.connect()

def build_routes_map():
	routes = db.get_routes()
	routes_map = {}
	
	for route in routes:
		key = (route["service_no"],route["direction"])
		if key not in routes_map:
			routes_map[key] = []
		routes_map[key]+=[route]
	return routes_map
	
def build_graph():
	routes_map = build_routes_map()
	graph = {}
	for service, path in routes_map.items():
		for route_index in range(len(path)-1):
			key = path[route_index]["bus_stop_code"]
			if key not in graph:
				graph[key]=  {}
			curr_route_stop = path[route_index]
			next_route_stop = path[route_index + 1]
			curr_distance = curr_route_stop["distance"]
			next_distance = next_route_stop["distance"]
			if curr_distance == None:
				curr_distance = 0
				
			if next_distance == None:
				next_distance = 0
				
			distance = next_distance - curr_distance
			if distance >= 0:
				graph[curr_route_stop["bus_stop_code"]][next_route_stop["bus_stop_code"]] = distance
	return graph
	
def execute(start,end):
	graph = build_graph()
	seen = set()
	
	# maintain a queue of paths
	queue = []
    # push the first path into the queue
	heapq.heappush(queue, (0, [start]))
	while queue:
		# get the first path from the queue
		(curr_distance, path) = heapq.heappop(queue)
		# get the last node from the path
		node = path[-1]
		# path found
		if node == end:
			return path
		if node in seen:
			continue
		seen.add(node)
        # enumerate all adjacent nodes, construct a new path and push it into the queue
		for adjacent, distance in graph.get(node, {}).items():
			new_path = list(path)
			new_path.append(adjacent)
			heapq.heappush(queue, (curr_distance, new_path))
			
def get_path_details(path):
	code_list = '('
	count = 0
	for code in path:
		code_list += "'" + code + "'"
		if count < len(path) - 1:
			code_list += ","
		else:
			code_list += ")"
			return code_list
		count += 1
			
	return ''
	