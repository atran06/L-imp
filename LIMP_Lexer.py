'''
File Description: Basic lexer/scanner that scans for PUNCTUATION, IDENTIFIERs, and NUMBERs.
                  RegEx:    IDENIFIER = ([a-z] | [A-Z])([a-z] | [A-Z] | [0-9])*
                            NUMBER = [0-9]+
                            PUNCTUATION = \+ | \- | \* | / | \( | \) | \; | \: | \=
                            KEYWORD = if|then|else|endif|while|do|endwhile|skip
                  Instructions on how to use the program are contained in 'instructions.txt'.
'''

import sys
import re

keywords = ["if", "then", "else", "endif", "while", "do", "endwhile", "skip"]

# Function: scan
# Description: Takes in a line, scans it for tokens, and returns a list of said tokens
# Parameters: line - a line of text containing various tokens
# Returns: a list of tokens
def scan(line):
    basicTokens = [] # holds the first pass of the scan
    tokens = [] # contains the final list of tokens

    # extracting basic tokens between whitespace and punctuation
    token = ""
    for i, char in enumerate(line): # goes through each character in the string and adds the char into the variable 'token' until one of the conditions are met
        if char == " ":
            if token != "": 
                basicTokens.append(token) # appends the substring from last append to whitespace
                token = "" 

        elif re.search("\+|\-|\*|/|\(|\)|\;|\:|\=", char): # uses regular expressions to check for punctuation
            if char == ":":
                if token != "":
                    basicTokens.append(token)
                    token = ""
                token += char

            elif char == "=":
                token += char
                basicTokens.append(token)
                token = ""

            else:
                if token != "":
                    basicTokens.append(token)
                    token = ""

                basicTokens.append(char)

        else: token += char

    if token != "": basicTokens.append(token) # adds the last token into the list

    # second pass to check for tokens that are starting with numbers 
    for string in basicTokens:
        # checking if token/identifier begins with a digit and whether or not the entire token is already a digit
        # also checks if the length is 1 which means that it's impossible for the string to contain more than 1 token
        if string[0].isdigit() and len(string) > 1 and not string.isdigit(): 
            newToken = ""
            for x, ch in enumerate(string): # current index is held in 'x' and the char at the index is held in 'ch'
                if not ch.isdigit(): break # breaks out of the loop once a non-digit is reached
                else: newToken += ch

            # adds the divided token into the final token list
            tokens.append(newToken)
            tokens.append(string[x:])

        else:
            tokens.append(string) # adds unchanged token into final token list

    return tokens

# Function: identifyTokens
# Description: Given a tokens, this function identifies the type of token between 'IDENTIFIER',
#              'NUMBER','PUNCTUATION' and 'ERROR'
# Parameters: token - token to be identified
# Returns: the token type coresponding to the given token
def identifyTokens(token):
    if re.search("\+|\-|\*|/|\(|\)|\;|\:|\=", token): return "PUNCTUATION"
    elif token in keywords: return "KEYWORD"
    elif token[0].isdigit(): return "NUMBER"
    elif token[0].isalpha(): return "IDENTIFIER"
    else: return "ERROR"

def getTokensAndType(line):
    tokensAndType = [] # holds a list of pairs of (TOKEN, TOKENTYPE)

    tokens = scan(line.strip())

    for token in tokens:
        tokenName = identifyTokens(token) # holds the type of token

        tokensAndType.append((token, tokenName)) # adds the pair to list
            
    return tokensAndType
