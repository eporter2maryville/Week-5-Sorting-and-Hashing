# Name: Brent Porter
# GitHub ID: eporter2maryville
# Assignment: 5.1.3 Insertion Sort

testIntegers = [ 10,2,5,4,1,3,7,9,8,6 ]

def insertionSort(list):
    n = len(list)
    #loop to run it the correct number of passes and assigns the first item to the new list
    for index in range(1,n):
        currentValue = list[index]
        position = index
        #compares each successive item to the current list and places it appropriately
        while position>0 and list[position-1]>currentValue:
            list[position] = list[position-1]
            position = position-1
            
        list[position]=currentValue
    
def main():
    print(testIntegers) #original jumbled list
    insertionSort(testIntegers) #performing sort
    print(testIntegers) #sorted list
    
    
main()