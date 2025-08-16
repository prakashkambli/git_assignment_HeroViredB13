import math

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
 Temporary merge branch 1
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

    def square_root(self, x):
        if x < 0:
            raise ValueError("Cannot take square root of a negative number.")
        return math.sqrt(x)

if __name__ == "__main__":
    calculator = Calculator()

    num1 = 16
    num2 = 4
=========
        if b == 0:
            return "Error: Division by zero"
        return a / b


# ----------------- Test -----------------
if __name__ == "__main__":
    calculator = Calculator()

    num1, num2 = 16, 4
>>>>>>>>> Temporary merge branch 2

    print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
    print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}")
    print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
    print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")
<<<<<<<<< Temporary merge branch 1

    num3 = 25
    print(f"The square root of {num3} = {calculator.square_root(num3)}")
=========
>>>>>>>>> Temporary merge branch 2
