def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

def prime_in_range(start,end):
    print(f"Prime numbers between {start} and {end} are : ")
    for i in range(start,end+1): # to include end number
        if(is_prime(i)):
            print(i,end=' ')
    print()


prime_in_range(10,100)