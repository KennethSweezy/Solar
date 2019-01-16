# The Solar Programming Language
# https://github.com/Solar-language/Solar

# Licensed under the MIT Licence.
# See https://github.com/Solar-language/Solar/blob/master/LICENSE.md

from error import SolarError

class Interpreter:
    def __init__(self):
        self.environment = {
            "+": lambda args: self.stdAdd(args),
            "-": lambda args: self.stdSubtract(args),
            "*": lambda args: self.stdMultiply(args),
            "/": lambda args: self.stdDivide(args),
            "%": lambda args: self.stdModulo(args),
            "list": lambda args: self.stdList(args),
            "int": lambda args: self.stdInt(args),
            "float": lambda args: self.stdFloat(args),
            "str": lambda args: self.stdStr(args),
            "put": lambda args: self.stdPut(args),
            "print": lambda args: self.stdPrint(args),
            "get": lambda args: self.stdGet(args),
            "=": lambda args: self.stdEquals(args),
            ">": lambda args: self.stdGreater(args),
            "<": lambda args: self.stdLess(args),
            ">=": lambda args: self.stdGreaterOrEquals(args),
            "<=": lambda args: self.stdLessOrEquals(args),
            "lower": lambda args: self.stdLower(args),
            "upper": lambda args: self.stdUpper(args),
            "encode": lambda args: self.stdEncode(args),
            "decode": lambda args: self.stdDecode(args),
            "def": lambda args: self.stdDef(args),
            "set": lambda args: self.stdSet(args),
            "raise": lambda args: self.stdRaise(args),
        }


    def getVariable(self, expression):
        name = expression["value"]

        try:
            return self.environment[name]
        except KeyError:
            raise SolarError(f"Runtime error: Undefined variable {name}.")

                        
    def call(self, expression):
        functionName = expression["name"]
        
        try:
            function = self.environment[functionName]
        except KeyError:
            raise SolarError(f"Runtime error: Undefined function '{functionName}'.")

        return function(expression["params"])

                        
    def evaluate(self, expression):
        typ = expression["type"]

        if (typ == "NumberLiteral" or
                typ == "StringLiteral" or
                typ == "BoolLiteral" or
                typ == "NullLiteral"):
            return expression["value"]
        
        elif typ == "VariableExpression":
            return self.getVariable(expression)
        
        elif typ == "CallExpression":
            return self.call(expression)

    def interpret(self, program):
        for expression in program["body"]:
            self.evaluate(expression)

                        
    # --- Functions in environment --- #

    # Name: 'def'
    def stdDef(self, args):
        # May either have 1 or 2 args
        if len(args) > 2:
            raise SolarError(f"Function 'def' expected 1 or 2 args, but got {len(args)}.")
            
        name = args[0]

        if name["type"] != "VariableExpression":
            raise SolarError("Can only assign to variable names.")
            
        value = self.evaluate(args[1]) if len(args) == 2 else None
        
        if name["value"] in self.environment.keys():
            raise SolarError(f"Cannot redeclare the already declared variable '{name['value']}'. Try using 'set' instead.")
        
        self.environment[name["value"]] = value
        
    
    # Name: 'set'
    def stdSet(self, args):
        assertArgsLength(args, 2, "set")

        name = args[0]

        if name["type"] != "VariableExpression":
            raise SolarError("Can only assign to variable names.")

        if name["value"] in self.environment.keys():
            self.environment[name["value"]] = self.evaluate(args[1])
        else:                    
            raise SolarError(f"Cannot set the undeclared variable '{name['value']}'. Try using 'def' instead.")


    # Name: '+'
    def stdAdd(self, args):
        assertArgsLength(args, 2, "+")
        return self.evaluate(args[0]) + self.evaluate(args[1])

  
    # Name: '-'
    def stdSubtract(self, args):
        assertArgsLength(args, 2, "-")
        return self.evaluate(args[0]) - self.evaluate(args[1])

  
    # Name: '*'
    def stdMultiply(self, args):
        assertArgsLength(args, 2, "*")
        return self.evaluate(args[0]) * self.evaluate(args[1])

  
    # Name: '/'
    def stdDivide(self, args):
        assertArgsLength(args, 2, "/")
        return self.evaluate(args[0]) / self.evaluate(args[1])

  
    # Name: '%'
    def stdModulo(self, args):
        assertArgsLength(args, 2, "%")
        return self.evaluate(args[0]) % self.evaluate(args[1])

                             
    # Name: 'list'
    def stdList(self, args):
        return [self.evaluate(arg) for arg in args]
                             
                        
    # Name: 'int'
    def stdInt(self, args):
        assertArgsLength(args, 1, "int")
        return int(self.evaluate(args[0]))

                        
    # Name: 'float'
    def stdFloat(self, args):
        assertArgsLength(args, 1, "float")
        return float(self.evaluate(args[0]))

                        
    # Name: 'str'
    def stdStr(self, args):
        assertArgsLength(args, 1, "str")
        return str(self.evaluate(args[0]))

  
    # Name: 'put'
    def stdPut(self, args):
        assertArgsLength(args, 1, "put")
        val = self.evaluate(args[0])
        print(val)
        return val
                             
                             
    # Name: 'print'
    def stdPrint(self, args):
        assertArgsLength(args, 1, "print")
        val = self.evaluate(args[0])
        print(val, "")
        return val             
    
    
    # Name: 'get'
    def stdGet(self, args):
        # May either have 0 or 1 args
        if len(args) > 1:
            raise SolarError(f"Function 'get' expected 0 or 1 args, but got {len(args)}.")
        return input(self.evaluate(args[0])) if len(args) == 1 else input()

    
    # Name: '='
    def stdEquals(self, args):
        assertArgsLength(args, 2, "=")
        return self.evaluate(args[0]) == self.evaluate(args[1])

    
    # Name: '>'
    def stdGreater(self, args):
        assertArgsLength(args, 2, ">")
        return self.evaluate(args[0]) > self.evaluate(args[1])

    
    # Name: '<'
    def stdLess(self, args):
        assertArgsLength(args, 2, "<")
        return self.evaluate(args[0]) < self.evaluate(args[1])


    # Name: '>='
    def stdGreaterOrEquals(self, args):
        assertArgsLength(args, 2, ">=")
        return self.evaluate(args[0]) >= self.evaluate(args[1])


    # Name: '<='
    def stdLessOrEquals(self, args):
        assertArgsLength(args, 2, "<=")
        return self.evaluate(args[0]) <= self.evaluate(args[1])
    

    # Name: 'lower'
    def stdLower(self, args):
        assertArgsLength(args, 1, "lower")
        return self.evaluate(args[0]).lower()

    
    # Name: 'upper'
    def stdUpper(self, args):
        assertArgsLength(args, 1, "upper")
        return self.evaluate(args[0]).upper()

    
    # Name: 'encode'
    def stdEncode(self, args):
        assertArgsLength(args, 1, "encode")
        arg = self.evaluate(args[0])
        if type(arg) is list:
            return [chr(item) for item in arg]
        else:
            return chr(self.evaluate(args[0]))
                             
                             
    # Name: 'decode'
    def stdDecode(self, args):
        assertArgsLength(args, 1, "decode")
        li = []
        for i in self.evaluate(args[0]):
            li.append(ord(i))
        return li
          
        
    # Name: 'raise'
    def stdRaise(self, args):
        assertArgsLength(args, 1, "raise")
        raise SolarError(f"Error raised: {self.evaluate(args[0])}")
  
# --- End functions in environment --- #

def assertArgsLength(args, expectedLength, functionName):
    if len(args) != expectedLength:
        raise SolarError(f"Function '{functionName}' expected {expectedLength} args, but got {len(args)}.")