import tkinter as tk
import Button as b
import math
from functools import partial


def update_enterField(clicked_button):
    if enterField.get() == '0':
        enterField.delete(0)
    updated_text = str(clicked_button.cget('text'))
    enterField.insert(tk.END, updated_text)

def backspace():
    back_var = enterField.get()[:-1]
    enterField.delete(0,tk.END)
    enterField.insert(0,back_var)

def clear_enterField():
    enterField.delete(0,tk.END)
    enterField.insert(0, '0')

def calculation():
    enterField_text = enterField.get()[::]
    print(enterField_text)
    result = None
    if '*' in enterField_text:
        first_num = int(enterField_text.split('*')[0])
        second_num = int(enterField_text.split('*')[-1])
        result = first_num * second_num
    elif '/' in enterField_text:
        first_num = enterField_text.split('/')[0]
        second_num = enterField_text.split('/')[-1]
        result = int(first_num) / int(second_num)
    elif '+' in enterField_text:
        first_num = int(enterField_text.split('+')[0])
        second_num = int(enterField_text.split('+')[-1])
        result = first_num + second_num
    elif '-' in enterField_text:
        first_num = int(enterField_text.split('-')[0])
        second_num = int(enterField_text.split('-')[-1])
        result = first_num - second_num
    
    enterField.delete(0,tk.END)
    enterField.insert(0,result)

window = tk.Tk()
window.title('Багатофункціональний калькулятор')
window.geometry('800x500')
window.resizable(width='False', height='False')
calculator = tk.Frame(window)
calculator.grid()

# --- enter field --- #

enterField = tk.Entry(calculator, justify=tk.RIGHT)
enterField.insert(0, '0')
enterField.grid(row=0, column=0, columnspan=4, pady=10)

btn_Backspace = tk.Button(calculator, text='<=', command=backspace, background='#15C54D')
btn_Backspace.grid(row=0, column=3, pady=1, padx=10)

# --- NumPad --- #

numPad = [7, 8, 9, 4, 5, 6, 1, 2, 3]
num = 0
for i in range(2, 5):
    for j in range(3):
        btn = tk.Button(calculator, text='{}'.format(numPad[num]), width=6, height=2)
        btn.configure(command=partial(update_enterField, btn))
        btn.grid(row=i, column=j, pady=1)
        num += 1

# --- misc --- #

btn_Zero = tk.Button(calculator, text='0', command=lambda: update_enterField(btn_Zero), width=12, height=1)
btn_Zero.grid(row=5, column=0, columnspan=2)

btn_Comma = tk.Button(calculator, text=',', command=lambda: update_enterField(btn_Comma), width=6, height=1)
btn_Comma.grid(row=5, column=2)

btn_Equal = tk.Button(calculator, text='=', width=12, height=2, command=calculation)
btn_Equal.grid(row=4, column=3, columnspan=2)

# --- Memory buttons --- #

btn_MemoSave = tk.Button(calculator, text='MS', )
btn_MemoSave.grid(row=1, column=0, pady=1)

btn_MemoRead = tk.Button(calculator, text='MR', )
btn_MemoRead.grid(row=1, column=1, pady=1)

btn_MemoClear = tk.Button(calculator, text='MC', command=clear_enterField)
btn_MemoClear.grid(row=1, column=2, pady=1)

btn_MemoAdd = tk.Button(calculator, text='M+', )
btn_MemoAdd.grid(row=1, column=3, pady=1, padx=10)

btn_MemoSubtract = tk.Button(calculator, text='M-', )
btn_MemoSubtract.grid(row=1, column=4, pady=1, padx=10)


# --- simple operations --- #

btn_Plus = b.Button(calculator, text='+', command=lambda: update_enterField(btn_Plus))
btn_Subtract = b.Button(calculator, text='-', command=lambda: update_enterField(btn_Subtract))
btn_Divide = b.Button(calculator, text='/', command=lambda: update_enterField(btn_Divide))
btn_Multiply = b.Button(calculator, text='*', command=lambda: update_enterField(btn_Multiply))

btn_Plus.grid(row=2, column=3)
btn_Subtract.grid(row=2, column=4)
btn_Divide.grid(row=3, column=3)
btn_Multiply.grid(row=3, column=4)

# --- additional operations --- #

btn_Expo = b.Button(calculator, text='x^y', command=lambda: update_enterField(btn_Expo))
btn_Root = b.Button(calculator, text='√', command=lambda: update_enterField(btn_Root))
btn_Factorial = b.Button(calculator, text='!', command=lambda: update_enterField(btn_Factorial))
btn_Percent = b.Button(calculator, text='%', command=lambda: update_enterField(btn_Percent))

btn_Expo.grid(row=2, column=6)
btn_Root.grid(row=2, column=7)
btn_Factorial.grid(row=3, column=6)
btn_Percent.grid(row=3, column=7)

# --- logaryphmic operations --- #

# btn_Log = b.Button(calculator, text='log_base(x)', command=log_b, row=2, col=8)
# btn_Log10 = b.Button(calculator, text='log_10(x)', command=lg, row=2, col=9)
# btn_Log2 = b.Button(calculator, text='log_2(x)', command=log_2, row=3, col=8)
# btn_Log1p = b.Button(calculator, text='ln(1+x)', command=ln, row=3, col=9)

window.mainloop()
