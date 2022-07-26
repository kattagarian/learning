def fatorial(fatorial_atual, fatorial_anterior):
    #Funcao que calcula o fatorial n (atual) aproveitando o fatorial de (n-2) (anterior)
    if fatorial_atual == 0:
        return 1
    else:
        return (fatorial_atual)*(fatorial_atual-1)*fatorial_anterior

def expoente(base, expoente):
    #Funcao que calcula o expoente repetindo a multiplicacao da base por ela mesma (n-1) vezes.
    contador = 0
    final = base
    if expoente == 0:
        return 1
    else:
        for n in range(0, expoente-1):
            final = final*base
        return final

def divisao(numerador, denominador):
    #Funcao que recebe o numerador e denominador e retorna o resultado da divisao entre eles
    return numerador/denominador

def main():
    #Funcao principal, onde declaramos as variaveis e rodamos o laço principal que soma n vezes a funcao cosseno
    x = float(input())
    n = 0
    fatorial_atual = 1
    fatorial_anterior = 1
    numerador = 1
    total = 0
    for n in range(50):
        if n%2 == 0:
            numerador = -1
        else:
            numerador = 1
        cosseno = divisao((-1)*numerador, fatorial(2*n, fatorial_anterior))*expoente(x, 2*n)
        fatorial_anterior = fatorial(2*n, fatorial_anterior)
        total = total + cosseno
    print("%.4f"%total)

main()