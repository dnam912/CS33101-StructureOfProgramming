"""
parser.py -- implement parser for simple expressions
Accept a string of tokens, return an AST expressed as stack of dictionaries.
"""

"""
    simple_expression = number | "(" expression ")" | "-" simeple_expression
    factor = simple_expression
    term = factor { "*"|"/" factor }
    expression = term { "+"|"-" term }
"""


from tokenizer import tokenize

def parse_simple_expression(tokens):

    """
    simple_expression = number | "(" expression ")" | "-" simple_expression
    """
    if tokens["tag"] == "number":
        return tokens[0], tokens[1:]
    

def test_parse_simple_expression():

    """
    simple_expression = number | "(" expression ")" | "-" simple_expression
    """

    print("testing parse_simple_expression")

    tokens = tokenize ("2")
    ast, tokens = parse_simple_expression(tokens)
    assert ast["tag"] == "number"
    assert ast["value"] == 2

if __name__ == "__main__":
    test_parse_simple_expression()
    print("done")

