"""
class for working with vectors
autor: Alex Olivier Michaud
"""
from zlomky import Zlomek
from math import sqrt, atan2, degrees
class Vector:
    def __init__(self, x, y):
        """
        :param x: x coordinate: Zlomek
        :param y: y coordinate: Zlomek
        """
        self._x = x     #atributy instance
        self._y = y



    def phi(self):
        """
        return: degrees of the vector
        """
        a = atan2(self._x.citatel / self._x.jmenovatel, self._y.citatel / self._y.jmenovatel)
        return degrees(a)

    def minus_phi(self, other):
        """
        :param other: vector
        :return: degrees
        """
        return self.phi() - other.phi()

    def __repr__(self) -> str:
        return f"[{self._x},{self._y}]"

    def __str__(self) -> str:
        return f"[{self._x},{self._y}]"

    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y)

    def velikost(self):
        z1 = self._x * self._x + self._y * self._y
        return sqrt(z1.citatel) / sqrt(z1.jmenovatel)

    def __abs__(self):
        internal = self.velikost()
        return internal

    def __neg__(self):
        return Vector(Zlomek(-1) *self._x, Zlomek(-1) *self._y)

    def __eq__(self, other):
        return (self.velikost() == other.velikost)

    def __lt__(self, other):
        return (self.velikost() < other.velikost)

    def __gt__(self, other):
        return (self.velikost() > other.velikost)

    @classmethod
    def fromStr(self, retezec) ->None:
        x, y = retezec.split(",")
        try:
            internal_1, internal_2 = x.split("/")
            internal_3, internal_4 = y.split("/")
            z1 = Zlomek(int(internal_1), int(internal_2))
            z2 = Zlomek(int(internal_3), int(internal_4))
            return Vector(z1, z2)
        except:
            return Vector(float(x), float(y))


if __name__ == "__main__":
    v1 = Vector(Zlomek(1),Zlomek(1))
    v2 = Vector(Zlomek(6, 4),Zlomek(7,4))
    print(v1.phi())
    print(v1 + v2)
    print(v2)

    print(v1.velikost())
    print(abs(v1))
    print(v1.fromStr("3/4,2/5"))