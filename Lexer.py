import re, collections

class Lexer(object):

    WHITESPACE = r'(?P<WHITESPACE>\s+)'
    COMMENT = r'(?P<COMMENT>{[^}]*})'
    READ = r'(?P<READ>\bread\b)'
    WRITE = r'(?P<WRITE>\bwrite\b)'
    IF = r'(?P<IF>\bif\b)'
    THEN = r'(?P<THEN>\bthen\b)'
    ELSE = r'(?P<ELSE>\belse\b)'
    END = r'(?P<END>\bend\b)'
    REPEAT = r'(?P<REPEAT>\brepeat\b)'
    UNTIL = r'(?P<UNTIL>\buntil\b)'
    PLUS = r'(?P<PLUS>\+)'
    MINUS = r'(?P<MINUS>\-)'
    MULTIPLICATION = r'(?P<MULTIPLICATION>\*)'
    DIVISION = r'(?P<DIVISION>\/)'
    GREATER = r'(?P<GREATER>\>)'
    LESS = r'(?P<LESS>\<)'
    ASSIGN = r'(?P<ASSIGN>:=)'
    LPAREN = r'(?P<LPAREN>\()'
    RPAREN = r'(?P<RPAREN>\))'
    IDENTIFIER = r'(?P<IDENTIFIER>[a-z]+)'
    INTEGER = r'(?P<NUMBER>\d+)'
    SEMICOLON = r'(?P<SEMICOLON>;)'

    regex = re.compile('|'.join([
        WHITESPACE,
        COMMENT,
        READ,
        WRITE,
        IF,
        THEN,
        ELSE,
        END,
        REPEAT,
        UNTIL,
        PLUS,
        MINUS,
        MULTIPLICATION,
        DIVISION,
        GREATER,
        LESS,
        ASSIGN,
        LPAREN,
        RPAREN,
        IDENTIFIER,
        INTEGER,
        SEMICOLON
        ]))

    def __init__ (self, TINY):

        def generate_tokens(text):
            Token = collections.namedtuple('Token', ['type','value'])
            scanner = Lexer.regex.finditer(text)
            last_end = 0
            for m in scanner:
                start = m.start()
                end = m.end()
                if start != last_end:
                    # skipped over text to find the next token implies that there was unrecognizable text or an "error token"
                    text = self.text[last_end:start]
                    token = Token('ERROR', text)
                    yield token
                last_end = end
                token = Token(m.lastgroup, m.group())
                if token.type != 'WHITESPACE' and token.type != 'COMMENT':
                    yield token
            yield Token('EOF', '<end-of-file>')



        self._token_generator = generate_tokens(TINY)

    def next_token(self):
        # if you call this past the "EOF" token you will get a StopIteration exception
        return self._token_generator.__next__()


# lexer = Lexer('input.txt')
# while True:
#     token = lexer.next_token()
#     print(token.value, ", ", token.type)
#     if token.type == 'EOF':
#         break