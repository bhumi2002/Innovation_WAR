from tkinter import *
def showval(): 
    print (sli1.get())
parent = Tk()
parent.geometry("500x500")
sli1 = Scale(parent, from_=10, to=100, orient=HORIZONTAL)
sli1.place(relx=0.15,rely=0.06,relwidth=10)
sli1.pack()
Button(parent, text='click me !!', command=showval).pack()
mainloop()
