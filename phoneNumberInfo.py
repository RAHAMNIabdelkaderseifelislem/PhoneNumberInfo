#pip install phonenumbers
import phonenumbers as pn
from phonenumbers import geocoder
from phonenumbers import carrier

num = input("Enter full phone number : ")
phone = pn.parse(num)
print(geocoder.description_for_number(phone, 'en'))
print(carrier.name_for_number(phone,'en'))