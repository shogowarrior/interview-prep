# Find shortest palindrome by adding characters in front

def shortest_palindrome(s: str) -> str:
    rev_s = s[::-1]
    concat = s + '#' + rev_s
    lps = [0] * len(concat)


    print("Concat:", concat)
    # Build KMP table (lps array)
    for i in range(1, len(concat)):
        # KMP algorithm to find the longest prefix which is also a suffix
        # lps[i] is the length of the longest prefix of concat[0:i] which is also a suffix
        j = lps[i - 1] # previous longest prefix length

        print("J", j)
    
        # Iterate through the string to fill lps array
        # If characters don't match, we backtrack using the lps array
        while j > 0 and concat[i] != concat[j]:
            j = lps[j - 1] # backtrack to the last known prefix length
            print(" while J", j)
        if concat[i] == concat[j]:
            print("Match found at", i, "with j =", j)
            j += 1
        lps[i] = j

    print(lps)
    # lps[-1] is the length of the longest prefix of s which is also a suffix of rev_s
    to_add = rev_s[:len(s) - lps[-1]]
    return to_add + s


# Test
test_cases = ["abcd", "aacecaaa", ""]
for s in test_cases:
    print(f"'{s}' -> '{shortest_palindrome(s)}'")