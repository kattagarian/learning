def mdc(a, b):  #Recebe dois valores, a e b e retorna o mdc
    if a == 0 and b == 0:   #Quando ambos os valores são zero, temos uma indeterminação matemática
        print("indeterminado")
        quit()  #Sem a função quit, o programa não encerrará
    if b == 0: return a    #Caso base. Se b = 0, a será o mdc dos dois números.
    else: return mdc(b, a%b) #Nós calculamos o resto de a e b e trocamos a posição de b para calcularmos ambos a cada iteração.

def main(): #função que declara as variaveis e chama a func mdc
    a, b = int(input()), int(input())
    print(mdc(a, b))

main()