contador = 0
somatorio = 0
for i in range(11):
    funcao = (2**(i+1))-(2**(i))
    print(funcao)
    somatorio = funcao + somatorio
print(somatorio)