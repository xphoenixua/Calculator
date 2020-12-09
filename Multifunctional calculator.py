from tkinter import *
import math
window = Tk()
window.title('Багатофункціональний калькулятор')
window.geometry('800x500')
window.resizable(width = 'False', height = 'False')
calculator = Frame(window)
calculator.grid()



enterField = Entry(calculator, justify = RIGHT)
enterField.insert(0, '0')
enterField.grid(row = 0, column = 0, columnspan = 4, pady = 10)

d

numberPad = [7,8,9,4,5,6,1,2,3]
num = 0
btn = []
for i in range(2,5):
    for j in range(3):
        btn.append(Button(calculator, text='{}'.format(numberPad[num]), width = 6, height = 2))
        btn[num].grid(row = i, column = j, pady = 1)
        num+=1

btn_Zero = Button(calculator, text = '0', width = 12, height = 1)
btn_Zero.grid(row = 5, column = 0, columnspan = 2)

btn_Comma = Button(calculator, text = ',', width = 6, height = 1)
btn_Comma.grid(row = 5, column = 2)

btn_Equal = Button(calculator, text = '=', width = 12, height = 2)
btn_Equal.grid(row = 4, column = 3, columnspan = 2)



btn_MemoSave = Button(calculator, text = 'MS', )
btn_MemoSave.grid(row = 1, column = 0, pady = 1)

btn_MemoRead = Button(calculator, text = 'MR', )
btn_MemoRead.grid(row = 1, column = 1, pady = 1)

btn_MemoClear = Button(calculator, text = 'MC', )
btn_MemoClear.grid(row = 1, column = 2, pady = 1)

btn_MemoAdd = Button(calculator, text = 'M+', )
btn_MemoAdd.grid(row = 1, column = 3, pady = 1, padx = 10)

btn_MemoSubtract = Button(calculator, text = 'M-', )
btn_MemoSubtract.grid(row = 1, column = 4, pady = 1, padx = 10)



btn_Add = Button(calculator, text = '+', width = 6, height = 2)
btn_Add.grid(row = 2, column = 3)

btn_Subtract = Button(calculator, text = '-', width = 6, height = 2)
btn_Subtract.grid(row = 2, column = 4)

btn_Multiply = Button(calculator, text = '*', width = 6, height = 2)
btn_Multiply.grid(row = 3, column = 3)

btn_Divide = Button(calculator, text = '/', width = 6, height = 2)
btn_Divide.grid(row = 3, column = 4)



btn_Expo = Button(calculator, text = 'x^y', width = 6, height = 2)
btn_Expo.grid(row = 2, column = 5)

btn_Root = Button(calculator, text = '√', width = 6, height = 2)
btn_Root.grid(row = 2, column = 6)

btn_Factorial = Button(calculator, text = '!', width = 6, height = 2)
btn_Factorial.grid(row = 3, column = 5)

btn_Percents = Button(calculator, text = '%', width = 6, height = 2)
btn_Percents.grid(row = 3, column = 6)



btn_Log = Button(calculator, text = 'log_base(x)', width = 6, height = 2)
btn_Expo.grid(row = 4, column = 5)

btn_Log2 = Button(calculator, text = 'log_2(x)', width = 6, height = 2)
btn_Root.grid(row = 5, column = 6)

btn_Log10 = Button(calculator, text = 'log_10(x)', width = 6, height = 2)
btn_Factorial.grid(row = 4, column = 5)

btn_Log1p = Button(calculator, text = 'ln(1+x)', width = 6, height = 2)
btn_Percents.grid(row = 5, column = 6)


window.mainloop()