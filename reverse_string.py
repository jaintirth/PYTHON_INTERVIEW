# method 1 (preferred)
def reverse_string(s):
    return s[::-1]

print(reverse_string('hello'))

# method 2
def rev_string(s):
    result = ''
    for char in s:
        result = char + result
    return result

print(rev_string('tirth'))