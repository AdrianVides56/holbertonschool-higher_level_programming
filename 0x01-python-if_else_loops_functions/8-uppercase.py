#!/usr/bin/python3
def uppercase(str):
    strUPPER = ""

    for lowToUpp in str:
        if ((ord(lowToUpp) < 97 or ord(lowToUpp) > 122)):
            strUPPER = strUPPER + lowToUpp
        elif (ord(lowToUpp) > 97 or ord(lowToUpp) < 122):
            uP = (ord(lowToUpp) - 32)
            strUPPER = strUPPER + (chr(uP))
    print("{:s}".format(strUPPER))
