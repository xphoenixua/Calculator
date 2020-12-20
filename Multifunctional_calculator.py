import tkinter as tk
import Button as b
import math
from functools import partial
import re
 
def add(string):
    equ = string
    flag = True
    while flag:
        is_right = re.search('[\-]?\d+\.?\d*\+[\-]?\d+\.?\d*', equ)
        if is_right:
            old = is_right.group()
            nums = old.split('+')
            sum = float(nums[0]) + float(nums[1])
            new = str(sum)
            equ = equ.replace(old,new)
        else:
            flag = False
    print(equ, 'equ add')
    return equ 
 
def subtract(string):
    equ = string
    flag = True
    while flag:
        is_right = re.search('[\-]?\d+\.?\d*-[\-]?\d+\.?\d*', equ)
        if is_right:
            old = is_right.group()
            count = len(re.findall('-',old))
            if count==1:
                nums = old.split('-')
                sum = float(nums[0]) - float(nums[1])
                new = str(sum)
                equ = equ.replace(old, new)
            elif count==2:
                nums = old.split('-')
                sum = - float(nums[1]) - float(nums[2])
                new = str(sum)
                equ = equ.replace(old, new)
        else:
            flag = False
    print(equ, 'equ minus')
    return equ
 
def multiply(string):
    equ = string
    flag = True
    while flag:
        is_right = re.search('[\-]?\d+\.?\d*\*[\-]?\d+\.?\d*', equ)
        if is_right:
            old = is_right.group()
            nums = old.split('*')
            sum = float(nums[0]) * float(nums[1])
            new = str(sum)
            equ = equ.replace(old,new)
        else:
            flag = False
    print(equ, 'equ mult')
    return equ
 
def divide(string):
    equ = string
    flag = True
    while flag:
        is_right = re.search('[\-]?\d+\.?\d*/[\-]?\d+\.?\d*', equ)
        if is_right:
            old = is_right.group()
            nums = old.split('/')
            if nums[1] == '0':
                exit('ділення на 0')
            sum = float(nums[0]) / float(nums[1])
            new = str(sum)
            equ = equ.replace(old,new)
        else:
            flag = False
    print(equ, 'equ div')
    return equ
 
def expo(string):
    equ = string
    flag = True
    while flag:
        is_right = re.search('[\-]?\d+\.?\d*\*{2}[\-]?\d+', equ)
        if is_right:
            old = is_right.group()
            nums = old.split('**')
            if float(nums[1])<1:
                break
            else:
                sum = pow(float(nums[0]),int(nums[1]))
                new = str(sum)
                equ = equ.replace(old,new)
        else:
            flag = False
    print(equ, 'equ expo')
    return equ

def factorial(string):
    equ = string
    flag = True
    while flag:
        is_right = re.search('\d+\!', equ)
        if is_right:
            old = is_right.group()
            nums = old.split('!')
            sum = math.factorial(int(nums[0]))
            new = str(sum)
            equ = equ.replace(old,new)
        else:
            flag = False
    print(equ, 'equ fact')
    return equ

def lg(string):
    equ = string
    flag = True
    while flag:
        is_right = re.search('lg_\d+\.?\d*', equ)
        if is_right:
            old = is_right.group()
            nums = old.split('lg_')
            sum = math.log10(float(nums[1]))
            new = str(sum)
            equ = equ.replace(old,new)
        else:
            flag = False
    print(equ, 'equ lg')
    return equ

def ln(string):
    equ = string
    flag = True
    while flag:
        is_right = re.search('ln_\d+\.?\d*', equ)
        if is_right:
            old = is_right.group()
            nums = old.split('ln_')
            sum = math.log1p(float(nums[1])-1)
            new = str(sum)
            equ = equ.replace(old,new)
        else:
            flag = False
    print(equ, 'equ ln')
    return equ

def log2(string):
    equ = string
    flag = True
    while flag:
        is_right = re.search('log2_\d+\.?\d*', equ)
        if is_right:
            old = is_right.group()
            nums = old.split('log2_')
            sum = math.log2(float(nums[1]))
            new = str(sum)
            equ = equ.replace(old,new)
        else:
            flag = False
    print(equ, 'equ log2_')
    return equ

def percentage(string):
    equ = string
    flag = True
    while flag:
        is_right = re.search('\d+\.?\d*\%', equ)
        if is_right:
            old = is_right.group()
            nums = old.split('%')
            sum = float(nums[0])/100
            new = str(sum)
            equ = equ.replace(old,new)
        else:
            flag = False
    print(equ, 'equ perc')
    return equ

def root(string):
    equ = string
    flag = True
    while flag:
        is_right = re.search('\d+\.?\d*\*{2}[\-]?[0]\.{1,}\d*', equ)
        not_right = re.search('[\-]?\d+\.?\d*\*{2}[\-]?[0]\.{1,}\d*', equ)
        if is_right:
            old = is_right.group()
            nums = old.split('**')
            print(nums)
            sum = pow(float(nums[0]),float(nums[1]))
            new = str(sum)
            equ = equ.replace(old,new)
        elif not_right:
            print('Під коренем від’ємне число')
        else:
            flag = False
    print(equ, 'equ root')
    return equ

def pri(equ):
    flag = True
    while flag:
        ret = re.search('\([^()]+\)', equ)
        if ret:
            old = ret.group()

            new = old.replace('(', '')
            new = new.replace(')', '')

            new = multiply(new)
            new = divide(new)
            new = add(new)
            new = subtract(new)

            new = root(new)
            new = expo(new)
            new = factorial(new)
            new = percentage(new)

            new = lg(new)
            new = ln(new)
            new = log2(new)

            equ = equ.replace(old, new)
        else:
            flag = False
    else:
        equ = multiply(equ)
        equ = divide(equ)
        equ = add(equ)
        equ = subtract(equ)

        equ = expo(equ)
        equ = root(equ)
        equ = factorial(equ)
        equ = percentage(equ)
        
        equ = lg(equ)
        equ = ln(equ)
        equ = log2(equ)

    return equ

def check(equ):
    equ = equ.replace(' ','')
    if len(re.findall('[^0-9\-+/*\(\).!%logn_]', equ)):
            print ("Невірне введення виразу")
    elif not equ.count('(') == equ.count(')'):
            print ("Непарна кількість дужок у виразі")
    else:
        equ = pri(equ)
        print(equ)
        return equ

def calculation():
    equ = enterField.get()[::]
    print(equ, 'equ - before insert')
    equ = check(equ)
    print(equ, 'equ - insert')
    enterField.delete(0,tk.END)
    enterField.insert(0,equ)

def update_enterField(clicked_button):

    # --- logarithyms --- #

    if clicked_button == btn_Log2:
        if enterField.get() == '0':
            enterField.delete(0)
        updated_text = '(' + str(clicked_button.cget('text')) + '_'
        enterField.insert(tk.END, updated_text)

    elif clicked_button == btn_Ln:
        if enterField.get() == '0':
            enterField.delete(0)
        updated_text = '(' + str(clicked_button.cget('text')) + '_'
        enterField.insert(tk.END, updated_text)

    elif clicked_button == btn_Lg:
        if enterField.get() == '0':
            enterField.delete(0)
        updated_text = '(' + str(clicked_button.cget('text')) + '_'
        enterField.insert(tk.END, updated_text)
    
    # --- exceptions --- #

    elif clicked_button == btn_Dot and enterField.get() == '0':
        updated_text = str(clicked_button.cget('text'))
        enterField.insert(tk.END, updated_text)
    
    # --- constants --- #
    
    elif clicked_button == btn_Pi:
        if enterField.get() == '0':
            enterField.delete(0)
        updated_text = '3.141'
        enterField.insert(tk.END, updated_text)

    elif clicked_button == btn_Ex:
        if enterField.get() == '0':
            enterField.delete(0)
        updated_text = '2.718'
        enterField.insert(tk.END, updated_text)





    # --- process --- #

    else:
        updated_text = str(clicked_button.cget('text'))
        enterField.insert(tk.END, updated_text)
    
def backspace():
    back_var = enterField.get()[:-1]
    enterField.delete(0,tk.END)
    enterField.insert(0,back_var)
    if back_var == '':
        enterField.insert(0,'0')

def clear_enterField():
    enterField.delete(0,tk.END)
    enterField.insert(0, '0')

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

btn_Dot = tk.Button(calculator, text='.', command=lambda: update_enterField(btn_Dot), width=6, height=1)
btn_Dot.grid(row=5, column=2)

btn_Equal = tk.Button(calculator, text='=', width=12, height=2, command=calculation)
btn_Equal.grid(row=4, column=3, columnspan=2)

btn_BrLeft = tk.Button(calculator, text='(', command=lambda: update_enterField(btn_BrLeft), width=6, height=1)
btn_BrLeft.grid(row=5, column=3)

btn_BrRight = tk.Button(calculator, text=')', command=lambda: update_enterField(btn_BrRight), width=6, height=1)
btn_BrRight.grid(row=5, column=4)

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

btn_Factorial = b.Button(calculator, text='!', command=lambda: update_enterField(btn_Factorial))
btn_Percent = b.Button(calculator, text='%', command=lambda: update_enterField(btn_Percent))

btn_Percent.grid(row=2, column=6)
btn_Factorial.grid(row=3, column=6)


# --- logaryphmic operations --- #

lbl_Const = tk.Label(calculator, text = 'Logarithms')
lbl_Const.grid(row=1, column=8, columnspan=2)

frm_Blank = tk.Frame(calculator, width=35)
frm_Blank.grid(row=2, column=7)

# btn_Log = b.Button(calculator, text='log_base(x)', command=log_b, row=2, col=8)
btn_Lg = b.Button(calculator, text='lg', command=lambda: update_enterField(btn_Lg))
btn_Log2 = b.Button(calculator, text='log2', command=lambda: update_enterField(btn_Log2))
btn_Ln = b.Button(calculator, text='ln', command=lambda: update_enterField(btn_Ln))

# btn_Log.grid(row=2, column=6)
btn_Lg.grid(row=2, column=9)
btn_Log2.grid(row=2, column=8)
btn_Ln.grid(row=3, column=9)


# --- math constants --- #

lbl_Const = tk.Label(calculator, text = 'Math constants')
lbl_Const.grid(row=1, column=11, columnspan=2)

frm_Blank = tk.Frame(calculator, width=35)
frm_Blank.grid(row=2, column=10)

btn_Pi = b.Button(calculator, text='pi', command=lambda: update_enterField(btn_Pi))
btn_Ex = b.Button(calculator, text='e', command=lambda: update_enterField(btn_Ex))

btn_Pi.grid(row=2, column=11)
btn_Ex.grid(row=2, column=12)


# --- physics constants --- #

lbl_Const = tk.Label(calculator, text = 'Physic constants')
lbl_Const.grid(row=1, column=14, columnspan=2)

frm_Blank = tk.Frame(calculator, width=35)
frm_Blank.grid(row=2, column=13)

btn_Tr = b.Button(calculator, text='tr', command=lambda: update_enterField(btn_Tr))
btn_Td = b.Button(calculator, text='td', command=lambda: update_enterField(btn_Td))

btn_Tr.grid(row=2, column=14)
btn_Td.grid(row=2, column=15)

window.mainloop()