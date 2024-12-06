class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def square(self, a):
        return a * a

    def modulus(self, a, b):
        if b == 0:
            raise ValueError("Cannot take modulus by zero")
        return a % b
