from __future__ import division
import math


class Rational:
    def __init__(self, numer, denom):
        gcd = math.gcd(numer, denom)
        self.num = int(numer / gcd)
        self.den = int(denom / gcd)

        if self.den < 0:
            self.num = -self.num
            self.den = -self.den


    def __eq__(self, other):
        return self.num == other.num and self.den == other.den

    def __repr__(self):
        return '{}/{}'.format(self.num, self.den)

    def __add__(self, other):
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        return Rational(num, den)

    def __sub__(self, other):
        num = self.num * other.den - self.den * other.num
        den = self.den * other.den
        return Rational(num, den)

    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        return Rational(num, den)

    def __truediv__(self, other):
        num = self.num * other.den
        den = self.den * other.num
        return Rational(num, den)

    def __abs__(self):
        num = abs(self.num)
        den = abs(self.den)
        return Rational(num, den)

    def __pow__(self, power):
        if power >= 0:
            num = self.num ** power
            den = self.den ** power
            return Rational(num, den)
        else:
            num = self.den ** power
            den = self.num ** power
            return Rational(num, den)

    def __rpow__(self, base):
        return base ** (self.num / self.den)
