from tkinter import *
import psycopg2

def insert_data():
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='password')
    cur = conn.cursor()
    name = name_entry.get()
    price = float(price_entry.get())
    quantity = int(quantity_entry.get())
    query = '''INSERT INTO products(NAME, PRICE, QUANTITY) VALUES(%s, %s, %s)'''
    cur.execute(query, (name, price, quantity))
    print('Data inserted')
    conn.commit()
    conn.close()

def search():
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='password')
    cur = conn.cursor()
    id = name_search.get()
    query = '''SELECT * FROM products where id=%s'''
    cur.execute(query, (id))
    row = cur.fetchone()
    listbox = Listbox(frame, width=20, height=1)
    listbox.grid(row=6, column=1)
    listbox.insert(END, row)
    conn.commit()
    conn.close()

def display_all():
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='password')
    cur = conn.cursor()
    query = '''SELECT * FROM products'''
    cur.execute(query)
    row = cur.fetchall()
    listbox = Listbox(frame, width=20, height=5)
    listbox.grid(row=8, column=1)
    for x in row:
        listbox.insert(END, x)
    conn.commit()
    conn.close()

root = Tk()
root.minsize(width=400, height=300)

frame = Frame(root)
frame.pack()
Label(frame, text='Add data:').grid(row=0, column=1, pady=10)
Label(frame, text='Name:').grid(row=1, column=0)
Label(frame, text='Price:').grid(row=2, column=0)
Label(frame, text='Quantity:').grid(row=3, column=0)

name_entry = Entry(frame)
name_entry.grid(row=1, column=1)
price_entry = Entry(frame)
price_entry.grid(row=2, column=1)
quantity_entry = Entry(frame)
quantity_entry.grid(row=3, column=1)
name_search = Entry(frame)
name_search.grid(row=5, column=1)

Button(frame, text='Add', command=insert_data).grid(row=4, column=1, pady=10)
Button(frame, text='Search', command=search).grid(row=5, column=0)
Button(frame, text='Display all', command=display_all).grid(row=7, column=1)

root.mainloop()