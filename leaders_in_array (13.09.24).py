arr=input("")
arr=list(map(int,arr.strip("[]").split(",")))
leaders=[]
max_from_right=0
for i in range(len(arr)-1,-1,-1):
    if arr[i]>max_from_right:
        leaders.append(arr[i])
        max_from_right=arr[i]
        
print(leaders[::-1])

