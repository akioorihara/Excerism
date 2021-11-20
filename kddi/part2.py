#You will be given an upsorted list of inegers and you are required to find the median of the list. For clarity, let's say N is the size of the list. You need to ouput the element 
#which should be at position (N+1)/2 (starting the indexing by 1) if the list is sorted. List size will be given in the first line of the input. 
#List elements will be given in the next line, separated by a single space 

#case 1 
# input 5 
# 3 1 2 5 4 

def FindMedian():

    size = int(input())
    median = int((size+1) / 2)  

    value = input()
    value = value.split()
    value.sort()

    print(value[median-1])

FindMedian()

