def romanToInt(self, s: str) -> int:
    roman_to_integer = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
    }
    
    prev, current, total = 0, 0, 0

    i = len(s) - 1
    while i != -1:
        current = roman_to_integer[s[i]]
        if current < prev:
            total -= current
        else:
            total += current
        
        prev = current
        i -= 1

    return total