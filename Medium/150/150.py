def evalRPN(self, tokens: list[str]) -> int:
        stack = [] 
        
        ops = {
            "+" : int.__add__,
            "-" : int.__sub__,
            "*" : int.__mul__,
            "/" : int.__truediv__
        }

        for i in tokens:
            if i.isalnum() or (len(i) > 1):
                stack.append(i)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(ops[i](num1, num2))

        return int(stack[0])