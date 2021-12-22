import os
import requests
from colorama import *
init(autoreset=True)
from config import *


os.system("title IP-Lookup")
print(Fore.RED + 'for educational purposes only')
IP = input("{IP-ADD}: ")
os.system("cls")


URLDATA = f'https://api.ipgeolocation.io/ipgeo?apiKey={apikey}&ip={IP}&excludes=continent_code,currency,time_zone'
data = requests.get(URLDATA).json()
isp = data['isp']
stateprov = data['state_prov']
city = data['city']

os.system(f"title Lookup Data: {IP}")
print("====================================")
print(f"info to: {IP}")
print("====================================")
print(f"ISP: {isp}")
print(f"State: {stateprov}")
print(f"City: {city}")
print("")
os.system("pause")

