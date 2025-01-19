
#Creating node

class Node:

    def __init__(self,x): # Initialize Node
        self.data = x
        self.next = None

#Creation of Hastable
class HashOpen:

    def __init__(self, size = 10):
        self.bucket_size = [None] * size #Initialize bucket size


    def Hash(self,x): #function to calculate the index
        return x % len(self.bucket_size) #return the result of x modulo of bucket size length

    def insert_data(self,x):
        index = self.Hash(x) #find the index using hash
        new_Node = Node(x) #Create new node

        #iF the bucket is empty, place the new node there
        if self.bucket_size[index] is None:
            self.bucket_size[index] = new_Node
        else:
            #if the bucket is not empty, find the last node and append the new node
            p = self.bucket_size[index]
            while p.next is not None:
                p = p.next

            p.next = new_Node # ituturo mo yung pointer to the next node


    def delete_data(self,x):
        #calculate the index suing the hash function
        index = self.Hash(x)
        p = self.bucket_size[index]
        q = None

        #traverse the linked list at the index to find the node to delete
        while p is not None:
            if p.data == x:
                if q is None:
                    #the node to delete is the first node in the list
                    self.bucket_size[index] = p.next

                else:
                    #the node to delete is in the middle or end
                    q.next = p.next
                    return

            q = p
            p = p.next

    def display(self):
        for i in range(len(self.bucket_size)): # Use len(self.bucket_size) to get the size of the hash table
            print(f"Index {i}: ",end=" ")
            p = self.bucket_size[i]
            while p is not None:
                print(p.data, end =" ")
                p = p.next
            print()

ht = HashOpen()

# Insert data into the hash table
ht.insert_data(15)
ht.insert_data(25)
ht.insert_data(35)
ht.insert_data(5)
ht.insert_data(10)
ht.insert_data(30)

# Display the hash table contents
print("Hash table contents: ")
ht.display()

# Delete some data
ht.delete_data(25)  # Should delete 25
ht.delete_data(5)   # Should delete 5
ht.delete_data(100) # Should print a message that 100 is not found

# Display the hash table after deletions
print("Hash table contents after deletion: ")
ht.display()