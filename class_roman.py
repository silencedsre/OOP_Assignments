"""

Write a Python class that has an integer attribute set via a constructor and a method to convert the number to roman numeral.

"""

class Roman:

    def __init__(self,num):
        self.num=num

    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  self.num > 0:
            for _ in range(self.num // val[i]):
                roman_num += syb[i]
                self.num -= val[i]
            i += 1
        return roman_num

roman_obj=Roman(1)
print(roman_obj.int_to_Roman(1))