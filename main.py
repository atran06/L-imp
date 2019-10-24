import sys
import lexer

def main():
    # lexer.main()
    # opens the input file specified when running script from terminal
    inputFile = open(sys.argv[1]) # can change this line to inputFile = open("FILENAME", "r")

    for line in inputFile:
        print("Line: %s" % line.strip())

        tokens = lexer.scan(line.strip())
        for token in tokens:
            tokenName = lexer.identifyTokens(token) # holds the type of token
            if tokenName == "ERROR": 
                print("ERROR READING: \"" + token + "\"")
                break
            else: print(token + " : " + tokenName)

        print("")

if __name__ == "__main__":
    main()