def isValid(self, s: str) -> bool:
    stack = []
    closingBrackets = [')', ']', '}']

    for bracket in s:
        stack.append(bracket)

        if bracket in closingBrackets and len(stack) > 1:
            closing = stack.pop()
            opening = stack.pop()

            if not ( (opening == "(" and closing == ")") or (opening == "{" and closing == "}") or (opening == "[" and closing == "]") ):
                stack.append(opening)
                stack.append(closing)


    if len(stack) == 0:
        return True
    else:
        return False