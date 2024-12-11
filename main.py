from operator import truediv
import csv

class ChainingHashTable:
    def __init__(self, initial_capacity=16):
        self.table = []
        #self.num = 5
        for i in range(initial_capacity):
            self.table.append([])

    def insert(self, key, item):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for n in bucket_list:
            if n[0] == key:
                n[1] = item
                return True

        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for n in bucket_list:
            if n[0] == key:
                return n[1]
        return None


    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for n in bucket_list:
            if n[0] == key:
                bucket_list.remove([n[0], n[1]])

class Package:
    def __init__(self, ID, addr, city, zipcode, deadline,  weight, status):
        self.ID = ID
        self.addr = addr
        self.city = city
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.ID, self.addr, self.city, self.zipcode,self.deadline, self.weight, self.status)

class Vertex:
    # Constructor for a new Vertx object. All vertex objects
    # start with a distance of positive infinity.
    def __init__(self, label):
        self.label = label
        self.distance = float('inf')
        self.pred_vertex = None

class Graph:
    def __init__(self):
        self.adjacency_list = {}  # vertex dictionary {key:value}
        self.edge_weights = {}  # edge dictionary {key:value}

    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []  # {vertex_1: [], vertex_2: [], ...}

    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        # {(vertex_1,vertex_2): 484, (vertex_1,vertex_3): 626, (vertex_2,vertex_6): 1306, ...}
        self.adjacency_list[from_vertex].append(to_vertex)
        # {vertex_1: [vertex_2, vertex_3], vertex_2: [vertex_6], ...}

    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)

def loadPackageCSV(filename):
    with open(filename) as PackageCSV:
        packageData = csv.reader(PackageCSV, delimiter=',')
        next(packageData)
        for package in packageData:
            pID = int(package[0])
            pAddr = package[1]
            pCity = package[2]
            pZipCode = package[3]
            pDeadLine = package[4]
            pWeight = package[5]
            pStatus = "The Hub"

            package = Package(pID, pAddr, pZipCode, pWeight, pDeadLine, pCity, pStatus)

            #print(package)

            myHash.insert(pID, package)

            #print(myHash.table)

def loadDistanceTableCSV(filename):
    with open(filename) as DistanceTableCSV:
        distanceTableData = csv.reader(DistanceTableCSV, delimiter=',')
        next(distanceTableData)
        for distance in distanceTableData:
            print(distance)
            '''pID = int(package[0])
            pAddr = package[1]
            pCity = package[2]
            pZipCode = package[3]
            pDeadLine = package[4]
            pWeight = package[5]
            pStatus = "The Hub"'''

            #package = Package(pID, pAddr, pZipCode, pWeight, pDeadLine, pCity, pStatus)

            #print(package)

            #myHash.insert(pID, package)

            #print(myHash.table)

def packageLookUp(ID):
    return myHash.search(ID)


def dijkstra_shortest_path(g, start_vertex):
    # Put all vertices in an unvisited queue.
    unvisited_queue = []

    for current_vertex in g.adjacency_list:
        unvisited_queue.append(current_vertex)
        # unvisited_queue = [vertex_1, vertex_2, ...]

    # Start_vertex has a distance of 0 from itself
    start_vertex.distance = 0

    # One vertex is removed with each iteration; repeat until the list is
    # empty.
    while len(unvisited_queue) > 0:

        # Visit vertex with minimum distance from start_vertex
        smallest_index = 0
        for i in range(1, len(unvisited_queue)):
            # print(unvisited_queue[i].label, unvisited_queue[i].distance, unvisited_queue[i].pred_vertex)
            if unvisited_queue[i].distance < unvisited_queue[smallest_index].distance:
                smallest_index = i
        current_vertex = unvisited_queue.pop(smallest_index)
        # print("From Start Vetex to current_vertex.label: " + current_vertex.label +" distance: " + str(current_vertex.distance))

        # Check potential path lengths from the current vertex to all neighbors.
        for adj_vertex in g.adjacency_list[current_vertex]:  # values from  dictionary
            # if current_vertex = vertex_1 => adj_vertex in [vertex_2, vertex_3], if vertex_2 => adj_vertex in [vertex_6], ...
            edge_weight = g.edge_weights[(current_vertex, adj_vertex)]  # values from dictionary
            # edge_weight = 484 then 626 then 1306, ...}
            alternative_path_distance = current_vertex.distance + edge_weight

            # If shorter path from start_vertex to adj_vertex is found, update adj_vertex's distance and predecessor
            if alternative_path_distance < adj_vertex.distance:
                adj_vertex.distance = alternative_path_distance
                adj_vertex.pred_vertex = current_vertex


def get_shortest_path(start_vertex, end_vertex):
    # Start from end_vertex and build the path backwards.
    path = ""
    current_vertex = end_vertex
    while current_vertex is not start_vertex:
        path = " -> " + str(current_vertex.label) + path
        current_vertex = current_vertex.pred_vertex
    path = start_vertex.label + path
    return path


def get_shortest_path_city(start_vertex, end_vertex):
    # Start from end_vertex and build the path backwards.
    path = ""
    current_vertex = end_vertex
    while current_vertex is not start_vertex:
        myMovie = myHash.search(int(current_vertex.label))
        path = " -> " + myMovie.city + path
        current_vertex = current_vertex.pred_vertex
    path = "Salt Lake City " + path
    return path

myHash = ChainingHashTable()

loadPackageCSV("PackageCSV.csv")

loadDistanceTableCSV("DistanceTableCSV.csv")

g = Graph()

'''weight_arr = [
    [7.2],
    [3.8, 7.1]
]

city_arr = ["Western Governors University 4001 South 700 East, Salt Lake City, UT 84107",
            " 1060 Dalton Ave S (84104)",
            "1330 2100 S (84106)"] '''

vertex_1 = Vertex("Western Governors University"
"4001 South 700 East," 
"Salt Lake City, UT 84107")
g.add_vertex(vertex_1)

vertex_2 = Vertex(" 1060 Dalton Ave S"
"(84104)")
g.add_vertex(vertex_2)

vertex_3 = Vertex("1330 2100 S"
"(84106)")
g.add_vertex(vertex_3)

g.add_undirected_edge(vertex_1, vertex_2, 7.2)
g.add_undirected_edge(vertex_1, vertex_3, 3.8)
g.add_undirected_edge(vertex_2, vertex_3, 7.1)

dijkstra_shortest_path(g, vertex_1)

'''print("\nDijkstra shortest path:")
for v in g.adjacency_list:
    if v.pred_vertex is None and v is not vertex_1:
        print("1 to %s ==> no path exists" % v.label)
    else:
        print("1 to %s ==> %s (total distance: %g)" % (v.label, get_shortest_path(vertex_1, v), v.distance))
'''
#print(vertex_1.label, vertex_2.label)

#print(g.edge_weights)

#print(packageLookUp(3))

#for i in range(len(myHash.table)+1):
 #  print("Key: {} and Package: {}".format(i + 1, myHash.search(i + 1)))

#myHash.insert(1)
#myHash.insert(1)

#1d to access the bucket, 2d to access a key value pair in the bucket, and 3d to access the specific itm in the key value
# pair, in the below case, the object itself

#kv = myHash.table[1][1][1]
#print(kv)