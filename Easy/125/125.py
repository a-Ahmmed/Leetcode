def isPalindrome(self, s: str) -> bool:
    left, right = 0, 0  # Pointers
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '

    # Sanitize Input Str
    string = s.lower()

    for x in punctuation:
        string = string.replace(x, "")

    right = len(string) - 1 # Sanitized length

    # Check for palindrome
    while left < right:
        if string[left] != string[right]:
            return False
        
        left += 1
        right -= 1

    return True