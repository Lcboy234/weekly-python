def get_duplicates(input):
    final = {}

    for word in input:
        if word in final:
            final[word] += 1
        else:
            final[word] = 1

    second_dic = {}

    for word in final:
        if final[word] > 1:
            second_dic[word] = final[word]
    
    return second_dic

answer = get_duplicates(['it', 'is', 'the', 'right', 'right', 'is', 'not', 'it', 'right'])
print(answer)