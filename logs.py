from klase import Prece, Dators, Mātesplate
import tkinter as tk
from tkinter import ttk, END

root= tk.Tk()
root.title("Detaļu un programmatūru uzskaite")
root.geometry("500x400")

frame = ttk.Frame(root)
frame.grid(padx=10, pady=10)
options = {"padx": 5, "pady": 5}

# Preču saraksts
visas_preces = []
total_income = 0

# Ekrāns

# Nosaukums label
nosaukums_label = ttk.Label(frame, text='Nosaukums')
nosaukums_label.grid(column=0, row=0, sticky='w', **options)

prece_label = ttk.Label(frame, text='Prece')
prece_label.grid(column=0, row=1, sticky='w', **options)

skaits_label = ttk.Label(frame, text='Skaits')
skaits_label.grid(column=0, row=2, sticky='w', **options)

izgatavotajs_label = ttk.Label(frame, text='Izgatavotājs')
izgatavotajs_label.grid(column=0, row=3, sticky='w', **options)


# nosaukums entry
nosaukums = tk.StringVar()
nosaukums = ttk.Entry(frame, textvariable=nosaukums)
nosaukums.grid(column=1, row=0, **options)
nosaukums.focus()

# skaits entry
skaits = tk.StringVar()
skaits_entry = ttk.Entry(frame, textvariable=skaits)
skaits_entry.grid(column=1, row=1, **options)

# prece entry
prece = tk.IntVar()
prece_entry = ttk.Entry(frame, textvariable=prece)
prece_entry.grid(column=1, row=2, **options)

# izgatavotajs entry
izgatavotajs = tk.IntVar()
izgatavotajs_entry = ttk.Entry(frame, textvariable=izgatavotajs)
izgatavotajs_entry.grid(column=1, row=3, **options)


# ražošanas button
def convert_button_clicked():
    preces_nosaukums = nosaukums.get()
    preces_skaits = skaits.get()
    preces_tips = prece.get()
    preces_izgatavotajs = izgatavotajs.get()
    visas_preces.append(Prece(preces_nosaukums, preces_skaits, preces_tips, preces_izgatavotajs))
    result_label.config(text=visas_preces[-1].pastastit_par_sevi())
    nomainit_sarakstu()


razot_button = ttk.Button(frame, text='Ražot')
razot_button.grid(column=2, row=0, sticky='W', **options)
razot_button.configure(command=convert_button_clicked)

# Saraksta loga atjaunošana
saturs = tk.Variable(value=tuple(visas_preces))

listbox = tk.Listbox(
    root,
    listvariable=saturs,
    height=6,
    selectmode=tk.EXTENDED
)

listbox.grid(row=4, columnspan=3, **options)


# Listbox saraksta atjaunošana
def nomainit_sarakstu():
    listbox.delete(0,END)
    for preces in visas_preces:
        listbox.insert("end","{},{},{},{}".format(preces.name,preces.identity,preces.number,preces.izgatavotajs))


# result label
result_label = ttk.Label(frame)
result_label.grid(row=3, columnspan=3, **options)

# start the app
root.mainloop()