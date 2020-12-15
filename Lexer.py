import re, collections

class Lexer(object):

    WHITESPACE = r'(?P<WHITESPACE>\s+)'
    COMMENT = r'(?P<Comment>{[^}]*})'
    READ = r'(?P<READ>\bread\b)'
    WRITE = r'(?P<WRITE>\bwrite\b)'
    IF = r'(?P<IF>\bif\b)'
    THEN = r'(?P<THEN>\bthen\b)'
    ELSE = r'(?P<ELSE>\belse\b)'
    END = r'(?P<END>\bend\b)'
    REPEAT = r'(?P<REPEAT>\brepeat\b)'
    UNTIL = r'(?P<UNTIL>\buntil\b)'
    OPERATOR = r'(?P<OPERATOR>(?:[+*/<>-]|:=))'
    IDENTIFIER = r'(?P<Identifier>[a-z]+)'
    NUMBER = r'(?P<Number>\d+)'
    SEMICOLON = r'(?P<Semicolon>;)'

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
        OPERATOR,
        IDENTIFIER,
        NUMBER,
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
                    text = text[last_end:start]
                    token = Token('Error', text)
                    yield token
                last_end = end
                token = Token(m.lastgroup, m.group())
                if token.type != 'WHITESPACE':
                    if token.type == "READ" or token.type == "WRITE" or token.type == "IF" or token.type == "THEN" or token.type == "ELSE" or token.type == "END" or token.type == "REPEAT" or token.type == "UNTIL":
                        token = Token('Reserved Word', token.value)
                    elif token.type == "OPERATOR":
                        token = Token('Special Symbol', token.value)
                    yield token
            yield Token('EOF', '<end-of-file>')



        self._token_generator = generate_tokens(TINY)

    def next_token(self):
        # if you call this past the "EOF" token you will get a StopIteration exception
        return self._token_generator.__next__()
