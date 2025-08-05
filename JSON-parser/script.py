#!/usr/bin/env python3

import sys
import re

class Token:
    def __init__(self):
        self.val = ""
        self.valType = ""

    def setVals(self, val1, val2):
        self.val = val1
        self.valType = val2

val = sys.stdin.read()

def tokenizer(input):
    tokensArr = []
    currentIdx = 0

    if (input[0] != '{' or input[-2] != "}") and (input[0] != '[' or input[-2] != ']'):
        raise Exception(f"Must be object or array {input[0]}, {input[-2]}")

    while currentIdx < len(input):
        token =  Token()
        letter = input[currentIdx]
        
        if re.match(r'\s', letter):
            currentIdx += 1
            continue
        elif letter == "{":
            token.setVals("{", "BraceOpen")
        elif letter == "}":
            token.setVals("}", "BraceClose")
        elif letter == "[":
            token.setVals("[", "BracketOpen")
        elif letter == "]":
            token.setVals("]", "BracketClose")
        elif letter == ":":
            token.setVals(":", "Colon")
        elif letter == '"':
            value = ""
            currentIdx += 1
            char = input[currentIdx]
            while(char != '"'):
                value += char
                currentIdx += 1 
                char = input[currentIdx]
            token.setVals(value, "String")
        elif letter == ',':
            token.setVals(',', "Comma")
        elif letter == "t":
            value = ""
            for i in range(4):
                value += letter
                currentIdx += 1 
                letter  = input[currentIdx]
            if value == "true":
                token.setVals(True, 'Boolean')
            else:
                raise Exception(f"Invalid Value: f{value}")
        elif letter == "f":
            value = ""
            for i in range(5):
                value += letter
                currentIdx += 1 
                letter = input[currentIdx]
            if value == "false":
                token.setVals(False, "Boolean")
            else:
                raise Exception(f"Invalid Value: f{value}")
        elif letter == 'n':
            value = ""
            for i in range(4):
                value += letter
                currentIdx += 1 
                letter = input[currentIdx]
            if value == "null":
                token.setVals(None, "Null")
            else:
                raise Exception(f"Invalid Value: f{value}")
        elif re.match(r'\d', letter):
            value = ""
            while re.match(r'\d', letter):
                value += letter
                currentIdx += 1 
                letter = input[currentIdx]
            token.setVals(int(value), "Number")
        else:   
            raise Exception(letter, "Letter not valid")

        currentIdx += 1

        tokensArr.append(token)
    return tokensArr

def parser(tokensArr):
    if not tokensArr:
        raise Exception("Nothing to parse")
    
    current = 0

    def parseArray():
        nonlocal current
        node = []
        current += 1 
        token = tokensArr[current]
        
        while token.valType != "BracketClose":
            if token != ",":
                node.append(parseValue())
                current += 1 
                token = tokensArr[current]
                continue
            current += 1 
            token = tokensArr[current]

        return node


    def parseValue():
        nonlocal current
        token = tokensArr[current]

        match token.valType:
            case "BraceOpen":
                return parseObj()
            case "String":
                return token.val
            case "Number":
                return token.val 
            case "Boolean":
                return token.val
            case "Null":
                return None
            case "BracketOpen":
                return parseArray()
            case _:
                raise Exception(f"Unexpected token type: {token.valType}")
    
    def parseObj():
        nonlocal current 
        node = {"type" : "Object", "val" : {}}
        current += 1
        token = tokensArr[current]

        while token.valType != "BraceClose":
            if(token.valType == "String"):
                key = token.val
                current += 1 
                token = tokensArr[current]
                if(token.valType != "Colon"):
                    raise Exception("Expected : in key-value pair")
                current += 1 
                token = tokensArr[current]
                value = parseValue()
                node["val"][key] = value
            elif token.valType == "Comma":
                current += 1 
                token = tokensArr[current]
                if current < len(tokensArr) and token.valType == "String":
                    continue
                else:
                    raise Exception("Expected key-value pair after comma")
            else:
                raise Exception(f"Expected String key in object. Token type: {token.valType}")

            current += 1
            token = tokensArr[current]
        return node
    
    AST = parseValue()

    return AST


print(parser(tokenizer(val)))
