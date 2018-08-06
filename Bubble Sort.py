# Name: Brent Porter
# GitHub ID: eporter2maryville
# Assignment: 5.1.1 Bubble Sort

testIntegers = [ 10,2,5,4,1,3,7,9,8,6 ]

#The sort takes 2 numbers from the list at a time and compares them,moving the larger on
#This continues until the sort has moved a number the largest number reaches it's proper place in the list.
#At this point the second pass occurs, and the process repeats until all items are in place.

def bubbleSort(list):
    n = len(list)
    #getting the accurate number of passes
    for i in range(n-1, 0, -1):
        for j in range(i):
            #number comparison and placement 
            if list[j]>list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
                
def main():
    print(testIntegers) #original jumbled list
    bubbleSort(testIntegers) #performing sort
    print(testIntegers) #sorted list
    
    
main()

        