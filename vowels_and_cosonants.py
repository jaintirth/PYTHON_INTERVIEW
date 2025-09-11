# method 1 -> drawback if space is in middle 'hello world' it will be counted as consonant , also does not handle "Surekha"

def vowels(s):
    count=0
    for char in s:
        if(char in ('a','e','i','o','u')):
            count=count+1
    return count

def consonants(s):
    total_vowels = vowels(s)
    return len(s)-total_vowels

print(vowels('surekha'))
print(consonants('surekha'))

# method 2

def vow(s):
    count=0
    for char in s.lower():
        if char.isalpha() and char in ('a','e','i','o','u'):
            count+=1
    return count

def cons(s):
    count=0
    for char in s.lower():
        if char.isalpha() and char not in ('a','e','i','o','u'):
            count+=1
    return count

print(vow("Hello World"))
print(cons("Hello World"))