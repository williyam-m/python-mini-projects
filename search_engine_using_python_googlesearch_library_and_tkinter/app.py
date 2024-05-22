import webbrowser
from tkinter import *
from googlesearch import search

def search_google():
    query = entry.get()
    num_links = links_entry.get()
    if num_links.isdigit():
        search_results = search(query, num=int(num_links), stop=int(num_links), pause=2)
        display_results(search_results)
    else:
        error_label.config(text="Please enter a valid number",fg="red")


def display_results(results):
    for i, link in enumerate(results):
        button = Button(result_frame, text=link, width=100, command=lambda l=link: open_link(l), font=("Helvetica", 15, "bold"),)
        button.grid(row=i, column=0, sticky=W, pady=5)
        button.config(borderwidth=4, relief="solid", bg="#3b3c36", fg="white")

def open_link(url):
    webbrowser.open_new(url)

root = Tk()
root.title("Simple Search Engine")
root.geometry("1200x700")

frame = Frame(root)
frame.pack(pady=15)

label = Label(frame, text="Enter your query:")
label.pack(side=LEFT)

entry = Entry(frame, width=100)
entry.pack(side=LEFT)

links_label = Label(root, text="Number of Links:")
links_label.pack()

links_entry = Entry(root, width=20)
links_entry.pack()

error_label = Label(root, text="", fg="red")
error_label.pack()


button = Button(root, text="  Search  ", command=search_google)
button.pack(pady=10)

result_frame = Frame(root, bd=2, relief="solid")
result_frame.pack(pady=15)

root.mainloop()
