import itertools

str = input('string a ser permuntada')

resultado = itertools.permutations(str, len(str))

for i in resultado:
    print(''.join(i))