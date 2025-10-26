# Write a function make_histogram() that takes a string of letters as input 
# argument and returns a dictionary mapping each letter to its frequency. 
# For example, make_histogram('parrot') should return

# {'p': 1, 'a': 1, 'r': 2, 'o': 1, 't': 1}

# (not necessarily in this order).

# Test you implementations on several inputs, and make sure it works correctly.

def make_histogram(a):
    # get an empty histogram
    histogram = {}
    # for loop i into the input
    for i in a:
        # check if i is in histogram and 
        # loop into the histogram
        if i in histogram:
            # every histogram[i]
            # for example histogram[r]
            # repeated twice
            # so add 1 to it to make it 2
            histogram[i] += 1
        else:
            # else keep it as 1
            histogram[i] = 1
    # return the entire histogram
    return histogram

final = make_histogram('parrot')
print(final)