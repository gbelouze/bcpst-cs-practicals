def find7(x, L):
    for y in L:
        if y < x:
            return False
        if y == x:
            return True
    return False
