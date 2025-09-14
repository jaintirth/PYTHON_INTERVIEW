def factors(n):
    factors = [1,n]
    for i in range(2,n):
        if(n%i==0):
            factors.append(i)
    return sorted(factors)

print(factors(27))