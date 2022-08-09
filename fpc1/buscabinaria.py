from math import floor

def buscabinaria(x, lista, contador):
    n = len(lista)  #Tamanho da lista
    if n%2 == 0:    meio = int(n/2) #Se par, usa o meio tradicional
    else:   meio = int(floor(n/2))  #Se impar, usa a função floor para arredondar para baixo
    #print(lista, contador)
    if lista[meio] == x: return contador    #Verifica se o meio é o valor procurado
    else:
        if n <= 2:  return contador #Se possui 2 ou menos elementos, retorna o contador. Já que ou o elemento alvo está entre os dois ou não está
        if lista[meio] < x:
            return buscabinaria(x, lista[meio:], contador+1)    #procura a primeira metade da lista
        else:
            return buscabinaria(x, lista[:meio], contador+1)    #Procura a segunda metade da lista

def main():
    contador = 1
    lista = [int(i) for i in input().split()]   #Declaração de x e lista
    print(buscabinaria(lista[0], lista[1:], contador))
main()
