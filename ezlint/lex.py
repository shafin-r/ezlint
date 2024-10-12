class Lexer:
    def __init__(self, source):
        # Source code routed to lexer as a string. New line appended at the end to simply lexing tokens.
        self.source = source + "\n"
        self.curChar = ''  # Current character in the string
        self.curPos = -1  # Current position in the string
        self.nextChar()  # Function call to move to next character in the string

    # Process the next character.
    def nextChar(self):
        self.curPos += 1
        if self.curPos >= len(self.source):
            self.curChar = '\0'  # EOF (End Of File)
        else:
            self.curChar = self.source[self.curPos]

    # Return the lookahead character.
    def peek(self):
        if self.curPos + 1 >= len(self.source):
            return '\0'  # EOF (End Of File)
        return self.source[self.curPos+1]

    # Invalid token found, print error message and exit.
    def abort(self, message):
        pass

    # Skip whitespace except newlines, which we will use to indicate the end of a statement.
    def skipWhitespace(self):
        pass

    # Skip comments in the code.
    def skipComment(self):
        pass

    # Return the next token.
    def getToken(self):
        pass
