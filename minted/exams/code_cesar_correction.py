def code_cesar(message, k):
    lettre_vers_position = dico_cesar(k)
    m_k = ""
    for c in message:
        if c == ' ':
            m_k += ' '
        else:
            m_k += alphabet[lettre_vers_position[c]]
    return m_k

