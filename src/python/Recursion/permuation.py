# Design an algorithm that takes a string, for example, abc, and prints out all possible permutations of the string.



def string_permutations(s: str) -> set:
    if len(s) == 0:
        return {""}
    
    permutations = set()
    
    # Iterate through each character in the string
    # and fix it at the first position, then find permutations of the remaining characters
    for i, char in enumerate(s):
        # Get all permutations of the remaining characters
        for perm in string_permutations(s[:i] + s[i+1:]):
            permutations.add(char + perm)
    
    return permutations

print(string_permutations("abc"))  # Output: {'abc', 'acb', 'bac', 'bca', 'cab', 'cba'}
