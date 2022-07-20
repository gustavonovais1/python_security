from cmath import e
from re import A
import socket
import sys

from numpy import tri

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    except socket.error as e:
        print('A conexão falhou!!!')
        print('Erro: {}'.format(e))
        sys.exit()
    
    print('socket criado com sucesso')

    hostAlvo = input('Diite o host ou ip a ser conectado: ')
    portaAlvo = input('Diite a porta ou ip a ser conectado: ')

    try:
        s.connect((hostAlvo, int(portaAlvo)))
        print('Cliente conectado com sucesso no host: '+ hostAlvo, portaAlvo +'na porta: ' + portaAlvo)
        s.shutdown(2)
    except socket.error as e:
        print('Não foi possível conectar no host: '+ hostAlvo+ '-porta: '+ portaAlvo)
        print('Erro: {}'.format(e))
        sys.exit()

if __name__=="__main__":
    main()