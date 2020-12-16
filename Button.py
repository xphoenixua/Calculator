import tkinter as tk


class Button(tk.Button):
    def __init__(self, master, **kwargs):
        tk.Button.__init__(self, master, width=6, height=2, **kwargs)