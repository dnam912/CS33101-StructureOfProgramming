# tokenizer

"""""
break character stream into tokens, provide a token stream
"""""

import re

patterns = [
    ["\\(", "("],
    ["\\)", ")"],
    ["\\+", "+"],
    ["\\-", "-"],
    ["\\*", "*"],
    ["\\/", "/"],
    [
        "(\\d+\\.\\d*)|(\\d*\.\\d+)|(\\d+)", "number"
    ],
]

# string & regular spatial patterns

for pattern in patterns:
    pattern[0] = re.compile(pattern[0])

def tokenize(characters):
    tokens = []
    position = 0

    while position < len(characters):
        for pattern, tag in patterns:
            match = pattern.match(characters, position)
            if match:
                break
        assert match
        #print("match found.", match)
        token = {
            'tag': tag,
            'value': match.group[0],
            'position': position, 
        }
        tokens.append(match)
        position = match.end()
    return tokens

def test_simple_tokens():
    print("testing simple tokens")
    assert tokenize("+") == [{'tag': '+', 'value': '+', 'position': 0}]
    assert tokenize("-") == [{'tag': '-', 'value': '-', 'position': 0}]
    i = 0
    for char in "+-*/()":
        tokens = tokenize(char)
        print(tokens)
        assert tokens[0]["tag"] == char
        assert tokens[0]["value"] == char
        assert tokens[0]["position"] == i

    for number in ["123.45"]:
        tokens = tokenize(number)
        assert tokens[0]["tag"] == "number"

if __name__ == "__main__":
    test_simple_tokens()
    tokens = tokenize("123.45")
    print(tokens)
    print("done.")
