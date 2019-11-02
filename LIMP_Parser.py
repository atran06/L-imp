'''
File Description: Parser that uses a list of tokens and their types to construct parse trees.
                  Parser Specification: expression -> term {+ term}
                                        term -> factor {- factor}
                                        factor -> piece {/ piece}
                                        piece -> element {* element}
                                        element -> (expresssion) | NUMBER | IDENTIFIER
                  Instructions on how to use the program are contained in 'instructions.txt'.
'''

from tree import Tree

def parseNumber(tokensAndTypes):
    if tokensAndTypes[0][1] != "NUMBER": 
        raise Exception("parseNumber Error")

    token = tokensAndTypes[0]
    tokensAndTypes.pop(0) # removes the current token from the list of tokens

    return Tree(token[0], token[1], None, None)

def parseIdentifier(tokensAndTypes):
    if tokensAndTypes[0][1] != "IDENTIFIER": 
        raise Exception("parseIdentifier Error")

    token = tokensAndTypes[0]
    tokensAndTypes.pop(0) # removes the current token from the list of tokens

    return Tree(token[0], token[1], None, None)

def parseElement(tokensAndTypes):
    tree = None

    if tokensAndTypes[0][0] == "(":
        tokensAndTypes.pop(0) # removes the current token from the list of tokens (used to ommit parenthesis from the tree)

        tree = parseExpression(tokensAndTypes)

        if tokensAndTypes[0][0] != ")": 
            raise Exception("parseElement Error")

        tokensAndTypes.pop(0) # removes the current token from the list of tokens (used to ommit parenthesis from the tree)

    elif tokensAndTypes[0][1] == "NUMBER": tree = parseNumber(tokensAndTypes)
    else: tree = parseIdentifier(tokensAndTypes)

    return tree

def parsePiece(tokensAndTypes):
    tree = parseElement(tokensAndTypes)

    while len(tokensAndTypes) > 0 and tokensAndTypes[0][0] == "*":
        tokensAndTypes.pop(0) # removes the current token from the list of tokens
        tree = Tree("*", "PUNCTUATION", tree, parseElement(tokensAndTypes)) # creates a new subtree with the punctuation as the root

    return tree

def parseFactor(tokensAndTypes):
    tree = parsePiece(tokensAndTypes)

    while len(tokensAndTypes) > 0 and tokensAndTypes[0][0] == "/":
        tokensAndTypes.pop(0) # removes the current token from the list of tokens
        tree = Tree("/", "PUNCTUATION", tree, parsePiece(tokensAndTypes)) # creates a new subtree with the punctuation as the root

    return tree

def parseTerm(tokensAndTypes):
    tree = parseFactor(tokensAndTypes)

    while len(tokensAndTypes) > 0 and tokensAndTypes[0][0] == "-":
        tokensAndTypes.pop(0) # removes the current token from the list of tokens
        tree = Tree("-", "PUNCTUATION", tree, parseFactor(tokensAndTypes)) # creates a new subtree with the punctuation as the root

    return tree

def parseExpression(tokensAndTypes):
    tree = parseTerm(tokensAndTypes)

    while len(tokensAndTypes) > 0 and tokensAndTypes[0][0] == "+":
        tokensAndTypes.pop(0) # removes the current token from the list of tokens
        tree = Tree("+", "PUNCTUATION", tree, parseTerm(tokensAndTypes)) # creates a new subtree with the punctuation as the root

    return tree

def parseTokens(tokensAndTypes):
    copyTokensAndTypes = tokensAndTypes[:] # creates a copy of tokensAndTypes to conserve the original list

    return parseExpression(copyTokensAndTypes) 