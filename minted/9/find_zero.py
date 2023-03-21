from math import sin

def find_zero(a, b, n_iteration):
    if sin(a) > 0 or sin(b) < 0:
        return "Cannot do a dichotomy"
    
    for i in range(n_iteration):
        mid = (a + b)/2
        if sin(mid) > 0:
            a, b = ...
        else:
            a, b = ...

    return a, b


