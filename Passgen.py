import customtkinter as ctk
import random
import string
import subprocess
import os

ctk.set_appearance_mode("system")
ctk.set_default_color_theme('dark-blue')
win = ctk.CTk()
win.title('Passgen!')
win.geometry("520x125")

server = 'server.bat'
passfile = 'passwrdgen.txt'


def web():
    port_ask.get()
    ip_ask.get()
    with open(server, "w") as file:
        file.write(f"py -3 -m http.server {port_ask.get()} -b {ip_ask.get()}")
        file.close()

    subprocess.call(server)


def passgen(length: int):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_strs = ''.join(random.choice(characters) for _ in range(length))
    return random_strs


def generate():
    chars_ask.get()
    plat_ask.get()
    user_ask.get()

    if chars_ask.get() == "Character Amount":
        char_def = ctk.CTkLabel(master=win, text="Select a character amount!", text_color="red")
        char_def.grid(row=4, column=1, padx=5, pady=3)
    else:
        characters = int(chars_ask.get())
        with open(passfile, "a") as file_:
            file_.write(
                f"Platform: {plat_ask.get()} | User: {user_ask.get()} | Password: " + passgen(characters) + os.linesep)
            file_.close()


def openfile():
    os.startfile(passfile)


plat_ask = ctk.CTkEntry(master=win,
                        placeholder_text="Enter Platform Here", width=165)
plat_ask.grid(row=1, column=0, padx=5, pady=3)
user_ask = ctk.CTkEntry(master=win,
                        placeholder_text="Enter Username Here", width=165)
user_ask.grid(row=2, column=0, padx=5, pady=3)
chars_ask = ctk.CTkComboBox(master=win, text_color="dark gray", width=165,
                            values=["Character Amount", "10", "12", "14", "16", "18", "20"])
chars_ask.grid(row=3, column=0, padx=5, pady=3)
port_ask = ctk.CTkEntry(master=win,
                        placeholder_text="Enter Port Here", width=165)
port_ask.grid(row=2, column=2, padx=5, pady=3)
ip_ask = ctk.CTkEntry(master=win,
                      placeholder_text="Enter Ip Address Here", width=165)
ip_ask.grid(row=1, column=2, padx=5, pady=3)

bttn_gen = ctk.CTkButton(master=win, text="Generate!", command=generate)
bttn_gen.grid(row=1, column=1, padx=5, pady=3)
bttn_web = ctk.CTkButton(master=win,
                         text="Start Webserver!", command=web)
bttn_web.grid(row=3, column=2, padx=5, pady=3)
bttn_open = ctk.CTkButton(master=win, text="Open Password File!", command=openfile)
bttn_open.grid(row=3, column=1, padx=5, pady=3)

watermark = ctk.CTkLabel(master=win, text='Passgen!', font=('Goudy Old Style', 24),
                         text_color='dark gray')
watermark.grid(row=2, column=1, padx=5, pady=3)
win.mainloop()
