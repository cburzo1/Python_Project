import csv
from datetime import timedelta

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

    def __str__(self):
        return f'{self.label} {self.distance} pred: {self.pred_vertex}'

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

class truck:
    def __init__(self, num, packageList, location, startingLocation, time, startingTime, mileage):
        self.num = num
        self.packageList = packageList
        self.location = location
        self.startingLocation = startingLocation
        self.time = time
        self.startingTime = startingTime
        self.mileage = mileage

def loadPackageCSV(filename):
    with open(filename) as PackageCSV:
        packageData = csv.reader(PackageCSV, delimiter=',')
        next(packageData)
        for package in packageData:
            pID = int(package[0])
            pAddr = package[1]
            pCity = package[2]
            pZipCode = package[4]
            pDeadLine = package[5]
            pWeight = package[6]
            pStatus = ["At Hub", "08:00:00"]

            package = Package(pID, pAddr, pCity,  pZipCode, pDeadLine, pWeight,  pStatus)

            myHash.insert(pID, package)

city_arr2 = []
weight_arr2 = []

def loadDistanceTableCSV(filename):
    with open(filename) as DistanceTableCSV:
        distanceTableData = csv.reader(DistanceTableCSV, delimiter=',')
        next(distanceTableData)
        for distance in distanceTableData:
            #print(distance[1])
            city_arr2.append(distance[1])
            weight_arr2.append(distance[2:len(distance)])

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
    #print(start_vertex.label, end_vertex.label)
    ctr = 0

    current_vertex = end_vertex
    '''and current_vertex is not None'''
    while current_vertex is not start_vertex:
        #print('\t',ctr, '\t', current_vertex)
        path = " -> " + str(current_vertex.label) + path
        current_vertex = current_vertex.pred_vertex
        ctr += 1
    path = start_vertex.label + path
    #print('\t', path)
    return path

myHash = ChainingHashTable()

loadPackageCSV("PackageCSV.csv")

myHash.search(25).addr = "5383 S 900 East #104"
myHash.search(26).addr = "5383 S 900 East #104"

#print(myHash.search(25).addr)
#print(myHash.search(26).addr)

loadDistanceTableCSV("DistanceTableCSV.csv")

def getDistanceBetween2Cities(start, end):
    if(start <= end):
        return weight_arr2[end][start]
    else:
        return 'ERROR::make sure start is less than or equal to end'

def getMinimumDistanceBetween2Cities(start, end):
    #print("Start", start)
    #print("End", end)

    g = Graph()
    vertex_arr = []

    # adding all vertices to graph
    for i in range(0, len(city_arr2)):
        vertex_arr.append(Vertex(city_arr2[i].replace('\n', ' ')))
        g.add_vertex(vertex_arr[i])

    # adding undirected edge between two vertices
    for i in range(0, len(vertex_arr)):
        for j in range(i + 1, len(vertex_arr)):
            g.add_undirected_edge(vertex_arr[i], vertex_arr[j], float(weight_arr2[j][i]))

    vertex_1 = vertex_arr[start]
    dijkstra_shortest_path(g, vertex_1)
    get_shortest_path(vertex_arr[start], vertex_arr[end])

    if(start <= end):
        #print(vertex_arr[end].distance)
        return vertex_arr[end].distance
    else:
        return 'ERROR::make sure start is less than or equal to end'


def getTimeBetweenPXandPY(time_string, distanceFromPXtoPy):
    # print(time_string)
    h, m, s = time_string.split(':')
    current_time = timedelta(hours=int(h), minutes=int(m))
    # print(current_time)
    travel_time = timedelta(hours=distanceFromPXtoPy / 18)
    # print(travel_time, (current_time + travel_time))

    calc_time = current_time + travel_time

    formatted_timedelta_current_time = f"{calc_time.seconds // 3600:02}:{(calc_time.seconds // 60) % 60:02}:{calc_time.seconds % 60:02}"
    #formatted_timedelta_travel_time = f"{current_time.seconds // 3600:02}:{(current_time.seconds // 60) % 60:02}:{current_time.seconds % 60:02}"

    #print(formatted_timedelta_current_time)

    #print(formatted_timedelta_current_time + travel_time)

    return formatted_timedelta_current_time

def getTruckRoute(trk):
    total = 0
    currentTime = trk.time
    pkS = 0
    pkE = 0

    #arrList = []

    for i in range(0, len(trk.packageList)):
        if trk.location == "At Hub":
            pkS = city_arr2.index(" HUB")
            pkE = city_arr2.index(" "+packageLookUp(trk.packageList[i]).addr+"\n("+packageLookUp(trk.packageList[i]).zipcode+")")
            trk.location = "Delivered"
        else:
            pkS = city_arr2.index(" " + packageLookUp(trk.packageList[i - 1]).addr + "\n(" + packageLookUp(trk.packageList[i - 1]).zipcode + ")")
            pkE = city_arr2.index(" " + packageLookUp(trk.packageList[i]).addr + "\n(" + packageLookUp(trk.packageList[i]).zipcode + ")")
            trk.location = "Delivered"

        if pkS < pkE:
            temp_var = getMinimumDistanceBetween2Cities(pkS, pkE)
            #print(round(temp_var, 1))
            currentTime = getTimeBetweenPXandPY(str(currentTime), temp_var)
            #print(currentTime, trk.location)
            total += temp_var
            trk.mileage = total
            trk.time = str(currentTime)
            packageLookUp(trk.packageList[i]).status[0] = "Delivered"
            packageLookUp(trk.packageList[i]).status[1] = str(currentTime)
            #arrList.append({"truck":trk.num, "packageID":trk.packageList[i], "distanceTraveled": total,"status":trk.location, "time":str(currentTime)})
            #print("Not Switched")

        else:
            temp_var = getMinimumDistanceBetween2Cities(pkE, pkS)
            #print(round(temp_var, 1))
            currentTime = getTimeBetweenPXandPY(str(currentTime), temp_var)
            #print(currentTime, trk.location)
            total += temp_var
            trk.mileage = total
            trk.time = str(currentTime)
            packageLookUp(trk.packageList[i]).status[0] = "Delivered"
            packageLookUp(trk.packageList[i]).status[1] = str(currentTime)
            #arrList.append({"truck": trk.num, "packageID": trk.packageList[i], "distanceTraveled": total,"status": trk.location, "time": str(currentTime)})
            #print("Switched")

        if i == len(trk.packageList) - 1 and pkS < pkE:
            temp_var = getMinimumDistanceBetween2Cities(city_arr2.index(" HUB"), pkE)
            #print(temp_var)
            currentTime = getTimeBetweenPXandPY(str(currentTime), temp_var)
            trk.location = "At Hub"
            #print(currentTime, trk.location)
            total += temp_var
            trk.mileage = total
            trk.time = str(currentTime)
            #packageLookUp(trk.packageList[i]).status[0] = "At Hub"
            #packageLookUp(trk.packageList[i]).status[1] = str(currentTime)
            #arrList.append({"truck": trk.num, "packageID": trk.packageList[i], "distanceTraveled": total, "status": trk.location, "time": str(currentTime)})
        elif i == len(trk.packageList) - 1 and pkS > pkE:
            temp_var = getMinimumDistanceBetween2Cities(city_arr2.index(" HUB"), pkS)
            #print(temp_var)
            currentTime = getTimeBetweenPXandPY(str(currentTime), temp_var)
            trk.location = "At Hub"
            #print(currentTime, trk.location)
            total += temp_var
            trk.mileage = total
            trk.time = str(currentTime)
            #packageLookUp(trk.packageList[i]).status[0] = "At Hub"
            #packageLookUp(trk.packageList[i]).status[1] = str(currentTime)
            #arrList.append({"truck": trk.num, "packageID": trk.packageList[i], "distanceTraveled": total, "status": trk.location, "time": str(currentTime)})

    return trk

trk1 = getTruckRoute(truck(1, [15,40,37, 13,14, 16,19,20, 31, 34], "At Hub", "At Hub", "08:00:00", "08:00:00", 0))
trk2 = getTruckRoute(truck(2, [1, 6, 25, 29, 30, 3, 9, 18, 36, 38], "At Hub", "At Hub", "09:05:00", "09:05:00", 0))
trk1_2 = getTruckRoute(truck(1, [], "At Hub", "At Hub", trk1.time, trk1.time, trk1.mileage))

"1, 6, 25, 29, 30, 3, 18, 36, 9, 38, 11, 17, 21, 12"

#print(trk1.mileage)
#print(trk2.mileage)
#print(trk1_2.mileage)

#print(trk1.mileage + trk2.mileage + trk1_2.mileage)

myInputTime = "10:30:00"

#print("All Package Statuses at", myInputTime)
for i in range(1, 41):
    if packageLookUp(i).ID in trk1.packageList:
        truck = "trk1"
    elif packageLookUp(i).ID in trk2.packageList:
        truck = "trk2"
    elif packageLookUp(i).ID in trk1_2.packageList:
        truck = "trk1_2"
    else:
        truck = "no truck has loaded the package yet"

    #print(truck)

    if myInputTime < packageLookUp(i).status[1]:
        packageLookUp(i).status[0] = "En Route"

    if myInputTime < trk2.startingTime and truck == "trk2":
        packageLookUp(i).status[0] = "At Hub"

    if myInputTime < trk1.time and truck == "trk1_2":
        packageLookUp(i).status[0] = "At Hub"

    if myInputTime >= "10:20:00":
        packageLookUp(9).addr = "410 S State St"
        packageLookUp(9).zipcode = "84111"

    #print("Package ID:", packageLookUp(i).ID,", ", packageLookUp(i).addr, ", ",packageLookUp(i).city, ", ",packageLookUp(i).zipcode, ", ",packageLookUp(i).deadline, ", ",packageLookUp(i).weight , " --- ", packageLookUp(i).status[0], " at ", packageLookUp(i).status[1] if packageLookUp(i).status[0] == "Delivered" else myInputTime)

#Write a program that will display the optimal destination for each element for each truck

def getaShorterDistance(arrTest)

'''print("\nDijkstra shortest path:")
for v in g.adjacency_list:
    if v.pred_vertex is None and v is not vertex_1:
        print("1 to %s ==> no path exists" % v.label)
    else:
        print("1 to %s ==> %s (total distance: %g)" % (v.label, get_shortest_path(vertex_1, v), v.distance))'''

#for i in range(len(myHash.table)+1):
    #print("Key: {} and Package: {}".format(i + 1, myHash.search(i + 1)))

#print(packageLookUp(1).status[1])