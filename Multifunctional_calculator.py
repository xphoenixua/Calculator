import tkinter as tk
from tkinter import messagebox
import Button as b
import math
from functools import partial
import re
import tkinter.ttk
 
# --- errors --- #

def err_Bracket():
    messagebox.showinfo('Input error', 'Check amount of brackets')

def err_Syntax():
    messagebox.showinfo('Input error', 'Check input expression')

def err_Complex():
    messagebox.showinfo('Calculation error', 'Underroot expression is negative')

def err_Zero():
    messagebox.showinfo('Calculation error', 'Zero division')

def err_Value():
    messagebox.showinfo('Calculation error', 'Value is out of range\n As ex. arc or log')

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
                err_Zero()
                return equ
            sum = float(nums[0]) / float(nums[1])
            new = str(sum)
            equ = equ.replace(old,new)
        else:
            flag = False
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
                comp_check = equ.replace(old,new)
                if re.search('[1]\.[0]\.', comp_check):
                    return equ
                equ = comp_check
                return equ
        else:
            flag = False
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
    return equ

def lg(string):
    equ = string
    flag = True
    while flag:
        is_right = re.search('lg_-?\d+\.?\d*', equ)
        if is_right:
            old = is_right.group()
            nums = old.split('lg_')
            try:
                sum = math.log10(float(nums[1]))
                new = str(sum)
                equ = equ.replace(old,new)
            except ValueError:
                err_Value()
                break
        else:
            flag = False
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
    return equ

def root(string):
    equ = string
    flag = True
    while flag:
        is_right = re.search('\d+\.?\d*\*{2}[\-]?[0]\.{1,}\d*', equ)
        not_right = re.search('[\-]\d+\.?\d*\*{2}[\-]?[0]\.{1,}\d*', equ)
        if not_right:
            err_Complex()
            return equ
        elif is_right:
            old = is_right.group()
            nums = old.split('**')
            sum = pow(float(nums[0]),float(nums[1]))
            new = str(sum)
            equ = equ.replace(old,new)
        else:
            flag = False
    return equ

def sin(string):
    equ = string
    flag = True
    while flag:
        is_right = re.search('sin\d+\.?\d*', equ)
        if is_right:
            old = is_right.group()
            nums = old.split('sin')
            sum = math.sin(float(nums[1]))
            new = str(sum)
            equ = equ.replace(old,new)
        else:
            flag = False
    return equ

def cos(string):
    equ = string
    flag = True
    while flag:
        is_right = re.search('cos\d+\.?\d*', equ)
        if is_right:
            old = is_right.group()
            nums = old.split('cos')
            sum = math.cos(float(nums[1]))
            new = str(sum)
            equ = equ.replace(old,new)
        else:
            flag = False
    return equ

def tg(string):
    equ = string
    flag = True
    while flag:
        is_right = re.search('tg\d+\.?\d*', equ)
        if is_right:
            old = is_right.group()
            nums = old.split('tg')
            sum = math.tan(float(nums[1]))
            new = str(sum)
            equ = equ.replace(old,new)
        else:
            flag = False
    return equ

def ctg(string):
    equ = string
    flag = True
    while flag:
        is_right = re.search('ctg\d+\.?\d*', equ)
        if is_right:
            old = is_right.group()
            nums = old.split('ctg')
            sum = 1/math.tan(float(nums[1]))
            new = str(sum)
            equ = equ.replace(old,new)
        else:
            flag = False
    return equ

def arcsin(string):
    equ = string
    flag = True
    while flag:
        is_right = re.search('arcsin\d+\.?\d*', equ)
        if is_right:
            old = is_right.group()
            nums = old.split('arcsin')
            try:
                sum = math.asin(float(nums[1]))
                new = str(sum)
                equ = equ.replace(old,new)
            except ValueError:
                err_Value()
                break
        else:
            flag = False
    return equ

def arccos(string):
    equ = string
    flag = True
    while flag:
        is_right = re.search('arccos\d+\.?\d*', equ)
        if is_right:
            old = is_right.group()
            nums = old.split('arccos')
            try:
                sum = math.acos(float(nums[1]))
                new = str(sum)
                equ = equ.replace(old,new)
            except ValueError:
                err_Value()
                break
        else:
            flag = False
    return equ

def arctg(string):
    equ = string
    flag = True
    while flag:
        is_right = re.search('arctg\d+\.?\d*', equ)
        if is_right:
            old = is_right.group()
            nums = old.split('arctg')
            try:
                sum = math.atan(float(nums[1]))
                new = str(sum)
                equ = equ.replace(old,new)
            except ValueError:
                err_Value()
                break
        else:
            flag = False
    return equ

def arcctg(string):
    equ = string
    flag = True
    while flag:
        is_right = re.search('arcctg\d+\.?\d*', equ)
        if is_right:
            old = is_right.group()
            nums = old.split('arcctg')
            try:
                sum = 1/math.atan(float(nums[1]))
                new = str(sum)
                equ = equ.replace(old,new)
            except ValueError:
                err_Value()
                break
        else:
            flag = False
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

            new = divide(new)
            new = multiply(new)
            new = add(new)
            new = subtract(new)

            new = root(new)
            new = expo(new)
            new = factorial(new)
            new = percentage(new)

            new = lg(new)
            new = ln(new)
            new = log2(new)
            
            new = arcsin(new)
            new = arccos(new)
            new = arcctg(new)
            new = arctg(new)

            new = sin(new)
            new = cos(new)
            new = ctg(new)
            new = tg(new)

            equ = equ.replace(old, new)
        else:
            flag = False
    else:
        equ = divide(equ)
        equ = multiply(equ)
        equ = add(equ)
        equ = subtract(equ)

        equ = root(equ)
        equ = expo(equ)
        equ = factorial(equ)
        equ = percentage(equ)
        
        equ = lg(equ)
        equ = ln(equ)
        equ = log2(equ)

        equ = arcsin(equ)
        equ = arccos(equ)
        equ = arcctg(equ)
        equ = arctg(equ)

        equ = sin(equ)
        equ = cos(equ)
        equ = ctg(equ)
        equ = tg(equ)
    return equ

def check(equ):
    equ = equ.replace(' ','')
    if len(re.findall('[^0-9\-+/*\(\).!%logn_csntiar]', equ)):
            err_Syntax()
            return equ
    elif not equ.count('(') == equ.count(')'):
            err_Bracket()
            return equ
    else:
        equ = pri(equ)
        return equ

# --- Entry() --- #

calc_history=[]
history = 'calculation_history.txt'
external = 'external.txt'

def calculation():
    equ = enterField.get()[::]
    calc_history.append(equ)
    equ = check(equ)
    calc_history.append(equ)
    calc_history.append('\n')
    if enterField.get()[::]==equ:
        err_Syntax()
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
    
    # --- trigonometry --- #
    elif clicked_button == btn_Sin:
        if enterField.get() == '0':
            enterField.delete(0)
        updated_text = '(' + str(clicked_button.cget('text'))
        enterField.insert(tk.END, updated_text)
    
    elif clicked_button == btn_Arcsin:
        if enterField.get() == '0':
            enterField.delete(0)
        updated_text = '(' + str(clicked_button.cget('text'))
        enterField.insert(tk.END, updated_text)
    
    elif clicked_button == btn_Cos:
        if enterField.get() == '0':
            enterField.delete(0)
        updated_text = '(' + str(clicked_button.cget('text'))
        enterField.insert(tk.END, updated_text)
    
    elif clicked_button == btn_Arccos:
        if enterField.get() == '0':
            enterField.delete(0)
        updated_text = '(' + str(clicked_button.cget('text'))
        enterField.insert(tk.END, updated_text)
    
    elif clicked_button == btn_Tg:
        if enterField.get() == '0':
            enterField.delete(0)
        updated_text = '(' + str(clicked_button.cget('text'))
        enterField.insert(tk.END, updated_text)
    
    elif clicked_button == btn_Arctg:
        if enterField.get() == '0':
            enterField.delete(0)
        updated_text = '(' + str(clicked_button.cget('text'))
        enterField.insert(tk.END, updated_text)
    
    elif clicked_button == btn_Ctg:
        if enterField.get() == '0':
            enterField.delete(0)
        updated_text = '(' + str(clicked_button.cget('text'))
        enterField.insert(tk.END, updated_text)
    
    elif clicked_button == btn_Arcctg:
        if enterField.get() == '0':
            enterField.delete(0)
        updated_text = '(' + str(clicked_button.cget('text'))
        enterField.insert(tk.END, updated_text)

    # --- exceptions --- #

    elif clicked_button == btn_Dot and enterField.get() == '0':
        updated_text = str(clicked_button.cget('text'))
        enterField.insert(tk.END, updated_text)
    
    # --- math constants --- #
    
    elif clicked_button == btn_Pi:
        if enterField.get() == '0':
            enterField.delete(0)
        updated_text = str(math.pi)
        enterField.insert(tk.END, updated_text)

    elif clicked_button == btn_Ex:
        if enterField.get() == '0':
            enterField.delete(0)
        updated_text = str(math.e)
        enterField.insert(tk.END, updated_text)
    
    elif clicked_button == btn_Tau:
        if enterField.get() == '0':
            enterField.delete(0)
        updated_text = str(math.tau)
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

window=tk.Tk()
window.title('Багатофункціональний калькулятор')
window.geometry('850x550+400+300')
window.resizable(width='False', height='False')
calculator=tk.Frame(window)
calculator.grid()

# --- Menu ---#

def fact_perc():
    messagebox.showinfo('Syntax instruction', 
    'Values with % or ! put inside brackets:\n 4-(300%)\n 5*(3!)')
def logarithms():
    messagebox.showinfo('Syntax instruction', 
    "Logarithms already have bracket before\n so don't forget to close after:\n 9+6*(ln2.12)/8")
def trigonometric():
    messagebox.showinfo('Syntax instruction', 
    "Trigonometric functions already have bracket before\n so don't forget to close after:\n (arcsin9)/8+2*ctg(1)")

menu=tk.Menu(calculator)
instruction=tk.Menu(calculator, tearoff=False)

menu.add_cascade(label='Instruction', menu=instruction)
instruction.add_command(label='Factorial and percentage', command=lambda: fact_perc())
instruction.add_command(label='Logarithms', command=lambda: logarithms())
instruction.add_command(label='Trigonometric funcs', command=lambda: trigonometric())

menu.add_cascade(label='Exit', command=lambda: window.destroy())

window.config(menu=menu)

# --- enter field --- #

enterField = tk.Entry(calculator, justify=tk.RIGHT, width=45)
enterField.insert(0, '0')
enterField.grid(row=0, column=0, columnspan=7, pady=10)

btn_Backspace = tk.Button(calculator, text='<=', command=backspace)
btn_Backspace.grid(row=0, column=7, pady=1)

btn_Clear = tk.Button(calculator, text='C', command=clear_enterField, width=5)
btn_Clear.grid(row=1, column=7, pady=1)

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

# --- files --- #

def fileSave():
    calc_output=open(history, 'w', encoding='utf-8')
    for line in calc_history:
        calc_output.write(line+'\n')
    calc_output.close()

def fileRead():
    calc_input=open(external, 'r', encoding='utf-8')
    expression=calc_input.readline()
    if enterField.get() == '0':
            enterField.delete(0)
    enterField.insert(tk.END,expression)

btn_fileSave = tk.Button(calculator, text='Save calculation\n history', command=lambda: fileSave(), width=15)
btn_fileSave.grid(row=6, column=0, columnspan=3)

btn_fileRead = tk.Button(calculator, text='Read external.txt\n expression', command=lambda: fileRead(), width=15)
btn_fileRead.grid(row=6, column=3, columnspan=3)

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

tkinter.ttk.Separator(calculator, orient=tk.VERTICAL).grid(row=0, column=10, rowspan=8, sticky='ns', padx=10)

# --- math constants --- #

lbl_mConst = tk.Label(calculator, text = 'Math constants')
lbl_mConst.grid(row=1, column=11)

btn_Pi = tk.Button(calculator, text='pi', command=lambda: update_enterField(btn_Pi), width=15)
btn_Ex = tk.Button(calculator, text='e', command=lambda: update_enterField(btn_Ex), width=15)
btn_Tau = tk.Button(calculator, text='tau', command=lambda: update_enterField(btn_Tau), width=15)

btn_Pi.grid(row=2, column=11, pady=10)
btn_Ex.grid(row=3, column=11, pady=10)
btn_Tau.grid(row=4, column=11, pady=10)

#tkinter.ttk.Separator(calculator, orient=tk.VERTICAL).grid(row=0, column=12, rowspan=8, sticky='ns')

# --- physical constants --- #

lbl_pConst = tk.Label(calculator, text = 'Physic constants')
lbl_pConst.grid(row=1, column=12, padx=25)

btn_R = tk.Button(calculator, text='R [gas const, J/(mol*K)]', command=lambda: update_enterField(btn_R), width=20)
btn_C = tk.Button(calculator, text='c [light velocity, m/s]', command=lambda: update_enterField(btn_C), width=20)
btn_N = tk.Button(calculator, text='N [Avogadro const, 1/mol]', command=lambda: update_enterField(btn_N), width=20)
btn_K = tk.Button(calculator, text='k [Boltzmann const, J/K]', command=lambda: update_enterField(btn_K), width=20)
btn_H = tk.Button(calculator, text='h [Planck const, eV/s]', command=lambda: update_enterField(btn_H), width=20)

btn_R.grid(row=2, column=12, columnspan=2, padx=5)
btn_C.grid(row=3, column=12, columnspan=2)
btn_N.grid(row=4, column=12, columnspan=2)
btn_K.grid(row=5, column=12, columnspan=2)
btn_H.grid(row=6, column=12, columnspan=2)

# --- constant funcs --- #

def const_Add():
    const=enterField.get()
    lst_const.insert(tk.END, const)

def const_Delete():
    const_selection=lst_const.curselection()
    lst_const.delete(const_selection[0])

# --- constants list --- #

lbl_nConst = tk.Label(calculator, text='Own constants')
lbl_nConst.grid(row=8, column=11, columnspan=2)

lst_const = tk.Listbox(calculator, width=40)
lst_const.grid(row=9, column=10, columnspan=5, rowspan=4)

btn_addConst = tk.Button(calculator, text='Add const',command=const_Add)
btn_addConst.grid(row=13, column=11, padx=5)

btn_addConst = tk.Button(calculator, text='Delete const',command=const_Delete)
btn_addConst.grid(row=13, column=12, padx=10)

# --- Statistic operations --- #

def statSum():
    values=enterField_st.get()
    values_lst=values.split(',')
    values_lst=[float(x) for x in values_lst]
    values_sum=sum(values_lst)
    enterField_st.delete(0,tk.END)
    enterField_st.insert(tk.END,values_sum)

def statAvg():
    values=enterField_st.get()
    values_lst=values.split(',')
    values_lst=[float(x) for x in values_lst]
    values_avg=sum(values_lst)/len(values_lst)
    enterField_st.delete(0,tk.END)
    enterField_st.insert(tk.END,values_avg)

lbl_Stat = tk.Label(calculator, text='Statistics calculation')
lbl_Stat.grid(row=4, column=6, columnspan=4)

enterField_st = tk.Entry(calculator)
enterField_st.grid(row=5, column=6, columnspan=4)

btn_Sum = tk.Button(calculator, text='Sum',command=statSum)
btn_Sum.grid(row=6, column=6, columnspan=3, padx=5)

btn_Avg = tk.Button(calculator, text='Avg',command=statAvg)
btn_Avg.grid(row=6, column=7, columnspan=3, padx=5)

# --- trigonometry --- #

lbl_Trig = tk.Label(calculator, text='Trigonometry')
lbl_Trig.grid(row=9, column=0, columnspan=3, pady=10)

btn_Sin = b.Button(calculator, text='sin', command=lambda: update_enterField(btn_Sin))
btn_Arcsin = b.Button(calculator, text='arcsin', command=lambda: update_enterField(btn_Arcsin))
btn_Cos = b.Button(calculator, text='cos', command=lambda: update_enterField(btn_Cos))
btn_Arccos = b.Button(calculator, text='arccos', command=lambda: update_enterField(btn_Arccos))

btn_Sin.grid(row=10, column=0, columnspan=2)
btn_Arcsin.grid(row=10, column=1, columnspan=2)
btn_Cos.grid(row=11, column=0, columnspan=2)
btn_Arccos.grid(row=11, column=1, columnspan=2)

btn_Tg = b.Button(calculator, text='tg', command=lambda: update_enterField(btn_Tg))
btn_Arctg = b.Button(calculator, text='arctg', command=lambda: update_enterField(btn_Arctg))
btn_Ctg = b.Button(calculator, text='ctg', command=lambda: update_enterField(btn_Ctg))
btn_Arcctg = b.Button(calculator, text='arcctg', command=lambda: update_enterField(btn_Arcctg))

btn_Tg.grid(row=12, column=0, columnspan=2)
btn_Arctg.grid(row=12, column=1, columnspan=2)
btn_Ctg.grid(row=13, column=0, columnspan=2)
btn_Arcctg.grid(row=13, column=1, columnspan=2)

# --- convertation to degrees --- #

def RadToDeg():
    rad=enterField_rad.get()
    deg=math.degrees(float(rad))
    if enterField.get() == '0':
            enterField.delete(0)
    enterField_deg.insert(tk.END,str(deg))
    enterField_rad.delete(0,tk.END)

lbl_Rad = tk.Label(calculator, text='Radians to Degrees')
lbl_Rad.grid(row=8, column=3, columnspan=3, pady=10)

enterField_rad = tk.Entry(calculator)
enterField_rad.grid(row=9, column=3, columnspan=3)

btn_Rad = tk.Button(calculator, text='Convert', command=RadToDeg, height=1)
btn_Rad.grid(row=10, column=3, columnspan=3)

# --- convertation to radians --- #

def DegToRad():
    deg=enterField_deg.get()
    rad=math.radians(float(deg))
    if enterField.get() == '0':
            enterField.delete(0)
    enterField_rad.insert(tk.END,str(rad))
    enterField_deg.delete(0,tk.END)

lbl_Deg = tk.Label(calculator, text='Degrees to Radians')
lbl_Deg.grid(row=8, column=7, columnspan=3, pady=10)

enterField_deg = tk.Entry(calculator)
enterField_deg.grid(row=9, column=7, columnspan=3)

btn_Deg = tk.Button(calculator, text='Convert', command=DegToRad, height=1)
btn_Deg.grid(row=10, column=7, columnspan=3)

# --- convertation to DD --- #

def get_args():
    values=enterField_dms.get()
    values_lst=values.split(',')
    values_lst=[float(x) for x in values_lst]
    d,m,s=values_lst[0],values_lst[1],values_lst[2]
    dms_to_dd(d,m,s)

def dms_to_dd(d,m,s):
    dd = d + float(m)/60 + float(s)/3600
    if enterField.get() == '0':
            enterField.delete(0)
    enterField_dd.insert(tk.END,str(dd))
    enterField_dms.delete(0,tk.END)

lbl_dms = tk.Label(calculator, text='DMS to Decimal Degrees')
lbl_dms.grid(row=11, column=3, columnspan=3, pady=10)

enterField_dms = tk.Entry(calculator)
enterField_dms.grid(row=12, column=3, columnspan=3)

btn_DMS = tk.Button(calculator, text='Convert', command=get_args, height=1)
btn_DMS.grid(row=13, column=3, columnspan=3)

# --- convertation to DMS --- #

def dd_to_dms():
    dd=enterField_dd.get()
    m,s=divmod(float(dd)*3600,60)
    d,m=divmod(m,60)
    if enterField.get() == '0':
            enterField.delete(0)
    enterField_dms.insert(tk.END,str(d)+','+str(m)+','+str(s))
    enterField_dd.delete(0,tk.END)

lbl_DD = tk.Label(calculator, text='DD to Degrees, Minutes, Seconds')
lbl_DD.grid(row=11, column=7, columnspan=3, pady=10)

enterField_dd = tk.Entry(calculator)
enterField_dd.grid(row=12, column=7, columnspan=3)

btn_DD = tk.Button(calculator, text='Convert', command=dd_to_dms, height=1)
btn_DD.grid(row=13, column=7, columnspan=3)

window.mainloop()