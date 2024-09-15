def longestCommonPrefix(self, strs: list[str]) -> str:
    result = ""
    shortestWordLength = len(min(strs, key=lambda x: len(x)))

    i = 0
    while i < shortestWordLength:
        target = strs[0][i]

        for x in strs:
            if x[i] != target:
                return result
            
        result += target
        i += 1
    
    return result