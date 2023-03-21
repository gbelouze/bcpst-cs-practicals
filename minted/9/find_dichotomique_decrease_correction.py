def find_dichotomique_decrease(L, x):
    """
    Returns True if x is in L and False otherwise.
    Expects L to be sorted in decrease order
    """
    bottom, top = 0, len(L)  # if x is in L, then its index is in the interval [bottom, top[
    while top - bottom > 0:  # while the interval [bottom, top[ is not empty
        mid = (top + bottom) // 2
        y = L[mid]
        if x == y:
            return True
        elif x < y:
            bottom = mid + 1
        elif x > y:
            top = mid
    return False

