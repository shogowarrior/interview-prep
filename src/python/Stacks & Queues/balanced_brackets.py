
def are_brackets_balanced(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack.pop() != bracket_map[char]:
                return False
    return not stack

if __name__ == "__main__":
    print(are_brackets_balanced("[()]}"))
    print(are_brackets_balanced("[()]"))

