from ezlint.lex import *


def main():
    source = "let foobar = 123"
    lexer = Lexer(source)

    while lexer.peek() != '\0':
        print(lexer.curChar)
        lexer.nextChar()


main()
