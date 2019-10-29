'''
Parser Specification

expression -> term {+ term}
term -> factor {- factor}
factor -> piece {/ piece}
piece -> element {* element}
element -> (expresssion) | NUMBER | IDENTIFIER
'''

from tree import Tree

def parseNumber(tokensAndTypes):
    if tokensAndTypes[0][1] != "NUMBER": return

    token = tokensAndTypes[0]
    tokensAndTypes.pop(0)

    return Tree(token[0], token[1], None, None)

def parseIdentifier(tokensAndTypes):
    if tokensAndTypes[0][1] != "IDENTIFIER": return

    token = tokensAndTypes[0]
    tokensAndTypes.pop(0)

    return Tree(token[0], token[1], None, None)

def parseElement(tokensAndTypes):
    tree = None

    if tokensAndTypes[0][0] == "(":
        tokensAndTypes.pop(0)

        tree = parseExpression(tokensAndTypes)

        if tokensAndTypes[0][0] != ")": return
        tokensAndTypes.pop(0)

    elif tokensAndTypes[0][1] == "NUMBER": tree = parseNumber(tokensAndTypes)
    else: tree = parseIdentifier(tokensAndTypes)

    return tree

def parsePiece(tokensAndTypes):
    tree = parseElement(tokensAndTypes)

    while len(tokensAndTypes) > 0 and tokensAndTypes[0][0] == "*":
        tokensAndTypes.pop(0)
        tree = Tree("*", "PUNCTUATION", tree, parseElement(tokensAndTypes))

    return tree

def parseFactor(tokensAndTypes):
    tree = parsePiece(tokensAndTypes)

    while len(tokensAndTypes) > 0 and tokensAndTypes[0][0] == "/":
        tokensAndTypes.pop(0)
        tree = Tree("/", "PUNCTUATION", tree, parsePiece(tokensAndTypes))

    return tree

def parseTerm(tokensAndTypes):
    tree = parseFactor(tokensAndTypes)

    while len(tokensAndTypes) > 0 and tokensAndTypes[0][0] == "-":
        tokensAndTypes.pop(0)
        tree = Tree("-", "PUNCTUATION", tree, parseFactor(tokensAndTypes))

    return tree

def parseExpression(tokensAndTypes):
    tree = parseTerm(tokensAndTypes)

    while len(tokensAndTypes) > 0 and tokensAndTypes[0][0] == "+":
        tokensAndTypes.pop(0)
        tree = Tree("+", "PUNCTUATION", tree, parseTerm(tokensAndTypes))

    return tree

def parseTokens(tokensAndTypes):
    copyTokensAndTypes = tokensAndTypes[:] # creates a copy of tokensAndTypes to conserve the original list

    return parseExpression(copyTokensAndTypes) 