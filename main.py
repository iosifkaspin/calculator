import tkinter as tk

root = tk.Tk()
root.geometry('500x500+500+500')
root['bg'] = 'blue'
root.title('calculator')
def add_number(digit):
    value = calc.get()
    if value[0]=='0' and len(value)== 1:
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0,value + digit)
def add_digite(digit):
    return tk.Button(text=digit,bd = 5,font=('Arial',13), command=lambda:add_number(digit))
def make_operation(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red',command=lambda: add_number(operation))




calc = tk.Entry(root, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.insert(0,'0')
calc.grid(row=0,column=0,columnspan=4,stick = 'we')
add_digite('1').grid(row=1,column=0,sticky='wens',padx=5,pady=5)
add_digite('2').grid(row=1,column=1,sticky='wens',padx=5,pady=5)
add_digite('3').grid(row=1,column=2,sticky='wens',padx=5,pady=5)
add_digite('4').grid(row=2,column=0,sticky='wens',padx=5,pady=5)
add_digite('5').grid(row=2,column=1,sticky='wens',padx=5,pady=5)
add_digite('6').grid(row=2,column=2,sticky='wens',padx=5,pady=5)
add_digite('7').grid(row=3,column=0,sticky='wens',padx=5,pady=5)
add_digite('8').grid(row=3,column=1,sticky='wens',padx=5,pady=5)
add_digite('9').grid(row=3,column=2,sticky='wens',padx=5,pady=5)
add_digite('0').grid(row=4,column=1,sticky='wens',padx=5,pady=5)
make_operation('+').grid(row=1,column=3,sticky='wens',padx=5,pady=5)
make_operation('-').grid(row=2,column=3,sticky='wens',padx=5,pady=5)
make_operation('/').grid(row=3,column=3,sticky='wens',padx=5,pady=5)
make_operation('*').grid(row=4,column=3,sticky='wens',padx=5,pady=5)










root.mainloop()