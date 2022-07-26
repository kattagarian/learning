somatorio = 0
for i in range(1, 101):
    funcao = 1 + ((-1)**i)
    print(funcao)
    somatorio = funcao + somatorio
print(somatorio)