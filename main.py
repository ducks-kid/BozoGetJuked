from subprocess import CREATE_NEW_CONSOLE
import requests
import random
import string
import time
import colorama
from colorama import init, Fore, Back, Style
import os
import ctypes



ctypes.windll.kernel32.SetConsoleTitleW("Bossmans Discord Nitro GEN + CODE CHECKER")

init(convert=True)
init()

print(Back.WHITE + Fore.BLACK + """NITRO GEN + CHECKER | BY Boss man |        """)
time.sleep(2)
print(Back.WHITE + Fore.BLACK + "                                           ")
time.sleep(0.5)
print("GET YOUR VALID NITROS AT VALID CODES.TXT   ")
time.sleep(0.5)

print(Back.RED + "                                           ")
time.sleep(0.5)
print("MADE BY Boss man                           ")
time.sleep(0.5)
print(Back.RED + "                                           \n\n")
time.sleep(0.5)

init(convert=True)

print(Style.RESET_ALL)

num = int(input('HOW MANY CODES YOU WANT : '))

if num == 1000000:  
    print(Fore.RED + Back.GREEN + "      Make sure to run only one since this could crash the PC / THE CONSOLE       ")
    print(Style.RESET_ALL)
    print(" ")
    
    ans = input(Fore.GREEN + Back.RED + "   Type OK or CANCEL   ")
    if ans == "OK":
        print("      Starting       ")
        time.sleep(1)
    elif ans == "CANCEL":
        print("      DESTROYING the CLIENT       ")
        time.sleep(1)
        exit

    print(Style.RESET_ALL)




with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print("STATUS : OK")

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"GENERATED {num} CODES | TIME TAKEN : {time.time() - start}\n")

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(Back.GREEN + Fore.BLACK + f" Valid | {nitro} ")
            break
        else:
            print(Fore.RED + f" Invalid | {nitro} ")

input("\n CHECK VALID CODES.TXT FOR VALID CODES")