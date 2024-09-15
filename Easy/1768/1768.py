def mergeAlternately(self, word1: str, word2: str) -> str:
    len1 = len(word1)
    len2 = len(word2)
    result = ""
    i = 0
    j = 0

    while i < len1 and j < len2:
        result += word1[i]
        result += word2[j]

        i += 1
        j += 1

    if i < len1:
        result += word1[i:]
    elif j < len2:
        result += word2[j:]

    return result