import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def generate_table(contact_information, window):
    # define columns
    columns = ('name', 'phone_number', 'email_address')

    tree = ttk.Treeview(window, columns=columns, show='headings')

    # define headings
    tree.heading('name', text='Name')
    tree.heading('phone_number', text='Phone Number')
    tree.heading('email_address', text='Email Address')

    # generate sample data
    contacts = []
    for n in range(1, 100):
        contacts.append((f'name {n}', f'number {n}', f'email{n}@example.com'))

    # add data to the treeview
    for contact in contact_information:
        print(contact)
        tree.insert('', tk.END, values=contact)

    def item_selected(event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
            # show a message
            showinfo(title='Information', message=','.join(record))

    tree.bind('<<TreeviewSelect>>', item_selected)

    tree.grid(row=0, column=0, sticky='nsew')