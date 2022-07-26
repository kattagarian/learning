def fibonacci(N):
    if N == 0:
        return "b"
    elif N == 1:
        return "a"
    else:
        return fibonacci(N-1)+fibonacci(N-2)

N = int(input())
print(fibonacci(N))