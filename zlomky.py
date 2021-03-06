"""
making a class for franction
autor: Alex Olivier Michaud
"""
#Import
from math import gcd, lcm   #import největšího společného dělitele a nejměnšího společného násobku
#Class
class Zlomek:
     def __init__(self, citatel, jmenovatel=1):
         """
         :param citatel: int
         :param jmenovatel: int
         """
         self.citatel = (citatel)
         self.jmenovatel = (jmenovatel)

     def check_if_gdc(self):
         """
         přepíše objekt, tak aby se zlomek zkrátil
         """
         delitel = gcd(self.citatel, self.jmenovatel)   #hledání dělitele
         if delitel != self.citatel or delitel != self.jmenovatel:  #podmínky aby se to nezkracovalo když už je zlomek zkrácený
             self.citatel = self.citatel // delitel     #zrátění zlomku
             self.jmenovatel = self.jmenovatel // delitel

     def __add__(self, other):
         """
         Definování základního typu +
         :param other: obj type Zlomek
         :return:
         """
         lcmultiple = lcm(self.jmenovatel, other.jmenovatel)    #vyhledání násobku
         how_many_times_fits_in_1 = lcmultiple // self.jmenovatel   #vyhledání kolikrát výnasobit zlomek, aby se mohl upravit
         how_many_times_fits_in_2 = lcmultiple // other.jmenovatel
         zlomek = Zlomek(self.citatel*how_many_times_fits_in_1 + other.citatel*how_many_times_fits_in_2,
                         self.jmenovatel*how_many_times_fits_in_1 ) #definování nového objektu
         zlomek.check_if_gdc()  #zkrácení
         return zlomek

     def __sub__(self, other):
         """
         Definování základního typu -
         :param other: obj type Zlomek
         :return: obj type Zlomek
         """
         lcmultiple = lcm(self.jmenovatel, other.jmenovatel)    #vyhledání násobku
         how_many_times_fits_in_1 = lcmultiple // self.jmenovatel   #vyhledání kolikrát výnasobit zlomek, aby se mohl upravit
         how_many_times_fits_in_2 = lcmultiple // other.jmenovatel
         zlomek = Zlomek(self.citatel * how_many_times_fits_in_1 - other.citatel * how_many_times_fits_in_2,
                         self.jmenovatel * how_many_times_fits_in_1) #definování nového objektu
         zlomek.check_if_gdc()  #zkrácení
         return zlomek

     def __truediv__(self, other):
         """
         Definování základního typu /
         :param other: obj type Zlomek
         :return: obj type Zlomek
         """
         zlomek = Zlomek(self.citatel * other.jmenovatel, self.jmenovatel * other.citatel)      #otočení a vynásobení zlomku
         zlomek.check_if_gdc()  #zkrácení
         return zlomek

     def __mul__(self, other):
         """
         Definování základního typu *
         :param other: obj type Zlomek
         :return: obj type Zlomek
         """
         zlomek = Zlomek(self.citatel * other.citatel, self.jmenovatel * other.jmenovatel)  #násobení zlomku
         zlomek.check_if_gdc()  #zkrácení
         return zlomek

     def __str__(self):
         """
         definování základní funkce print
         :return: formated string of fraction
         """
         if self.jmenovatel == 1:   #jestli je jmenovatel jedna vrací to pouze čitatel
            return f"{self.citatel}"
         else:                      #všechny ostatní příprady
            return f"{self.citatel}/{self.jmenovatel}"

     def __pow__(self, power):
         """
         :param power: zlomek
         :return: zlomek
         """
         citatel_pow = self.citatel ** (power.citatel /power.jmenovatel)
         jmenovatel_pow = self.jmenovatel ** (power.citatel /power.jmenovatel)
         if citatel_pow - int(citatel_pow) == 0 and jmenovatel_pow - int(jmenovatel_pow) == 0:
             new_zlomek = Zlomek(int(citatel_pow), int(jmenovatel_pow))
             new_zlomek.check_if_gdc()
             return new_zlomek
         else:
             new_zlomek = Zlomek((citatel_pow), (jmenovatel_pow))

             return new_zlomek


#Main program
if __name__ == "__main__":
    z1 = Zlomek(3)
    z2 = Zlomek(1, 3)
    z3 = z1 + z2
    print(f"{z1} + {z2} = {z3}")
    print(Zlomek(1,2) ** Zlomek(1, 2))


