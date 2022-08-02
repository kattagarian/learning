def buscalinear(lista, i, j, x):
    if len(lista) == 0: return -1 #Caso a lista estiver vazia, retorno -1
    for i in range(j):  #loop que checa todos os elementos da lista em busca do x
        if lista[i] == x: return i  #Se encontrar o elemento, retorna a posição dele
    return -1   #Se o x não for encontrado, sairá do loop e retornará -1

def main():
    lista = [int(i) for i in input().split()]   #Declaração da lista
    i, j, x = int(input()), int(input()), int(input())  #declaração das variáveis
    print(buscalinear(lista, i, j+1, x)) #Chamando a função e printando o resultado

main()