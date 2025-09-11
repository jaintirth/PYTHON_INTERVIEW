# method 1

def max_of_three(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c

print(max_of_three(3,5,4))

# method 2

print(max(20,12,21))