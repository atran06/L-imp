'''
File Description: Parser that uses a list of tokens and their types to construct parse trees.
                  Parser Specification: statement -> basestatement {; basestatement}
                                        basestatement -> assignment | ifstatement | whilestatement | skip
                                        assignment -> IDENTIFIER := expression
                                        ifstatement -> if expression then statement else statement endif
                                        whilestatement -> while expression do statement endwhile

                                        expression -> term {+ term}
                                        term -> factor {- factor}
                                        factor -> piece {/ piece}
                                        piece -> element {* element}
                                        element -> (expresssion) | NUMBER | IDENTIFIER
                  Instructions on how to use the program are contained in 'instructions.txt'.
'''

from tree import Tree

def parseWhileStatement(tokensAndTypes):
    tree = parseExpression(tokensAndTypes)

    if tokensAndTypes[0][0] != "do": raise Exception("Missing 'do'")
    else:
        tokensAndTypes.pop(0)
        tree = Tree("WHILE-LOOP", "KEYWORD", tree, None, parseStatement(tokensAndTypes))

        if tokensAndTypes[0][0] != "endwhile": raise Exception("Missing 'endwhile'")
        tokensAndTypes.pop(0)

    return tree

def parseIfStatement(tokensAndTypes):
    tree = parseExpression(tokensAndTypes)

    if tokensAndTypes[0][0] != "then": raise Exception("Missing 'then'")
    else:
        tokensAndTypes.pop(0)
        statement1 = parseStatement(tokensAndTypes)

        if tokensAndTypes[0][0] != "else": raise Exception("Missing 'else'")
        else:
            tokensAndTypes.pop(0)
            tree = Tree("IF-STATEMENT", "KEYWORD", tree, statement1, parseStatement(tokensAndTypes))

    return tree

def parseAssignment(tokensAndTypes):
    tree = parseIdentifier(tokensAndTypes)

    if tokensAndTypes[0][0] == ":=":
        tokensAndTypes.pop(0)
        tree = Tree(":=", "PUNCTUATION", tree, None, parseExpression(tokensAndTypes))

    else:
        raise Exception("parseAssignment Error")

    return tree

def parseBaseStatement(tokensAndTypes):
    tree = None

    if len(tokensAndTypes) > 0:
        if tokensAndTypes[0][1] == "IDENTIFIER":
            tree = parseAssignment(tokensAndTypes)

        elif tokensAndTypes[0][0] == "if":
            tokensAndTypes.pop(0)
            tree = parseIfStatement(tokensAndTypes)

        elif tokensAndTypes[0][0] == "while":
            tokensAndTypes.pop(0)
            tree = parseWhileStatement(tokensAndTypes)

        elif tokensAndTypes[0][0] == "skip":
            tokensAndTypes.pop(0)
            tree = Tree("skip", "KEYWORD", None, None, None)  

    return tree

def parseStatement(tokensAndTypes):
    tree = parseBaseStatement(tokensAndTypes)

    while len(tokensAndTypes) > 0 and tokensAndTypes[0][0] == ";":
        tokensAndTypes.pop(0)
        tree = Tree(";", "PUNCTUATION", tree, None, parseBaseStatement(tokensAndTypes))
    
    return tree

def parseNumber(tokensAndTypes):
    if tokensAndTypes[0][1] != "NUMBER": 
        raise Exception("parseNumber Error")

    token = tokensAndTypes[0]
    tokensAndTypes.pop(0) # removes the current token from the list of tokens

    return Tree(token[0], token[1], None, None, None)

def parseIdentifier(tokensAndTypes):
    if tokensAndTypes[0][1] != "IDENTIFIER": 
        raise Exception("parseIdentifier Error")

    token = tokensAndTypes[0]
    tokensAndTypes.pop(0) # removes the current token from the list of tokens

    return Tree(token[0], token[1], None, None, None)

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
        tree = Tree("*", "PUNCTUATION", tree, None, parseElement(tokensAndTypes)) # creates a new subtree with the punctuation as the root

    return tree

def parseFactor(tokensAndTypes):
    tree = parsePiece(tokensAndTypes)

    while len(tokensAndTypes) > 0 and tokensAndTypes[0][0] == "/":
        tokensAndTypes.pop(0) # removes the current token from the list of tokens
        tree = Tree("/", "PUNCTUATION", tree, None, parsePiece(tokensAndTypes)) # creates a new subtree with the punctuation as the root

    return tree

def parseTerm(tokensAndTypes):
    tree = parseFactor(tokensAndTypes)

    while len(tokensAndTypes) > 0 and tokensAndTypes[0][0] == "-":
        tokensAndTypes.pop(0) # removes the current token from the list of tokens
        tree = Tree("-", "PUNCTUATION", tree, None, parseFactor(tokensAndTypes)) # creates a new subtree with the punctuation as the root

    return tree

def parseExpression(tokensAndTypes):
    tree = parseTerm(tokensAndTypes)

    while len(tokensAndTypes) > 0 and tokensAndTypes[0][0] == "+":
        tokensAndTypes.pop(0) # removes the current token from the list of tokens
        tree = Tree("+", "PUNCTUATION", tree, None, parseTerm(tokensAndTypes)) # creates a new subtree with the punctuation as the root

    return tree

def parseTokens(tokensAndTypes):
    copyTokensAndTypes = tokensAndTypes[:] # creates a copy of tokensAndTypes to conserve the original list

    return parseStatement(copyTokensAndTypes) 