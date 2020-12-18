#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string:
        idic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        if roman_string in idic:
            return idic[roman_string]
        else:
            buff = []
            numInInteger = []
            aux = 0
            for a in roman_string:
                if a == 'I':
                    buff += '1'
                elif a == 'V':
                    buff += '5'
                elif a == 'X':
                    buff += ['10']
                elif a == 'L':
                    buff += ['50']
                elif a == 'C':
                    buff += ['100']
                elif a == 'D':
                    buff += ['500']
                elif a == 'M':
                    buff += ['1000']
            print(buff)
            for b in range(len(buff)):
                print(numInInteger)
                if b == (len(buff) - 1):
                    numInInteger += [buff[b]]
                elif buff[b + 1] == buff[b]:
                    aux = int(buff[b]) + int(buff[b + 1])
                    numInInteger += [aux]
                else:
                    numInInteger += [buff[b]]
        return None
    return None
