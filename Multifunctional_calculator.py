import tkinter as tk
import Button as b
import math
from functools import partial
import re
import tkinter.ttk
 
# --- operations --- #

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
            if int(nums[1])<1 and int(nums[1])>0:
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

# --- parsing --- #

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
        equ = factorial(equ)
        equ = percentage(equ)
        
        equ = lg(equ)
        equ = ln(equ)
        equ = log2(equ)

    return equ

def check(equ):
    equ = equ.replace(' ','')
    if len(re.findall('[^0-9\-+/*\(\).!%elogn_]', equ)):
            print ("Невірне введення виразу")
    elif not equ.count('(') == equ.count(')'):
            print ("Непарна кількість дужок у виразі")
    else:
        equ = pri(equ)
        print(equ)
        return equ

# --- Entry() --- #

def calculation():
    equ = enterField.get()[::]
    print(equ, 'equ - before insert')
    equ = check(equ)
    print(equ, 'equ - insert')
    enterField.delete(0,tk.END)
    enterField.insert(0,equ)

def backspace():
    back_var = enterField.get()[:-1]
    enterField.delete(0,tk.END)
    enterField.insert(0,back_var)
    if back_var == '':
        enterField.insert(0,'0')

def clear_enterField():
    enterField.delete(0,tk.END)
    enterField.insert(0, '0')

# --- Memory operations --- #

def m_Save():
    global memory_s
    memory_s=enterField.get()

def m_Read():
    global memory_s
    memory_s=check(memory_s)
    if enterField.get() == '0':
            enterField.delete(0)
    enterField.insert(tk.END,memory_s)

def m_Clear():
    global memory_s
    memory_s=''

def m_Plus():
    global memory_s
    memory_s+='+' + check(enterField.get())
    memory_s=check(memory_s)

def m_Minus():
    global memory_s
    memory_s+='-' + check(enterField.get())
    memory_s=check(memory_s)

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
    
    # --- math constants --- #
    
    elif clicked_button == btn_Pi:
        if enterField.get() == '0':
            enterField.delete(0)
        updated_text = '3.1415926535'
        enterField.insert(tk.END, updated_text)

    elif clicked_button == btn_Ex:
        if enterField.get() == '0':
            enterField.delete(0)
        updated_text = '2.71828182'
        enterField.insert(tk.END, updated_text)
    
    # --- physical constants --- #

    elif clicked_button == btn_R:
        if enterField.get() == '0':
            enterField.delete(0)
        updated_text = '8.314462618'
        enterField.insert(tk.END, updated_text)
    elif clicked_button == btn_C:
            if enterField.get() == '0':
                enterField.delete(0)
            updated_text = '2.99792458*(10**8)'
            enterField.insert(tk.END, updated_text)
    elif clicked_button == btn_N:
            if enterField.get() == '0':
                enterField.delete(0)
            updated_text = '6.02214076*(10**23)'
            enterField.insert(tk.END, updated_text)
    elif clicked_button == btn_K:
            if enterField.get() == '0':
                enterField.delete(0)
            updated_text = '1.380649*(10**-23)'
            enterField.insert(tk.END, updated_text)
    elif clicked_button == btn_H:
            if enterField.get() == '0':
                enterField.delete(0)
            updated_text = '4.135667696*(10**-15)'
            enterField.insert(tk.END, updated_text)

    # --- process --- #

    else:
        if enterField.get() == '0':
            enterField.delete(0)
        updated_text = str(clicked_button.cget('text'))
        enterField.insert(tk.END, updated_text)
    
# --- Structure --- #

window = tk.Tk()
window.title('Багатофункціональний калькулятор')
window.geometry('880x500+400+300')
window.resizable(width='False', height='False')
calculator = tk.Frame(window)
calculator.grid()

# --- enter field --- #

enterField = tk.Entry(calculator, justify=tk.RIGHT, width=45)
enterField.insert(0, '0')
enterField.grid(row=0, column=0, columnspan=7, pady=10)

btn_Backspace = tk.Button(calculator, text='<=', command=backspace, background='#f0a818')
btn_Backspace.grid(row=0, column=7, pady=1)

btn_Backspace = tk.Button(calculator, text='C', command=clear_enterField, background='#de442c', width=5)
btn_Backspace.grid(row=0, column=8, columnspan=2, pady=1)

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

btn_Zero = tk.Button(calculator, text='0', command=lambda: update_enterField(btn_Zero), width=12)
btn_Zero.grid(row=5, column=0, columnspan=2)

btn_Dot = tk.Button(calculator, text='.', command=lambda: update_enterField(btn_Dot), width=6)
btn_Dot.grid(row=5, column=2)

btn_Equal = tk.Button(calculator, text='=', width=12, height=2, command=calculation)
btn_Equal.grid(row=4, column=3, columnspan=2)

btn_BrLeft = tk.Button(calculator, text='(', command=lambda: update_enterField(btn_BrLeft), width=6)
btn_BrLeft.grid(row=5, column=3)

btn_BrRight = tk.Button(calculator, text=')', command=lambda: update_enterField(btn_BrRight), width=6)
btn_BrRight.grid(row=5, column=4)

# --- Memory buttons --- #

btn_MemoSave = tk.Button(calculator, text='MS', command=m_Save)
btn_MemoSave.grid(row=1, column=0, pady=1)

btn_MemoRead = tk.Button(calculator, text='MR', command=m_Read)
btn_MemoRead.grid(row=1, column=1, pady=1)

btn_MemoClear = tk.Button(calculator, text='MC', command=m_Clear)
btn_MemoClear.grid(row=1, column=2, pady=1)

btn_MemoPlus = tk.Button(calculator, text='M+', command=m_Plus)
btn_MemoPlus.grid(row=1, column=3, pady=1, padx=10)

btn_MemoMinus = tk.Button(calculator, text='M-', command=m_Minus)
btn_MemoMinus.grid(row=1, column=4, pady=1, padx=10)


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

btn_Log = b.Button(calculator, text='log_b(a)',)
btn_Lg = b.Button(calculator, text='lg', command=lambda: update_enterField(btn_Lg))
btn_Log2 = b.Button(calculator, text='log2', command=lambda: update_enterField(btn_Log2))
btn_Ln = b.Button(calculator, text='ln', command=lambda: update_enterField(btn_Ln))

btn_Log.grid(row=3, column=8)
btn_Lg.grid(row=2, column=9)
btn_Log2.grid(row=2, column=8)
btn_Ln.grid(row=3, column=9)

tkinter.ttk.Separator(calculator, orient=tk.VERTICAL).grid(row=0, column=10, rowspan=8, sticky='ns')

# --- math constants --- #

lbl_Const = tk.Label(calculator, text = 'Math constants')
lbl_Const.grid(row=1, column=11, columnspan=2)

frm_Blank = tk.Frame(calculator, width=50)
frm_Blank.grid(row=2, column=10)

btn_Pi = tk.Button(calculator, text='pi', command=lambda: update_enterField(btn_Pi), width=15)
btn_Ex = tk.Button(calculator, text='e', command=lambda: update_enterField(btn_Ex), width=15)

btn_Pi.grid(row=2, column=11, columnspan=2, pady=10)
btn_Ex.grid(row=3, column=11, columnspan=2, pady=10)

tkinter.ttk.Separator(calculator, orient=tk.VERTICAL).grid(row=0, column=13, rowspan=8, sticky='ns')

# --- physical constants --- #

lbl_Const = tk.Label(calculator, text = 'Physic constants')
lbl_Const.grid(row=1, column=14, columnspan=2)

btn_R = tk.Button(calculator, text='R [gas const, J/(mol*K)]', command=lambda: update_enterField(btn_R), width=20)
btn_C = tk.Button(calculator, text='c [light velocity, m/s]', command=lambda: update_enterField(btn_C), width=20)
btn_N = tk.Button(calculator, text='N [Avogadro const, 1/mol]', command=lambda: update_enterField(btn_N), width=20)
btn_K = tk.Button(calculator, text='k [Boltzmann const, J/K]', command=lambda: update_enterField(btn_K), width=20)
btn_H = tk.Button(calculator, text='h [Planck const, eV/s]', command=lambda: update_enterField(btn_H), width=20)

btn_R.grid(row=2, column=14, columnspan=2, pady=10)
btn_C.grid(row=3, column=14, columnspan=2, pady=10)
btn_N.grid(row=4, column=14, columnspan=2, pady=10)
btn_K.grid(row=5, column=14, columnspan=2, pady=10)
btn_H.grid(row=6, column=14, columnspan=2, pady=10)

# --- constant funcs --- #

def const_Add():
    const=enterField.get()
    lst_const.insert(tk.END, const)

def const_Delete():
    const_selection=lst_const.curselection()
    lst_const.delete(const_selection[0])

# --- constants list --- #

lst_const = tk.Listbox(calculator, width=40)
lst_const.grid(row=10, column=10, columnspan=5)

btn_addConst = tk.Button(calculator, text="Add const",command=const_Add)
btn_addConst.grid(row=11, column=11, padx=5, pady=10)

btn_addConst = tk.Button(calculator, text="Delete const",command=const_Delete)
btn_addConst.grid(row=11, column=13, padx=5)

window.mainloop()