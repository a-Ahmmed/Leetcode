def simplifyPath(self, path: str) -> str:
    tokens = []

    i = 1
    while i < len(path):
        stack = []
        periodCount = 0

        while i < len(path) and path[i] != "/":
            if path[i] == '.':
                periodCount += 1
            
            stack.append(path[i])
            i += 1

        if periodCount == len(stack):
            match periodCount:
                case 1:
                    stack = []
                case 2:
                    stack = []
                    if len(tokens):
                        tokens.pop()
        
        if len(stack):
            tokens.append("".join(stack))
        i += 1

    return '/' + "/".join(tokens)