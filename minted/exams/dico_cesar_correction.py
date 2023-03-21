def dico_cesar(k):
    dico = {}
    for clef, valeur in dico_code_cesar0.items():
        dico[clef] = (valeur + k) % 26
    return dico
