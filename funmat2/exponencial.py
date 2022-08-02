def exponencial(a, n):
    if a == 0 and n == 0:   #não podemos calcular
        print("impossível calcular")
        quit()
    elif n == 0: return 1   #Caso base. Qualquer número (menos o zero) elevaado a 0 é igual a 1
    elif n == 1: return a   #Caso base. Qualquer número elevado a 1 é igual a ele mesmo
    else: return a*exponencial(a, n-1)  #Retorna a multiplicação entre a*a^n-1*a^n-2 até chegar nos casos bases

def main(): #Função que declara as variáveis e chama a função exponencial
    a, n = int(input()), int(input())
    print(exponencial(a, n))

main()