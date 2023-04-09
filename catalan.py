import sys

# Catalan class is made to represent and compute the nth Catalan Number
class Catalan:


    # accepts and initializes the argument for Catalan number
    def __init__(self, n):
        self.__n = n

    # takes in the argument n to calculate the nth catalan number recursively through using the catalan number formula
    def CatalanNumber(self, n):
        if self.__n < 0:
            return None
        elif self.__n <= 1:
            return 1
        c = 0
        for i in range(self.__n):
            c = c + self.CatalanNumber(i) * self.CatalanNumber(self.__n - i - 1)

        return c

# used for command prompt input and result output    
input =int(list(sys.argv)[1])
Number = Catalan(input)
print(Number.CatalanNumber(input))
