# method 1 count of a specific character

def total_occurrences(s,c):
    total = s.count(c)
    return total

print(total_occurrences("Nosferaatu",'a'))

# method 2 count of all characters

def count_all(s):
    counts = {}
    for char in set(s):
        if char.isalpha():
            counts[char] = s.count(char)
    return dict(counts)

print(count_all("Ford V Ferrari"))