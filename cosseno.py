def fatorial(atual, anterior):
    if atual == 0:
        return 1
    else:
        fatorial = (atual)*(atual-1)*anterior
        return fatorial

def expoente(x, n):
    contador = 0
    final = x
    if n == 0:
        return 1
    else:
        while contador != n-1:
            final = final*x
            contador += 1
            #print(contador, final)
        return final

def divisao(x, y):
    return x/y


x = float(input())
n = 0
fatorial_atual = 1
fatorial_anterior = 1
numerador = 1
total = 0
while n != 50:
    if n%2 == 0:
        numerador = -1
    else:
        numerador = 1
    cosseno = divisao((-1)*numerador, fatorial(2*n, fatorial_anterior))*expoente(x, 2*n)
    #cosseno = (((-1)*numerador)/(fatorial(2*n, fatorial_anterior)))*(expoente(x, 2*n))
    fatorial_anterior = fatorial(2*n, fatorial_anterior)
    #print(n, numerador, fatorial_anterior)
    #print(expoente(5, 0))
    total = total + cosseno
    #print(n)
    n += 1

print("%.4f"%total)