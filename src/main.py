# The Solar Programming Language
# https://github.com/Solar-language/Solar

# Licensed under the MIT Licence.
# See https://github.com/Solar-language/Solar/blob/master/LICENSE.md

import sys

from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

from error import SolarError

        
interpreter = Interpreter()


def run(inp):
    global interpreter

    tokens = Lexer().lex(inp)
    ast = Parser().parse(tokens)

    print("--START AST--")
    print(ast)
    print("--END AST--\n")

    interpreter.interpret(ast)

def getReplInput():
    inpu = str(input("solar > "))
    openParens = 0
        
    def walk(inp):
        nonlocal openParens
        for char in inp:
            if char == "(":
                openParens += 1
            elif char == ")":
                openParens -= 1
                
    walk(inpu)
                
    while openParens != 0:
        inp = str(" " + input("solar ^ "))
        inpu += inp
        walk(inp)
        
    return inpu
     
        
def runRepl():
    while True:
        inp = getReplInput()
        
        try:
            run(inp)
        except SolarError as error:
            print(error)
            print()
        except KeyboardInterrupt:
            print("\nQuitting...")
            sys.exit(1)
        except:
            print("Internal error, raising exception:")
            raise

                        
def runFile(filename):
    with open(filename, "r") as sourceFile:
        try:
            run(sourceFile.read())
        except SolarError as Error:
            print(Error)
            print()
            sys.exit(1)

                        
def main():
    if len(sys.argv) == 1:
        runRepl()
    elif len(sys.argv) == 2:
        runFile(sys.argv[1])
    else:
        raise RuntimeError("Usage: solar [filename]")

                        
main()
