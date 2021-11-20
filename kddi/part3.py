#Given are two unsorted horizontal lines of integers. You are required to give as ouput, a single vertical list with the elements sorted in decreasing order. 
#List size are give nin the first line of the input. The second line contains the first list of integers separated by single spaces. 
#The third line contains the second list of integers separated by single spaces. The elements of the resulting vertical list must be printed one per line/ 


def MergeLists():

    list1 = []
    ListSizes = input().split()

    for i in range(len(ListSizes)):
        value = input().split()
        list1.extend(value)
    list1.sort(reverse=True)
    
    print("\n")
    for i in list1:
        print(i)

MergeLists()