import numpy as np

# Transforme une liste L en matrice numpy
np.array(L)

# Crée une matrice ligne de n valeurs uniformément réparties entre a et b (inclus)
np.linspace(a, b, n)

# Crée la matrice nulle de taille n x m
np.zeros((n, m))

# Crée la matrice remplie de 1 de taille n x m
np.ones((n, m))

# Crée la matrice identité de taille n
np.eye(n)

# Crée la matrice diagonale dont les termes diagonaux sont les éléments de la liste L
np.diag(L)

# Calcule de la transposée de la matrice M
np.transpose(M)
M.T

# Multiplication matricielle de M par P
np.dot(M, P)
M @ P

# Somme de tous les éléments de M
np.sum(M)
M.sum()

# Le plus grand des éléments de M
np.max(M)
M.max()

# Le plus petit des éléments de M
np.min(M)
M.min()

# Renvoie dans un couple le format de la matrice M
np.shape(M)

# Renvoie le nombre d'éléments de M
np.size(M)

# Accéder à l'élément (i, j) de M
M[i, j]

# Accéder à la i-ième ligne de M
M[i, :]

# Accéder à la j-ième colonne de M
M[:, j]
