import os
import subprocess
import random
import string
import time

passfile = 'passwrdgen.txt'
pin = ""


def pincheck():
    pin_ask = input('Enter Pin: ')
    if pin_ask == pin:
        print('Correct Pin!')
        pass
    else:
        print('Incorrect Pin!')
        pincheck()


def web():
    server = 'server.bat'
    with open(server, 'w') as file:
        file.write(f'py -3 -m http.server {port} -b {ip}')
    subprocess.call(server)


def passgen(length: int):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_strs = ''.join(random.choice(characters) for _ in range(length))
    return random_strs


def generate():
    global chars_ask
    global plat_ask
    global user_ask

    characters = int(chars_ask)
    with open(passfile, "a") as file_:
        file_.write(
            f"Platform: {plat_ask} | User: {user_ask} | Password: " + passgen(characters) + os.linesep)
        file_.close()


print('   R              G               E')
time.sleep(0.7)
print('          0               U             !')
time.sleep(0.7)
print('')
print('')
print('|  PassGen! A Simple Password Generator!  |')
print('')
print('')
pincheck()
plat_ask = input('Enter Platform: ')
print('')
user_ask = input('Enter Username: ')
print('')
while True:
    chars_ask = input('Enter the amount of characters for the password: ')
    if chars_ask.isdigit():
        chars_ask = int(chars_ask)
        break
    else:
        print('Please enter a valid integer for the number of characters!')
generate()
print('')
print(f'Successfully generated in {passfile}!')
print('')
ser_ask = input('Do you want to start a web server to host the text file? (Y/N)')
if ser_ask == "Y":
    print('')
    ip = input('Enter IP Address: ')
    print('')
    port = input('Enter Port: ')
    print('')
    web()
else:
    pass
