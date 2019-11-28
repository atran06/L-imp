def top3Evaluable(stack):
    return len(stack) > 2 and stack[len(stack) - 1][1] == "NUMBER" and stack[len(stack) - 2][1] == "NUMBER" and stack[len(stack) - 3][1] == "PUNCTUATION"

def evaluateEquation(equation):
    if equation[0][0] == "+": return int(equation[1][0]) + int(equation[2][0])
    elif equation[0][0] == "-": return int(equation[1][0]) - int(equation[2][0])
    elif equation[0][0] == "*": return int(equation[1][0]) * int(equation[2][0])
    elif equation[0][0] == "/": return int(equation[1][0]) / int(equation[2][0])
    else: return 0

def getStack(ast, stack):
    if ast != None: 
        stack.append((ast.data, ast.tokenType)) # adds the value of the current node into the stack

        getStack(ast.left, stack)
        getStack(ast.middle, stack)
        getStack(ast.right, stack)

def evaluateStack(stack):
    newStack = [stack[0]]
    stack.pop(0)

    while newStack[0][1] != "NUMBER":
        if top3Evaluable(newStack):
            evaluatedEquation = evaluateEquation(newStack[len(newStack) - 3 : len(newStack)])
            newStack = newStack[:len(newStack) - 3]
            newStack.append((evaluatedEquation, 'NUMBER'))

        if len(stack) > 0:
            newStack.append(stack[0])
            stack.pop(0)

    return newStack[0][0]

def evaluate(ast):
    stack = []

    getStack(ast, stack)
    return evaluateStack(stack)
