# Name: Brent Porter
# GitHub ID: eporter2maryville
# Assignment: 5.2 Perfect Hash

from random import *

#selects a random hash table location to place the name
def perfectHash(tablesize):
    slot = randrange(0,tablesize)
    return slot

#creates a hashTable based on the original table size. Supports lists up to 19 items in length, uses prime
#numbers with reasonable spacing (roughly logarithmically spaced)
def createHashTable(tableSize):
    hashTable=[]
    if tableSize <= 7:
        hashTableLength=7
    elif tableSize <= 11:
        hashTableLength = 11
    elif tableSize <= 19:
        hashTableLength = 19
    else:
        print('Your list is too large to hash with this program, sorry.')
    for index in range(hashTableLength):
        hashTable.append(None)
    
    return hashTable
    
        
    
def main():
    names=['Brent','Kalee','Lucas','Kim','Eric','Molly','Lauren', 'Gabe', 'Alli', 'Mackey']
    print(names)
    tableSize=len(names)
    
    hashTable=createHashTable(tableSize)
    hashLength=len(hashTable)
    #runs the list through the hash process, and if the slot is occupied handles the collision by selecting another
    #placement repeatedy until an available slot is found
    for index in names:
        namePlacement = perfectHash(hashLength)
        while hashTable[namePlacement] != None:
            namePlacement = randrange(0,tableSize)
        hashTable[namePlacement] = index
        
    print(hashTable)
        
main()
        