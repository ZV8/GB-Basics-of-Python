class MyComplex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        MyComplex.print(self)

    def print(self):
        plus_minus = '-' if self.imag < 0 else '+'
        print(f'({self.real}{plus_minus}{abs(self.imag) if abs(self.imag) != 1 else ""}j)')

    def __add__(self, other):
        return MyComplex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return MyComplex(self.real * other.real + self.imag * other.imag * -1,
                         self.real * other.imag + self.imag * other.real)


my_complex_1 = MyComplex(3, 1)
my_complex_2 = MyComplex(5, -2)

print('Сумма: ', end='')
sum_1 = my_complex_1 + my_complex_2

print('Произведение: ', end='')
mul_1 = my_complex_1 * my_complex_2
