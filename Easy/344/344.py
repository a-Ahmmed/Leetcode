def reverseString(self, s: list[str]) -> None:
    i = 0
    length = len(s)

    while i < (length // 2):
        s[i], s[length - i - 1] = s[length - i - 1], s[i]
        i += 1