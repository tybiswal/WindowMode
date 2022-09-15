import tkinter as tk


window = tk.Tk()
title = tk.Label(text="Your Personal Details",
                 width=50,
                 height=2
                 )
typer = tk.Entry()
click = tk.Button(text="Click Me",
                  width=10,
                  height=2,
                  bg="#34A2FE"
                  )

title.pack()
typer.pack()
click.pack()
window.mainloop()
