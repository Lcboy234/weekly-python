def invert_dict(input):
    inverted = {}

    for key in input:
        value = input[key]

        if value in inverted:
            inverted[value].append(key)
        else:
            inverted[value] = [key]

    input.clear()

    input.update(inverted)

data = {'p': 1, 'a': 1, 'r': 2, 'o': 1, 't': 1}
invert_dict(data)
print(data)