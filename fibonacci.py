# fibonacci upto a specific number

def fib_upto(n):
    a,b = 0,1
    while a<=n:
        print(a,end=' ')
        a,b = b,a+b

fib_upto(40)


# fibonacci upto given terms

def fib(n):
    a, b = 0, 1
    for i in range(a,n):
        print(a,end=' ')
        a, b = b, a+b

fib(9)