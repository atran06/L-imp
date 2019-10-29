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
        preOrderTraversal(root.right, indent)

    return 

def main():
    # opens the input file specified when running script from terminal
    inputFile = open(sys.argv[1]) # can change this line to inputFile = open("FILENAME", "r")

    tokensAndTypes = lexer.getTokensAndType(inputFile) # list of all tokens and types in the input file

    parseTree = parser.parseTokens(tokensAndTypes) # generated parse tree using the list of tokens

    preOrderTraversal(parseTree, 0) # uses preorder traversal to print the tree

if __name__ == "__main__":
    main()