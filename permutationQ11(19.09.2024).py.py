import math
import itertools

def permutation(a):
    permutationi = set()  
    for perm in itertools.permutations(a):  
        word = ''.join(perm)
        permutationi.add(word)
        permutationi.add(word[::-1])  
    return list(permutationi)

a = input("Input: ").strip()
p = permutation(list(a))
print("Output:", sorted(p))