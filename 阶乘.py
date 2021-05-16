
def fib(N):
    if N == 1 or N == 2:
        return 1
    else:
        a, b  = 1, 1
        for i in range(3, N+1):
            c =a  + b
            a = b
            b = c
        return c
        

N = int(input())
print(fib(N))