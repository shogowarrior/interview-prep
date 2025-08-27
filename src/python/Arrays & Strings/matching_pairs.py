def matchingPairs(s, t):
    n = len(s)
    matches = 0
    mismatch_s = set()
    mismatch_t = set()
    mismatch_pairs = set()

    for i in range(n):
        if s[i] == t[i]:
            matches += 1
        else:
            mismatch_s.add(s[i])
            mismatch_t.add(t[i])
            mismatch_pairs.add((s[i], t[i]))

    # Check for perfect swap: mismatched (a, b) and (b, a)
    for a, b in mismatch_pairs:
        if (b, a) in mismatch_pairs:
            return matches + 2

    # Check for single improvement: one side overlap
    for a, b in mismatch_pairs:
        if a in mismatch_t or b in mismatch_s:
            return matches + 1

    # If s and t are already identical, swap will hurt
    if matches == n:
        return matches - 2

    return matches - 1


s = "abcd"
t = "adcb"
print(matchingPairs(s, t))  # Output: 4

s = "mno"
t = "mno"
print(matchingPairs(s, t))  # Output: 1


s = "abcde"
t = "abfde"
print(matchingPairs(s, t))  # Output: 3

