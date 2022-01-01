##############
# Hash Table #
##############

'''
The Hash table data structure stores elements in key-value pairs where
- Key - unique integer that is used for indexing the values
- Value - data that are associated with keys.
         _____________
        | Key | Value |
        |_____|_______|     Key and Value in Hash table

Hashing (Hash Function)
In a hash table, a new index is processed using the keys. And, the element corresponding to that key is stored in the index. This process is called hashing.
Let k be a key and h(x) be a hash function.
Here, h(k) will give us a new index to store the element linked with k.

Hash Collision
When the hash function generates the same index for multiple keys, there will be a conflict (what value to be stored in that index). This is called a hash collision.
We can resolve the hash collision using one of the following techniques.
- Collision resolution by chaining
- Open Addressing: Linear/Quadratic Probing and Double Hashing

1. Collision resolution by chaining (Open Hashing/ Closed addressing)
   In chaining, if a hash function produces the same index for multiple elements, these elements are stored in the same index by using a doubly-linked list.
        | / | 0
        | / |
        |   |-->| k1 |-->| k4 |
        | / |
        | / |
        |   |-->| k5 |-->| k2 |-->| k6 |
        | / |
        |   |-->| k7 |-->| k3 |
        |   |-->| k8 |
        | / |m-1

2. Open Addressing (Closed Hashing)
   Unlike chaining, open addressing doesn't store multiple elements into the same slot. Here, each slot is either filled with a single key or left NIL.
   Different techniques used in open addressing are:
   a. Linear probing
   b. Quadratic probing
   c. Double Hashing technique

   a. Linear probing
      When the collision occurs by mapping a new key to the cell already occupied by another key, then linear probing technique searches for the closest free locations and adds a new key to that empty cell. In this case, searching is performed sequentially, starting from the position where the collision occurs till the empty cell is not found.
      The problem with linear probing is that a cluster of adjacent slots is filled. When inserting a new element, the entire cluster must be traversed. This adds to the time required to perform operations on the hash table.

   b. Quadratic Probing
      In case of linear probing, searching is performed linearly. In contrast, quadratic probing is an open addressing technique that uses quadratic polynomial for searching until a empty slot is found.
      It can also be defined as that it allows the insertion ki at first free location from (u+i2)%m where i=0 to m-1.

   c. Double Hashing
      When the collision occurs then this technique uses the secondary hash of the key. It uses one hash value as an index to move forward until the empty location is found.
      In double hashing, two hash functions are used. Suppose h1(k) is one of the hash functions used to calculate the locations whereas h2(k) is another hash function. It can be defined as "insert ki at first free place from (u+v*i)%m where i=(0 to m-1)". In this case, u is the location computed using the hash function and v is equal to (h2(k)%m).

Applications of Hash Table
Hash tables are implemented where
- constant time lookup and insertion is required
- cryptographic applications
- indexing data is required
'''

# Program to demonstrate working of HashTable 

hashTable = [[],] * 10

def checkPrime(n):
    if n == 1 or n == 0:
        return 0

    for i in range(2, n//2):
        if n % i == 0:
            return 0

    return 1

def getPrime(n):
    if n % 2 == 0:
        n = n + 1

    while not checkPrime(n):
        n += 2

    return n

def hashFunction(key):
    capacity = getPrime(10)
    return key % capacity

def insertData(key, data):
    index = hashFunction(key)
    hashTable[index] = [key, data]

def removeData(key):
    index = hashFunction(key)
    hashTable[index] = []


insertData(123, "apple")
insertData(432, "mango")
insertData(213, "banana")
insertData(654, "guava")

print(hashTable)

removeData(123)

print(hashTable)