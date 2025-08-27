def encrypted_words(S):
    s_len = len(S)
    if s_len <= 1:
        return S
    mid = (s_len - 1) // 2
    return S[mid] + encrypted_words(S[0:mid]) + encrypted_words(S[mid+1:])

S = "abc"
R = "bac"
print(encrypted_words(S))

S = "abcd"
R = "bacd"
print(encrypted_words(S))

S = "abcxcba"
R = "xbacbca"
print(encrypted_words(S))

S = "facebook"
R = "eafcobok"
print(encrypted_words(S))
