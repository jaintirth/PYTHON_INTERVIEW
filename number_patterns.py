n=5 

# increasing number
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
print()    

# decreasing number
for i in range(n,0,-1):
    for j in range(n,i-1,-1):
        print(j,end=' ')
    print()
print()

# repeated numbers
for i in range(1,n+1):
    for  j in range(1,i+1):
        print(i,end=' ')
    print()
print()

# floyd's triangle
num=1
for i in range(1,n+1):
    for j in range(i):
        print(num,end=' ')
        num+=1
    print()
print()