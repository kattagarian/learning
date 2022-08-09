def buscalinear(lista, i, j, x):
    if len(lista) < 1: return -1    #Caso a lista estiver vazia (menor que 1), retorno -1
    elif lista[i] == x: return i    #Se o primeiro elemento é x, retorna a posição dele
    elif lista[j] == x: return j    #Se o último elemento é x, retorna a posição dele
    return buscalinear(lista, i+1, j-1, x)   #Se o x não for encontrado, diminuirá o escopo e tentará novamente
#Exemplo: Se [0, 1, 2, 3, 4] é nossa lista, com i = 0, j = 5 e x = 2
#Ele verificará na primeira vez se 0 e 4 (o primeiro e último) são nossos x. Se sim, retorna a posição deles
#Se não, ele chama recursivamente a mesma função mas diminui o escopo, agora i = 1, j = 4 e x continua o mesmo
#E analisa novamente o primeiro e último, que atualmente serão 1 e 3 reespectivamente. E fará isso até achar o valor 

def main():
    lista = [int(i) for i in input().split()]   #Declaração da lista
    i, j, x = int(input()), int(input()), int(input())  #declaração das variáveis
    print(buscalinear(lista, i, j, x)) #Chamando a função e printando o resultado
main()
