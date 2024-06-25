from math import gcd

class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Denominator cannot be zero")
        self.a = a
        self.b = b
        self._reduce()

    def _reduce(self):
        common_divisor = gcd(self.a, self.b)
        self.a //= common_divisor
        self.b //= common_divisor
        if self.b < 0:  # Ensure the denominator is positive
            self.a = -self.a
            self.b = -self.b

    def __mul__(self, other):
        if isinstance(other, Fraction):
            new_a = self.a * other.a
            new_b = self.b * other.b
            return Fraction(new_a, new_b)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_a = self.a * other.b + other.a * self.b
            new_b = self.b * other.b
            return Fraction(new_a, new_b)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_a = self.a * other.b - other.a * self.b
            new_b = self.b * other.b
            return Fraction(new_a, new_b)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b == other.a * self.b
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b > other.a * self.b
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b < other.a * self.b
        return NotImplemented

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

    def to_improper_str(self):
        return f"Fraction: {self.a}, {self.b}"

# Testing the Fraction class
f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert f_c.to_improper_str() == 'Fraction: 7, 6', f_c.to_improper_str()
f_d = f_b * f_a
assert f_d.to_improper_str() == 'Fraction: 1, 3', f_d.to_improper_str()
f_e = f_a - f_b
assert f_e.to_improper_str() == 'Fraction: 1, 6', f_e.to_improper_str()

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True

print('OK')
