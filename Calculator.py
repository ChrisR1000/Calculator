
class Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
        
    def add(self, number1, number2):
        result = number1 + number2
        print(result)

    def subtract(self, number1, number2):
        result = number1 - number2
        print(result)

    def divide(self, number1, number2):
        result = number1 / number2
        print(result)

    
    
    

# test change


calculator = Calculator(3, 2)
calculator.add(3, 2)


calculator.divide(3, 2)