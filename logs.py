from klase import Prece, Dators, Mātesplate
import tkinter as tk
from tkinter import ttk, END
import tkinter.messagebox

root= tk.Tk()
root.title("Detaļu un programmatūru uzskaite")
root.geometry("600x500")

frame = ttk.Frame(root)
frame.grid(padx=10, pady=10)
options = {"padx": 5, "pady": 5}

# Preču saraksts
visas_preces = []
total_income = 0

# Ekrāns

# Nosaukums label and entry
nosaukums_label = ttk.Label(frame, text='Nosaukums')
nosaukums_label.grid(column=0, row=0, sticky='w', **options)

nosaukums = tk.StringVar()
nosaukums_entry = ttk.Entry(frame, textvariable=nosaukums)
nosaukums_entry.grid(column=1, row=0, **options)
nosaukums_entry.focus()

# Prece label and entry
prece_label = ttk.Label(frame, text='Prece')
prece_label.grid(column=0, row=1, sticky='w', **options)

prece = tk.StringVar()
prece_entry = ttk.Entry(frame, textvariable=prece)
prece_entry.grid(column=1, row=1, **options)

# Izgatavotājs label and entry
izgatavotajs_label = ttk.Label(frame, text='Izgatavotājs')
izgatavotajs_label.grid(column=0, row=2, sticky='w', **options)

izgatavotajs = tk.StringVar()
izgatavotajs_entry = ttk.Entry(frame, textvariable=izgatavotajs)
izgatavotajs_entry.grid(column=1, row=2, **options)

# Skaits label and entry
skaits_label = ttk.Label(frame, text='Skaits')
skaits_label.grid(column=0, row=3, sticky='w', **options)

skaits = tk.StringVar()
skaits_entry = ttk.Entry(frame, textvariable=skaits)
skaits_entry.grid(column=1, row=3, **options)

# Cena label and entry
cena_label = ttk.Label(frame, text="Cena:")
cena_label.grid(row=4, column=0, sticky="w", **options)

cena = tk.StringVar()
cena_entry = ttk.Entry(frame, textvariable=cena)
cena_entry.grid(row=4, column=1, **options)

def nomainit_sarakstu():
    for i in tree.get_children():
        tree.delete(i)

    for prece in visas_preces:
        tree.insert("", "end", values=(
            prece.name,
            prece.get_identity_text(),  
            prece.izgatavotajs,
            prece.number,
            prece.cena
        ))

# ražošanas button
def convert_button_clicked():
    preces_nosaukums = nosaukums.get()
    preces_skaits = skaits.get()
    preces_tips = prece.get().lower()  
    preces_izgatavotajs = izgatavotajs.get()
    preces_cena = cena.get()
    
   
    if preces_tips not in ["p", "d", "da"]:
        tk.messagebox.showerror("Kļūda", "Nederīgs preces tips. Lūdzu, ievadiet 'p' programmatūrai, 'd' detaļai vai 'da' datoram.")
        return
    
    visas_preces.append(Prece(preces_nosaukums, preces_tips, preces_izgatavotajs, preces_skaits, preces_cena))
    nomainit_sarakstu()  
    
    # Notīra ievades laukus
    nosaukums.set("")
    skaits.set("")
    prece.set("")
    izgatavotajs.set("")
    cena.set("")
    
    nosaukums_entry.focus()

razot_button = ttk.Button(frame, text='Ražot')
razot_button.grid(column=2, row=0, sticky='W', **options)
razot_button.configure(command=convert_button_clicked)


saturs = tk.Variable(value=tuple(visas_preces))


tree = ttk.Treeview(root, columns=("nosaukums", "tips", "izgatavotajs", "skaits", "cena"), show="headings")
tree.grid(row=6, columnspan=3, sticky="nsew", **options)

# Kolonnu virsrakstus
tree.heading("nosaukums", text="Nosaukums")
tree.heading("tips", text="Kas par produktu")
tree.heading("izgatavotajs", text="Izgatavotājs")
tree.heading("skaits", text="Skaits")
tree.heading("cena", text="Cena")

# Kolonnu platumus
tree.column("nosaukums", width=100)
tree.column("tips", width=100)
tree.column("izgatavotajs", width=100)
tree.column("skaits", width=50)
tree.column("cena", width=50)


# Konfigurējam kolonnu un rindu paplašināšanos
root.columnconfigure(0, weight=1)
root.rowconfigure(6, weight=1)
frame.columnconfigure(1, weight=1)

root.mainloop()