arr = input("")
arr = list(map(int, arr.strip("[]").split(",")))
slow_pointer = fast_pointer = 0
while True:
    slow_pointer = arr[slow_pointer]
    fast_pointer = arr[arr[fast_pointer]]

    if slow_pointer == fast_pointer:
        break
slow_pointer = 0
while slow_pointer != fast_pointer:
    slow_pointer = arr[slow_pointer]
    fast_pointer = arr[fast_pointer]
print(slow_pointer)

    
    
    
    
        
        