import sys
import lexer
import parserE

def preOrderTraversal(root, indent):
    if root != None:
        for i in range(indent):
            print("\t" * indent, end = "")
        print(root.data, " : ", root.tokenType)

        indent += 1

        preOrderTraversal(root.left, indent)
        preOrderTraversal(root.right, indent)

    return 

def main():
    # opens the input file specified when running script from terminal
    inputFile = open(sys.argv[1]) # can change this line to inputFile = open("FILENAME", "r")

    tokensAndTypes = lexer.getTokensAndType(inputFile) # list of all tokens and types in the input file

    parseTree = parserE.parseTokens(tokensAndTypes)

    preOrderTraversal(parseTree, 0)

if __name__ == "__main__":
    main()