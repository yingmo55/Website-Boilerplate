import os

path = ''
def replace_all():
    x = input(r'enter the string you want to replace ')
    y = input(r'enter the symbol you want to replace ')
    z= input(r'enter the symbol you want {0} to be replaced as '.format(y))
    x = x.replace(y, z)
    print ("here's the text:", x)
    return x