from tkinter import END, Frame, Tk, Button, Label, Text
import pyperclip
import re

def creaelenco():
    indirizzi = ''
    test = text_input.get("1.0", END).strip()
    elenco = re.findall("([\S]*@[\S]*\.[\w]*)", test)

    for i in elenco:
        indirizzi += i.replace('\n', '').replace('<', '')+';'
    indirizzi = indirizzi[:-1]
    text_output.delete("1.0", END)
    text_output.insert("1.0", indirizzi)

interfaccia = Tk()
interfaccia.geometry("600x600")
interfaccia.title("Email Address Extractor")

testo = Frame(interfaccia, bd=3, relief="ridge", padx=15, pady=15)
testo.pack()

lb_input = Label(testo, text="Input:")
lb_input.pack()
text_input = Text(testo, bg="white", fg="black", padx=20, pady=20, height=9)
text_input.pack()
bt_input = Button(testo, text="Extract", command=creaelenco)
bt_input.pack(pady=10)

output = Frame(interfaccia, bd=3, relief="ridge", padx=15, pady=15)
output.pack()

lb_output = Label(output, text="Output:")
lb_output.pack()
text_output = Text(output, bg="white", fg="black", padx=20, pady=20, height=9)
text_output.pack()
bt_copy = Button(output, text="Copy to clipboard", command=lambda: pyperclip.copy(text_output.get('1.0', END)))
bt_copy.pack(pady=10)

interfaccia.mainloop()