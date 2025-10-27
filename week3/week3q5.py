def inverted_dict(input):

    inverted = {}

    for key in input:
        value = input[key]
        inverted.setdefault(value, []).append(key)

    return inverted

test = inverted_dict({'p': 1, 'a': 1, 'r': 2, 'o': 1, 't': 1})
print(test)