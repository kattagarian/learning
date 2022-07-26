from itertools import permutations
perm = permutations(["A", "B", "C", "D"])

for i in list(perm):
    print(f"T = {i}")