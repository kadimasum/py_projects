class Calculator:
    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def divide(self):
        return self.num1/self.num2

    def multiply(self):
        return self.num1 * self.num2

if __name__ == '__main__':
    calculator = Calculator(8, 2)
    print(f"Num1: {calculator.num1}", f"Num2: {calculator.num2}")
    print('Sum, ', str(calculator.add()))
    print('Subtraction, ', str(calculator.subtract()))
    print('Division, ', str(calculator.divide()))
    print('Multiplication, ', str(calculator.multiply()))
 

