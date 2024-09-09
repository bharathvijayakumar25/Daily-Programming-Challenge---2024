def median_find(a):
    ascen_list = []
    
    while len(a) > 0:
        min_val = a[0]
        for j in range(len(a)):
            if a[j] < min_val:
                min_val = a[j]
        ascen_list.append(min_val)
        a = [x for x in a if x != min_val]

    n = len(ascen_list)
    
    # Calculate median
    if n % 2 == 0:
        median = (ascen_list[n // 2 - 1] + ascen_list[n // 2]) / 2
    else:
        median = ascen_list[n // 2]
    
    return median

# Input processing
arr = input("arr: ")
try:
    list1 = [int(i) for i in arr.split(",")]
except ValueError:
    print("Invalid input. Please enter a list of integers separated by commas.")
else:
    print("arr:", list1)
    if len(list1) > 0:
        value = median_find(list1)
        print("Output:", value)
    else:
        print("The list is empty!")
