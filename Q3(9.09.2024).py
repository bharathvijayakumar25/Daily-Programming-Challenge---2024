"""Sort an Array of 0s, 1s, and 2sYou are given an array arr consisting only of 0s, 1s, and 2s. 
The task is to sort the array in increasing order in linear time (i.e., O(n)) without using any extra space.
 This means you need to rearrange the array in-place.
"""
def ascending_order(list1):
    sorted1 = []
    while(len(list1)!=0):
        mine = list1[0]
        a = 0
        for i in range(1,len(list1)):
            if mine>list1[i]:
                a = i
                mine = list1[i]
        sorted1.append(mine)
        mine = list1[0]
        del list1[a]
    return sorted1
arr = input("arr: ")
try:
    list1 = [int(i) for i in arr.split(",")]
except ValueError:
    print("Invalid input. Please enter a list of integers separated by commas.")
else:
    print("arr:", list1)
    if len(list1) > 0:
        value = ascending_order(list1)
        print("Output:", value)
    else:
        print("The list is empty!")
