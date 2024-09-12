arr1 = input("")
arr2 = input("")
arr1 = list(map(int, arr1.strip("[]").split(",")))
arr2 = list(map(int, arr2.strip("[]").split(",")))
i = 0;j = 0
while i < len(arr1) and j < len(arr2):
    if arr1[i] > arr2[j]:
        arr1[i], arr2[j] = arr2[j], arr1[i]
        pointer = arr2[j]
        k = j + 1
        while k < len(arr2) and arr2[k] < pointer:
            arr2[k - 1] = arr2[k]
            k += 1
        arr2[k - 1] = pointer   
    i += 1
print(arr1,arr2)
