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

def packageLookUp(ID):
    return myHash.search(ID)

myHash = ChainingHashTable()

loadPackageCSV("PackageCSV.csv")

print(packageLookUp(3))

#for i in range(len(myHash.table)+1):
 #  print("Key: {} and Package: {}".format(i + 1, myHash.search(i + 1)))

#myHash.insert(1)
#myHash.insert(1)

#1d to access the bucket, 2d to access a key value pair in the bucket, and 3d to access the specific itm in the key value
# pair, in the below case, the object itself

#kv = myHash.table[1][1][1]
#print(kv)