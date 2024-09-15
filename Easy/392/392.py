def isSubsequence(self, s: str, t: str) -> bool:
    
    if len(s) == 0:
        return False

    length = len(t)
    index = 0 # Used to store index of string s

    i = 0
    while i < length:
        if t[i] == s[index]:
            index += 1
        
        i += 1

    return len(s) == index