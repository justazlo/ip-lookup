import os
import requests
import colorama
from colorama import Fore

colorama.init()

os.system("cls")
print(f'''{Fore.LIGHTRED_EX}
████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗
╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝
   ██║   ██████╔╝███████║██║     █████╔╝ ███████╗
   ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ╚════██║
   ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████║
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝''')

ip = input(Fore.LIGHTCYAN_EX + 'Enter IP Address: ')
url = requests.get(f"https://ipapi.co/{ip}/json")
print(Fore.LIGHTGREEN_EX + url.text)