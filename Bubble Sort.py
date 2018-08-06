# Name: Brent Porter
# GitHub ID: eporter2maryville
# Assignment: 5.1.1 Bubble Sort

testIntegers = [ 10,2,5,4,1,3,7,9,8,6 ]

def bubbleSort(list):
    n = len(list)
    
    for i in range(n-1, 0, -1):
        for j in range(i):
            if list[j]>list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
                
def main():
    print(testIntegers) #original jumbled list
    bubbleSort(testIntegers) #performing sort
    print(testIntegers) #sorted list
    
    
main()

        