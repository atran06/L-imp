from tree import Tree

def parseNumber(tokensAndTypes):
    if tokensAndTypes[0][1] != "NUMBER": return

    token = tokensAndTypes[0]
    tokensAndTypes.pop(0)

    return Tree(token[0],token[1], None, None)

def parseExpression(tokensAndTypes):
    tree = parseNumber(tokensAndTypes)

    while len(tokensAndTypes) > 0 and tokensAndTypes[0][0] == "+":
        tokensAndTypes.pop(0)
        tree = Tree("+", "PUNCTUATION", tree, parseNumber(tokensAndTypes))

    return tree

def parseTokens(tokensAndTypes):
    copyTokensAndTypes = tokensAndTypes[:] # creates a copy of tokensAndTypes to conserve the original list

    return parseExpression(copyTokensAndTypes) 