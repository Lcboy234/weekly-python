def inverted_dict(input_dict):
    new_invert = {}

    for key in input_dict:
        # get the value of the key
        value = input_dict[key]

        if value in new_invert:
            new_invert[value].append(key)
        
        else:
            new_invert[value] = [key]

    return new_invert

data = {'p': 1, 'a': 1, 'r': 2, 'o': 1, 't': 1}
print(inverted_dict(data))