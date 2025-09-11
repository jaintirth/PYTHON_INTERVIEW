n=5
# Left aligned triangle
for i in range(1,n+1):
    print('* ' * i)
print('')

# Right aligned triangle
for i in range(1,n+1):
    print(' ' * (2*(n-i)) + '* ' * i)
print('')

# Pyramid
for i in range(1,n+1):
    print(' ' * (n-i) + '* ' * i)
print('')

# square 
for i in range(1,n+1):
    print("*" * n)
print('')

# Inverted Pyramid
for i in range(n, 0, -1):
    print(' ' * (n-i) + '* ' * i)
print('')

# Diamond Pattern
for i in range(1,n+1):
    print(' ' * (n-i) + '* ' * i)
for i in range(n-1, 0, -1):
    print(' ' * (n-i) + '* ' * i)
print('')
