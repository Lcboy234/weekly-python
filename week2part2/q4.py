# Write a function reverse() that takes one argument that can be either 
# a string as input, and returns its reversal.

# For example, reverse("left to right") should return the string "thgir ot tfel".

def reverse(any_input):
    reversed_string = ""

    for i in any_input:
        reversed_string = i + reversed_string
        # l + ""
        # e + l
        # f + el
    return reversed_string
    
print(reverse("left to right"))