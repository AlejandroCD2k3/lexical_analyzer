from Lexer import Lexer
from LexicalError import LexicalError

def main():
    code = """
    int a=5+2;
    """
    lexer = Lexer(code)
    
    try:
        tokens = lexer.tokenize()
        print("\nTokens found:")
        print("-------------------")
        for token in tokens:
            print(f"Type: {token[0]}, Lexeme: '{token[1]}', Position: {token[2]}")
    except LexicalError as lexical_error:
        print(lexical_error)

if __name__ == "__main__":
    main()