import math
def expmod(a, n, m):
    if (a == 0 and n == 0) or (m<=1): #exceções
        print("impossível calcular")
        quit()
    elif n == 0: return 1   #Caso base da multiplicação.
    elif (n%2) == 0: return (expmod(a, n/2, m)**2)%m #Quando par
    else: return (((expmod(a, math.floor(n/2), m)**2)%m)*(a%m))%m #Quando impar

def main():
    a, n, m = int(input()), int(input()), int(input()) 
    print(expmod(a, n, m))
main()