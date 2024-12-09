from operator import truediv


class ChainingHashTable:
    def __init__(self, initial_capacity=10):
        self.table = []
        #self.num = 5
        for i in range(initial_capacity):
            self.table.append([])

    def insert(self, key, item):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        #print(self.num)

        #bucket_list.append(item)
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

        #if key in bucket_list:
            #item_index = bucket_list.index(key)
           # return bucket_list[item_index]
        #else:
            #return None

    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        #if key in bucket_list:
            #bucket_list.remove(key)

        for n in bucket_list:
            if n[0] == key:
                bucket_list.remove([n[0], n[1]])

#myHash = ChainingHashTable()

#myHash.insert(1)
#myHash.insert(1)

#print(myHash.table)

bestMovies = [
    [1, "CITIZEN KANE - 1941"],
    [2, "CASABLANCA - 1942"],
    [3, "THE GODFATHER - 1972"],
    [4, "GONE WITH THE WIND - 1939"],
    [5, "LAWRENCE OF ARABIA - 1962"],
    [6, "THE WIZARD OF OZ - 1939"],
    [7, "THE GRADUATE = 1967"],
    [8, "ON THE WATERFRONT - 1954"],
    [9, "SCHINDLER'SLIST - 1993"],
    [10, "SINGIN IN THE RAIN - 1952"],
    [11, "STAR WARS - 1977"]
]

myHash = ChainingHashTable()

myHash.insert(bestMovies[0][0], bestMovies[0][1])
myHash.insert(bestMovies[1][0], bestMovies[1][1])
myHash.insert(bestMovies[10][0], bestMovies[10][1])

print(myHash.table)