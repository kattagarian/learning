import math
import numbers

def escopo_numero(x):
    if x < 2 or x > 100:
        while x < 2 or x > 1000:
            x = int(input("Valor fora do escopo. Digite N:"))
        return x
    else:
        return x

def int_list(y):
    split = list(map(int, y.split()))
    split.sort()
    return split

def compara(lista, n):
    if len(lista) != (n - 1):
        print("Tamanho da lista inválido")
        return False
    else:
        return True

def num_repet(z):
    actual_item = math.nan
    contador = 0
    for item in z:
        last_item = actual_item
        actual_item = item
        if last_item == actual_item:
            print("Não pode haver numeros repetidos")
            return False
        else:
            contador = contador + 1
            if contador == len(z):
                return True

def num_ausente(lista):
    actual = math.nan
    if lista[0] != 1:
        return 1
    else:
        for item in lista:
            last = actual
            actual = item
            if actual == (last + 1):
                continue
            elif actual == (last + 2):
                return (actual - 1)

Quantos_numeros = int(input("Digite N:"))
Quantos_numeros = escopo_numero(Quantos_numeros)
bool1 = bool2 = False
while bool1 == False or bool2 == False:
    Quais_numeros = input(f"Digite {Quantos_numeros - 1} valores:")
    bool1 = compara(int_list(Quais_numeros), Quantos_numeros)
    bool2 = num_repet(int_list(Quais_numeros))
num_aus = num_ausente(int_list(Quais_numeros))
print(num_aus)