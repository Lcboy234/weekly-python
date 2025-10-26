def has_duplicates(a):
    duplicate = {}
    for i in a:
        if i in duplicate:
            if duplicate[i] > 1:
                return True
            elif duplicate[i] = 1:
                return None
            else:
                return False