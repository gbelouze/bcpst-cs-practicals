from random import random
from time import time

L = [random() for k in range(10_000)]  # a list of random floats between 0 and 1
L.sort()

start = time()
find_naive(L, 0.5)
end = time()
print("find_naive took {} seconds".format(end - start))

start = time()
find_dichotomique(L, 0.5)
end = time()
print("find_dichotomique took {} seconds".format(end - start))
