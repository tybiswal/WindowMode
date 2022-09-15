import tkinter as tk


window = tk.Tk()
title = tk.Label(text="Your Personal Details")
typer = tk.Entry()
click = tk.Button(text="Click Me")

title.pack()
typer.pack()
click.pack()
window.mainloop()

