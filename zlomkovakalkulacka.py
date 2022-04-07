##### Užití modulu zlomky
from zlomky import *
## modul operator
import operator

# namapování řetězců na operace
operace = {
    "+": operator.add,
    "-": operator.sub,
    "*" : operator.mul,
    "/" : operator.truediv,
    "^" : operator.pow
    }

###### funkce
def str2Zlomek(retezec):
    '''
        Converts string in a form "a/b" to fraction class Zlomek
        Return: Zlomek(a, b)
    '''
    retezec = str(retezec) ### zajistime, ze máme string
    if "/" in retezec: ### obsahuje řetězec lomítko ?
        z = retezec.split("/")
        if z[0].isdigit() and z[1].isdigit():
            return Zlomek(int(z[0]), int(z[1]))
        else:
            return None
    else:
        if retezec.isdigit():
            return Zlomek(retezec, 1)
        return None
### HLAVNÍ PROGRAM
print("\nPříklad musí mít dvě racionální čísla, jeden operátor (+, -, *, /, ^) a rovnítko.\nVšechny čtyři členy oddělte mezerami.")        #úvodní instrukce
print("Operátor ^ lze také napsat pomocí klávesové zkratky ALT + 94.\nPro ukončení stiskněte ENTER.\n")

print(operace["+"](3,4))
#### hlavní programová smyčka
while True:
    vstup = input("Zadej příklad (ENTER pro ukončení): ").strip().split()
    if len(vstup) == 3:
        zlomek1 = str2Zlomek(vstup[0])
        op = vstup[1] ## operátor
        zlomek2 = str2Zlomek(vstup[2])
        if op in operace.keys():
            zlomek3 = operace[op](zlomek1,zlomek2)
            print(zlomek1, op, zlomek2, "=", zlomek3)
        else:
            print(f"Chyba: {op} zatím není podporovaným operátorem naší kalkulačky!")
    else:
        break
### KONEC



