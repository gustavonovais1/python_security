import re
import json
from urllib.request import urlopen

from matplotlib.font_manager import json_load

url = 'https://ipinfo.io/json'

resposta = urlopen(url)

dados = json_load(resposta)

ip = dados['ip']
org = dados['org']
cid = dados['city']
pais = dados['country']
regiao = dados['region']

print('Detalhes do IP externo\n')
print('Ip: {4}\nregiao: {1}\nPais: {2}\nCidade: {3}\nOrg: {0}'.format(org, regiao, pais, cid, ip))