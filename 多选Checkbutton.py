# 2021年8月 Python 自学
import tkinter as tk
def ShowSelect():

    v1 = var1.get()
    v2 = var2.get()
    print(type(v1),v1)
    if v1 == '1':
        var2.set('0')
        lab1.config(text='你选择的是'+'订阅')
    elif v2 == '1':
        var1.set('0')
        lab1.config(text='你选择的是' + '不订阅')
    else:
        lab1.config(text='你选择的是'+'不订阅' )
form1 = tk.Tk()
var1 = tk.StringVar()
var2 = tk.StringVar()
form1.geometry('400x300+200+100')
lab1=tk.Label(form1,width=20,text='你还未选择')
lab1.pack()
c1 = tk.Checkbutton(form1,text='订阅',variable=var1,command=ShowSelect)
c2 = tk.Checkbutton(form1,text='不订阅',variable=var2,command=ShowSelect)
#c1.deselect()
c1.pack(anchor='w')
c2.pack(anchor='w')
form1.mainloop()
