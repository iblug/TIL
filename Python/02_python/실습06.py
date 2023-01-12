class Calculator:
    def __init__(self, number1:int, number2:int):
        self.number1 = number1
        self.number2 = number2

    def plus(self):
        return self.number1 + self.number2
    
    def minus(self):
        return self.number1 - self.number2

    def multiply(self):
        return self.number1 * self.number2
    
    def division(self):
        return self.number1 // self.number2
    
    def print(self):
        result = f'''number1 = {self.number1}, number2 = {self.number2}
합 : {self.plus()}
빼기 : {self.minus()}
곱 : {self.multiply()}
몫 : {self.division()}'''
        print(result)

calculator = Calculator(10, 5)
calculator.print()

calculator.number1 = -2
calculator.number2 = 2
calculator.print()