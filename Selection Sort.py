# Name: Brent Porter
# GitHub ID: eporter2maryville
# Assignment: 5.1.2 Selection Sort

testIntegers = [ 10,2,5,4,1,3,7,9,8,6 ]

#The selection sort identifies the number that should be at the end of the list and then places it there.
#Each successive pass builds the list by placing the next to last number until all numbers are in place.

def selectionSort(list):
    n = len(list)
    
    #determines number of passes
    for fillslot in range (n-1, 0, -1):
        positionOfMax=0
        #iterates through list
        for location in range (1, fillslot+1):
            if list[location]>list[positionOfMax]:
                positionOfMax = location
        #places selected number
        temp = list[fillslot]
        list[fillslot] = list[positionOfMax]
        list[positionOfMax] = temp

def main():
    print(testIntegers) #original jumbled list
    selectionSort(testIntegers) #performing sort
    print(testIntegers) #sorted list
    
    
main()
