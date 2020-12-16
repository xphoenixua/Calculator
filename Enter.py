import tkinter as tk

class Enter:
    def __init__(self):
        self.total=0
        self.current=''
        self.input_value=True
        self.check_sum=False
        self.operation=''
        self.result=False
        
    def numEnter(self,num):
        self.result=False
        num_first=enterField.get()
        num_second=str(num)
        if self.input_value:
            self.current=num_second
            self.input_value=False
        else:
            if num_second == '.':
                if num_second in num_first:
                    return
            self.current=num_first + num_second
        self.display(self.current)

    def display(self,value):
        enterField.delete(0,tk.END)
        enterField.insert(0,value)