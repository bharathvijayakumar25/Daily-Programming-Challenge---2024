def user_find(a,k):
    i = 0
    max_val  = 0
    while(True):
        for j in range(len(a)):
            max_val  = max_val  if max_val  > a[j] else a[j]
        if i!=(k-1):
            a = [x for x in a if x != max_val]
            i+=1
            max_val =0
        else:
            break
    return max_val
arr = input("arr :")
list1 = list([int(i) for i in arr.split(",")])
print("arr:",list1)
while(True):
    k = int(input("K : "))
    if (k<len(list1)):
        value = user_find(list1,k)
        print("k:",k)
        print("Output:",value)
        break
    else:
        print("index out of range!!")