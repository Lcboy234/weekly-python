def is_leading_string_repeated(s):
    # lorem ipsum dolor sit amethello,hello,hello,
    # len(s) = 44 = n
    n = len(s)
    # in range(1, 14) so it is in range(1, 15)
    # i in range(1, 15)
    for i in range(1, n // 3 + 1):
        # 我的 i 只会检查三分之一
        part = s[-i:]
        if s[-3 * i:] == part * 3:
            return part
    return None

print(is_leading_string_repeated('lorem ipsum dolor sit amethello,hello,hello,'))