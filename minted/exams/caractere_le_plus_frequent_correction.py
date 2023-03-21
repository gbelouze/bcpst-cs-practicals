def caractere_le_plus_frequent(message):
    c_to_count = {}
    for c in message:
        if c != ' ':
            if c in c_to_count:
                c_to_count[c] += 1
            else:
                c_to_count[c] = 1
    maxcount, maxc = 0, 'e'
    for c, count in c_to_count.items():
        if count > maxcount:
            maxcount, maxc = count, c
    return maxc
