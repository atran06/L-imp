'''
Project Phase 1.1
Author: Arthur Tran
Class: Comp141 - Programming Lanuages

Instructions on how to use the program are contained in 'instructions.txt'.
'''

import sys
import LIMP_Lexer as lexer
import LIMP_Parser as parser

def preOrderTraversal(root, indent):
    if root != None:
        print("\t" * indent, end = "") # prints the indentation
        print(root.data, " : ", root.tokenType) # prints the current node

        indent += 1 # increments the indent by one for each sub tree

        preOrderTraversal(root.left, indent)
        preOrderTraversal(root.middle, indent)
        preOrderTraversal(root.right, indent)

    return 

def printTokensAndTypes(tokensAndTypes):
    for tokenAndType in tokensAndTypes:
        print(tokenAndType[0], " : ", tokenAndType[1])

def main():
    # opens the input file specified when running script from terminal
    inputFile = open(sys.argv[1]) # can change this line to inputFile = open("FILENAME", "r")
    lines = inputFile.readlines()

    tokensAndTypes = []

    for line in lines:
        if not line.strip() == "":
            # print("Line: ", line.strip(), "\n")

            tokensAndTypes.extend(lexer.getTokensAndType(line.strip()))

            # print("Tokens: ")
            # printTokensAndTypes(tokensAndTypes)
            # print("")

            # print("AST: ")
            # preOrderTraversal(parser.parseTokens(tokensAndTypes), 0)

            # print("\n\n")
    
    print("Tokens: ")
    printTokensAndTypes(tokensAndTypes)
    print("")

    print("AST: ")
    preOrderTraversal(parser.parseTokens(tokensAndTypes), 0)

if __name__ == "__main__":
    main()