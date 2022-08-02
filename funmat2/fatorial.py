def fatorial(n):
    if n < 0:   return 0    #Fatorial só pode ser calculado por um número inteiro não-negativo, logo usaremos 0 caso n < 0
    elif n == 0:    return 1    #Caso base
    else:   return n*fatorial(n-1)  #Quando n > 0, o resultado será n*n-1*n-2 até alcançar o caso base, que é 1

def main(): #função main que declara a variável e chama a função fatorial
    n = int(input()) 
    print(fatorial(n))

main()
