import sys
import lexer

def main():
    # opens the input file specified when running script from terminal
    inputFile = open(sys.argv[1]) # can change this line to inputFile = open("FILENAME", "r")

    tokensAndTypes = lexer.getTokensAndType(inputFile)

if __name__ == "__main__":
    main()