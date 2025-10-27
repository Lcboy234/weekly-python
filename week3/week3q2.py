def has_duplicates(input):
    seen = {}

    for word in input:
        if word in seen:
            return True
        seen[word] = None
    return False

first = has_duplicates(['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'])
print(first)
second = has_duplicates(['magic', 'tree', 'house'])
print(second)
