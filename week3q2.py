def has_duplicates(words):
    seen = {}  # dictionary to store encountered words
    for i in words:
        if i in seen:
            return True  # duplicate found
        seen[i] = None  # store word as key
    return False  # no duplicates found