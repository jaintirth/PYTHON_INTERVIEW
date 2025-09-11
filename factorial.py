# method 1 using loop

def fact(n):
    result = 1
    i=n
    while(i!=0):
        result = result*i
        i=i-1
    return result

print(fact(6))

# method 2 using recursion

def rec_fact(n):
    if n==1 or n==0:
        return 1
    return n*rec_fact(n-1)

print(rec_fact(6))