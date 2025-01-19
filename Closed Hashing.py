

class HashTable:

    def __init__(self, bucket_size = 10):
        self.bucket_size = bucket_size
        self.table = [-1] * bucket_size #all the indexes of the list

    def hash(self,x):
        return x % self.bucket_size

    def insert_data(self,x):

        for i in range (self.bucket_size):
            index = self.hash(x + 1)  # get the index where you will put the data
            if self.table[index] > 0:
                continue
            else:
                self.table[index] = x
                return

        print("Table is Full")
        return

    def delete_data(self,x):
        for i in range (self.bucket_size):
            index = self.hash(x + 1) # get the index
            if self.table[index] == x:
                self.table[index] = -1
                return
        print("Data not Found")


    def display(self):
        for i in range (self.bucket_size):
            if self.table[i] > -1:
                print(self.table[i], end= " ")

            else:
                print("_", end = " ")

    def locate(self,x):

        for i in range (self.bucket_size):
            index = self.hash(x+1)
            if self.table[index] == x:
                return index

        print("Data not found")
        return


ht = HashTable()

ht.insert_data(10)
ht.insert_data(5)
ht.insert_data(14)

print("Hash Table contents: ")
ht.display()




