def intersects(l1, l2):
    return[x for x in l1 if x in l2]

l1 = ['a','b','c','d']
l2 = ['b','k','d']

print(intersects(l1,l2))