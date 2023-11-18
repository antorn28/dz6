import random


class Encoder:
    def __init__(self, value):
        self.value = value
        self._encode()

    def _encode(self):
        operation = random.choice(['+', '-', '*', '/'])
        operand = random.randint(1, 10)

        if operation == '+':
            self.value += operand
        elif operation == '-':
            self.value -= operand
        elif operation == '*':
            self.value *= operand
        elif operation == '/':
            if operand != 0:
                self.value /= operand

    def __repr__(self):
        return f"Encoded Value: {self.value}"


num = 10
encoder_obj = Encoder(num)

print(encoder_obj)