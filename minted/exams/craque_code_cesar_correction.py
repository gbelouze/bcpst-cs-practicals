def craque_code_cesar(message_code):
    x = caractere_le_plus_frequent(message_code)
    k = devine_k(x)
    return decode_cesar(message_code, k)
