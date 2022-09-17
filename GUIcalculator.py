
from tkinter import *
import math


#from tkinter import font
win = Tk()
#win.resizable(0, 0)
win.title('Calculator')
win.geometry('298x435')
win['bg'] = 'grey'

data = ''
inputVal = StringVar()
def clickListener(butVal):
    global data
    data = data + str(butVal)
    inputVal.set(data)

def equal():
    global data
    try:
        if data == '':
            inputVal.set('')
            data = ''
        else:
            solution = eval(data)
            inputVal.set(solution)
            data = str(solution)
            
    except:
        inputVal.set('')
        data = ''

def deleteDigit():
    global data
    try:
        solution = list(data)
        solution.pop()
        data = ''.join(solution)
        inputVal.set(data)
    except:
        inputVal.set('')
        data = ''

def Percentage():
    global data
    try:
            solution = float(data)/100
            inputVal.set(solution)
            data = str(solution)
    except:
            inputVal.set('')
            data = ''

def Sqrt():
    try:
        global data
        solution = math.sqrt(float(data))
        inputVal.set(solution)
        data = str(solution)
    except:
        inputVal.set("")
        data = ""



def clearAll():
    global data
    data = ''
    inputVal.set('')



frame = Frame(win,width=298,height=20,bd=2)
frame.pack(side=TOP,pady=5)
inputField = Entry(frame,width=20, font=('Arial bold',20),textvariable=inputVal,bg='white',fg='blue',justify=RIGHT)
#inputField.grid(row=0,column=0)
inputField.pack()

bton_frame = Frame(win,width=298,height=350,bg='black')
bton_frame.pack(side=TOP,pady=5)
nine = Button(bton_frame,text='9',bg='white',fg='blue',font=('Arial bold',10),width=8,height=4,command = lambda: clickListener(9)).grid(row=0,column=0)
eight = Button(bton_frame,text='8',bg='white',fg='blue',font=('Arial bold',10),width=8,height=4,command = lambda: clickListener(8)).grid(row=0,column=1)
seven = Button(bton_frame,text='7',bg='white',fg='blue',font=('Arial bold',10),width=8,height=4,command = lambda: clickListener(7)).grid(row=0,column=2)
clear = Button(bton_frame,text='⇐',bg='red',fg='white',font=('Arial bold',10),width=8,height=4,command = lambda: deleteDigit()).grid(row=0,column=3)


six = Button(bton_frame,text='6',bg='white',fg='blue',font=('Arial bold',10),width=8,height=4,command = lambda: clickListener(6)).grid(row=1,column=0)
five = Button(bton_frame,text='5',bg='white',fg='blue',font=('Arial bold',10),width=8,height=4,command = lambda: clickListener(5)).grid(row=1,column=1)
four = Button(bton_frame,text='4',bg='white',fg='blue',font=('Arial bold',10),width=8,height=4,command = lambda: clickListener(4)).grid(row=1,column=2)
add = Button(bton_frame,text='+',bg='teal',fg='white',width=8,font=('Arial bold',10),height=4,command = lambda: clickListener('+')).grid(row=1,column=3)


three = Button(bton_frame,text='3',bg='white',fg='blue',font=('Arial bold',10),width=8,height=4,command = lambda: clickListener(3)).grid(row=2,column=0)
two = Button(bton_frame,text='2',bg='white',fg='blue',font=('Arial bold',10),width=8,height=4,command = lambda: clickListener(2)).grid(row=2,column=1)
one = Button(bton_frame,text='1',bg='white',fg='blue',font=('Arial bold',10),width=8,height=4,command = lambda: clickListener(1)).grid(row=2,column=2)
divide = Button(bton_frame,text='/',bg='teal',fg='white',font=('Arial bold',10),width=8,height=4,command = lambda: clickListener('/')).grid(row=2,column=3)


point = Button(bton_frame,text='.',bg='white',fg='blue',font=('Arial bold',10),width=8,height=4,command = lambda: clickListener('.')).grid(row=3,column=0)
zero = Button(bton_frame,text='0',bg='white',fg='blue',font=('Arial bold',10),width=8,height=4,command = lambda: clickListener(0)).grid(row=3,column=1)
times = Button(bton_frame,text='*',bg='teal',fg='white',font=('Arial bold',10),width=8,height=4,command = lambda: clickListener('*')).grid(row=3,column=2)
minus = Button(bton_frame,text='-',bg='teal',fg='white',font=('Arial bold',10),width=8,height=4,command = lambda: clickListener('-')).grid(row=3,column=3)


exponent = Button(bton_frame,text='^',bg='white',fg='blue',font=('Arial bold',10),width=8,height=4,command = lambda: clickListener('**')).grid(row=4,column=0)
sqrt = Button(bton_frame,text='√',bg='white',fg='blue',font=('Arial bold',10),width=8,height=4,command = lambda: Sqrt()).grid(row=4,column=1)
percent = Button(bton_frame,text='%',bg='white',fg='blue',font=('Arial bold',10),width=8,height=4,command = lambda:Percentage()).grid(row=4,column=2)
equals = Button(bton_frame,text='=',bg='green',fg='white',font=('Arial bold',10),width=8,height=4,command = lambda: equal()).grid(row=4,column=3)



win.mainloop()
