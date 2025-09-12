n=5

# increasing
for i in range(n+1):
    for j in range(1,i+1):
        print(chr(j+64),end=' ')
    print()
print()

# repeated
for i in range(n+1):
    for j in range(1,i+1):
        print(chr(i+64),end=' ')
    print()
print()