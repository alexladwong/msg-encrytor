from tkinter import *
from tkinter import messagebox
import base64
import os


def decrypt():
    password = code.get()

    if password == "1234":
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x400")
        screen2.configure(bg="#00bd56")

        message = text1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt=base64_bytes.decode("ascii")

        Label(screen2, text="DECRYPT", font="arial", bg="#00bd56").place(x=10, y=0)
        text2 = Text(screen2, font="Rpbote 20", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=50, width=380, height=180)

        text2.insert(END, decrypt)

    elif password == "":
        messagebox.showerror("encryption", "Input Password")

    elif password != "1234":
        messagebox.showerror("encryption", "Invalid Password")


def encrypt():
    password = code.get()

    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x400")
        screen1.configure(bg="#ed3833")

        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen1, text="ENCRYPT", font="arial", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen1, font="Rpbote 20", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=50, width=380, height=180)

        text2.insert(END, encrypt)

    elif password == "":
        messagebox.showerror("encryption", "Input Password")

    elif password != "1234":
        messagebox.showerror("encryption", "Invalid Password")


def main_screen():
    global screen
    global code
    global text1

    screen = Tk()

    screen.geometry("370x400")
    # icon
    image_icon = PhotoImage(file="key.png")
    screen.iconphoto(False, image_icon)

    screen.title("MSGEncryptorApp")

    def reset():
        code.set("")
        text1.delete(1.0, END)

    Label(text="Enter text to be encrypted and decrypted for you", font=("calibri", 14)).place(x=10, y=10)
    text1 = Text(font="Robote 20", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text="Enter your secret key to Encrypt Decrypt messages", fg="black", font=("calibri", 14)).place(x=10, y=160)

    code=StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)

    Button(text="ENCRYPT", height="2", width=15, bg="#ed3833", fg="black", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=15, bg="#00bd56", fg="black", bd=0, command=decrypt).place(x=180, y=250)
    Button(text="RESET NOW", height="2", width=33, bg="#1089ff", fg="black", bd=0, command=reset).place(x=13, y=300)

    screen.mainloop()


main_screen()
