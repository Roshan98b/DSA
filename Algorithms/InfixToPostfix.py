def InfixToPostfix(infix):
    stack = []
    postfix = ''
    for c in infix:
        if (c in ['+','-','*','/','(',')']):
            if (c == '('):
                stack.append('(')
            elif (c == ')'):
                while (stack[-1] != '('):
                    postfix += stack.pop()
                stack.pop()
            elif (c in ['*','/']):
                stack.append(c)
            elif (c in ['+', '-']):
                if (len(stack)):
                    while (stack[-1] in ['+','-','*','/']):
                        postfix += stack.pop()
                        stack.append(c)
                        break
                    if (stack[-1] == '('):
                        stack.append(c)
                else:
                    stack.append(c)
        else:
            postfix += c
    for i in range(len(stack)):
        postfix += stack.pop()
    return postfix

infix1 = "a*b-c/(d+e)"
infix2 = "a+(b-c)*d"

print (InfixToPostfix(infix1))
print (InfixToPostfix(infix2))

