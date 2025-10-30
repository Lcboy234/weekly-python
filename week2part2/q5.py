# A palindrome is a string that is the same as its reversal. 
# Using reverse() write the function partialPalindrome that takes a string s and an integer n as input.

# partialPalindrome 
# returns a boolean that is True is there is a sub-string in s that is a palindrome of length n and False otherwise.

# For example, partialPalindrome("AGTTGCC",4) will return True and partialPalindrome("AGTTGCC",3), will return False.

def reverse(any_input):
    reversed_string = ""

    for i in any_input:
        reversed_string = i + reversed_string
        # l + ""
        # e + l
        # f + el
    return reversed_string

def partialPalindrome(s, n):
    # 7 - 4 + 1 = 4
    # len(4) = 0, 1, 2, 3
    # to lock it in bound
    # AGTT, GTTG, TTGC, TGCC
    for i in range(len(s) - n + 1):
        substring = s[i: i + n]
        if substring == reverse(substring):
            return True
    return False

print(partialPalindrome("AGTTGCC",4))
print(partialPalindrome("AGTTGCC",3))