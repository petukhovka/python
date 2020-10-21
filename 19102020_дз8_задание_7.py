
class Complex:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        result = self.number + other.number
        return result

    def __mul__(self, other):
        result = self.number * other.number
        return result

c1 = Complex(2+2j)
c2 = Complex(3-4j)
print(c1+c2)
print(c1*c2)