import tkinter as tk


class Button:
    def __init__(self, master, text, command, row, col, width=6, height=2):
        self.btn = tk.Button(master,
                             text=text,
                             command=command,
                             width=width,
                             height=height,
                             )
        self.btn.grid(row=row, column=col)
