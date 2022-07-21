import hashlib  

strin = input('Digite o texto a ser convertido para hash')

menu = int(input(''' ### MENU - ESCOLHA O TIPO DE HASH ###
        1) MD5
        2) SHA1
        3) SHA2256
        4) HSA512
        Digite o numero de hash a ser gerador'''))

if menu == 1:
    resultado = hashlib.md5(strin.encode('utf-8'))
    print('O hash MD5 da string: ', str ,'e: ', resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(strin.encode('utf-8'))
    print('O hash sha1 da string: ', str ,'e: ', resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(strin.encode('utf-8'))
    print('O hash sha256 da string: ', str ,'e: ', resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(strin.encode('utf-8'))
    print('O hash sha512 da string: ', str ,'e: ', resultado.hexdigest())
else:
    print('Algo deu errado, tente novamente!')