import pandas as pd
def f(a):
    sub_array = []
    for i in range(0,len(a)):
        k = 0
        sume  = 0
        temper = []
        temper.append(a[i])
        for j in range(i+1,len(a)):
            temper.append(a[j])
            sume = sum(temper)
            if sume==0:
                sub_array.append((i,j))
    return sub_array
a = input("enter the elements :").strip()
a = [int(x) for x in a.split(",")]
arr  = f(a)
df = pd.DataFrame(arr, columns=['first', 'second'])
result = df.loc[df.groupby('first')['second'].idxmax()]
result = list(result.itertuples(index=False, name=None))
print(result)
