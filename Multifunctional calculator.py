import tkinter as tk
import Button as b

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

# --- NumPad --- #

numberPad = [7, 8, 9, 4, 5, 6, 1, 2, 3]
num = 0
btn = []
for i in range(2, 5):
    for j in range(3):
        btn.append(tk.Button(calculator, text='{}'.format(numberPad[num]), width=6, height=2))
        btn[num].grid(row=i, column=j, pady=1)
        num += 1

# --- misc --- #

btn_Zero = tk.Button(calculator, text='0', width=12, height=1)
btn_Zero.grid(row=5, column=0, columnspan=2)

btn_Comma = tk.Button(calculator, text=',', width=6, height=1)
btn_Comma.grid(row=5, column=2)

btn_Equal = tk.Button(calculator, text='=', width=12, height=2)
btn_Equal.grid(row=4, column=3, columnspan=2)

# --- Memory buttons --- #

btn_MemoSave = tk.Button(calculator, text='MS', )
btn_MemoSave.grid(row=1, column=0, pady=1)

btn_MemoRead = tk.Button(calculator, text='MR', )
btn_MemoRead.grid(row=1, column=1, pady=1)

btn_MemoClear = tk.Button(calculator, text='MC', )
btn_MemoClear.grid(row=1, column=2, pady=1)

btn_MemoAdd = tk.Button(calculator, text='M+', )
btn_MemoAdd.grid(row=1, column=3, pady=1, padx=10)

btn_MemoSubtract = tk.Button(calculator, text='M-', )
btn_MemoSubtract.grid(row=1, column=4, pady=1, padx=10)


# --- operations' functions --- #

def plus():
    print('+')

def minus():
    print('-')

def divide():
    print('/')

def multiply():
    print('*')

def expo():
    print('x^y')

def root():
    print('√')

def factorial():
    print('!')

def percent():
    print('%')

def log_b():
    print('1')

def lg():
    print('2')

def log_2():
    print('3')

def ln():
    print('4')

# --- operations' dictionary --- #

operations = {
    '+': plus,
    '-': minus,
    '*': multiply,
    '/': divide,
    'x^y': expo,
    '√': root,
    '!': factorial,
    '%': percent,
    'log_base(x)': log_b,
    'log_10': lg,
    'log_2': log_2,
    'ln(1+x)': ln,
}

# --- simple operations --- #

btn_Add = b.Button(calculator, text='+', command=plus, row=2, col=3)
btn_Subtract = b.Button(calculator, text='-', command=minus, row=2, col=4)
btn_Divide = b.Button(calculator, text='/', command=divide, row=3, col=3)
btn_Multiply = b.Button(calculator, text='*', command=multiply, row=3, col=4)

# --- additional operations --- #

btn_Expo = b.Button(calculator, text='x^y', command=expo, row=2, col=6)
btn_Root = b.Button(calculator, text='√', command=root, row=2, col=7)
btn_Factorial = b.Button(calculator, text='!', command=factorial, row=3, col=6)
btn_Percent = b.Button(calculator, text='%', command=percent, row=3, col=7)

# --- logaryphmic operations --- #

btn_Log = b.Button(calculator, text='log_base(x)', command=log_b, row=2, col=8)
btn_Log10 = b.Button(calculator, text='log_10(x)', command=lg, row=2, col=9)
btn_Log2 = b.Button(calculator, text='log_2(x)', command=log_2, row=3, col=8)
btn_Log1p = b.Button(calculator, text='ln(1+x)', command=ln, row=3, col=9)

window.mainloop()