class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        result = 0
        c=a
        d=b
        if c< 0:
            a = 0-a
        if d< 0:
            b = 0-b
        for i in range(b):
            result = self.add(result, a)
        if (c<0 and d>0) or (c>0 and d<0):
            result = 0-result
        return result

    def divide(self, a, b):
        result = 0
        c=a
        d=b
        if c< 0:
            a = 0-a
        if d< 0:
            b = 0-b
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        if (c<0 and d>0) or (c>0 and d<0):
            result = 0-result
        return result
    
    def modulo(self, a, b):

        while a >= b:
            a = a-b
        
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(-1, -2))
    print("Example: multiplication: ", calc.multiply(2, -3))
    print("Example: division: ", calc.divide(10, -8))
    print("Example: modulo: ", calc.modulo(1, 2))