def find1(x, L):
    bottom, top = 0, len(L)
    while top > bottom:
        mid = (top+bottom) // 2
        if x == L[mid]:
            return True
        elif x > L[mid]:
            bottom = mid + 1
        elif x < L[mid]:
            top = mid
    return False


