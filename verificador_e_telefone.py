from pydoc import describe
from phonenumbers import geocoder
import phonenumbers

phone = input('Digite o telefone no formato: +5511974969463: ')

phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))