# Rotate letters and digits by rotationFactor positions
# Letters wrap around alphabet, digits wrap around 0-9

def rotationalCipher(s, k):
    result = []
    for c in s:
        if c.isalpha():
            # Rotate letters: a-z and A-Z
            base = ord('a') if c.islower() else ord('A')
            result.append(chr((ord(c) - base + k) % 26 + base))
        elif c.isdigit():
            # Rotate digits: 0-9
            result.append(chr((ord(c) - ord('0') + k) % 10 + ord('0')))
        else:
            # Keep non-alphanumeric characters unchanged
            result.append(c)
    return ''.join(result)

# Test cases
print(rotationalCipher("Zebra-493", 3))  # Cheud-726
print(rotationalCipher("abcdefghijklmNOPQRSTUVWXYZ0123456789", 39))  # nopqrstuvwxyzABCDEFGHIJKLM9012345678

