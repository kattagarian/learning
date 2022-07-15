'''Nand(a=a[0], b=b[0], out=nandout);
    Not(in=nandout, out=out[0]);'''
x = int(input())

for i in range(x):
    print(f"Nand(a=a[{i}], b=b[{i}], out=nandout{i});\nNot(in=nandout{i}, out=out[{i}]);\n")