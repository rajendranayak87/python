from tkinter import *
rt=Tk()
rt.geometry("270x150")
root=Frame(rt,height=900,width=900,bg="orange",cursor="cross",)
expression=""
total=""
#f=Frame(root,height=900,width=900,bg="black")
#f.propagate(0)
#f.pack()
one=Button(root,text='1',width=7,height=3,bg="red",command=lambda:buttonClick(1))
one.grid(row=405,column=1,ipadx=28)
Two=Button(root,text='2',width=7,height=3,bg="red",command=lambda:buttonClick(2))
Two.grid(row=405,column=2,ipadx=28)

Three=Button(root,text='3',width=7,height=3,bg="red" ,command=lambda:buttonClick(3))
Three.grid(row=405,column=3,ipadx=28)
Four=Button(root,text='4',width=7,height=3,bg="red",command=lambda:buttonClick(4))
Four.grid(row=405,column=4,ipadx=28)
Five=Button(root,text='5',width=7,height=3,bg="red",command=lambda:buttonClick(5))
Five.grid(row=406,column=1,ipadx=28)
Six=Button(root,text='6',width=7,height=3,bg="red",command=lambda:buttonClick(6))
Six.grid(row=406,column=2,ipadx=28)
Seven=Button(root,text='7',width=7,height=3,bg="red",command=lambda:buttonClick(7))
Seven.grid(row=406,column=3,ipadx=28)
Eight=Button(root,text='8',width=7,height=3,bg="red",command=lambda:buttonClick(8))
Eight.grid(row=406,column=4,ipadx=28)
nine=Button(root,text='9',width=7,height=3,bg="red",command=lambda:buttonClick(9))
nine.grid(row=407,column=1,ipadx=28)
Zero=Button(root,text='0',width=7,height=3,bg="red",command=lambda:buttonClick(0))
Zero.grid(row=407,column=2,ipadx=28)
minus=Button(root,text='-',width=7,height=3,bg="red",command=lambda:buttonClick("-"))
minus.grid(row=407,column=3,ipadx=28)
plus=Button(root,text='+',width=7,height=3,bg="white",command=lambda:buttonClick("+"))
plus.grid(row=407,column=4,ipadx=28)
div=Button(root,text='/',width=7,height=3,bg="white",command=lambda:buttonClick("/"))
div.grid(row=408,column=1,ipadx=28)
mul=Button(root,text='*',width=7,height=3,bg="white",command=lambda:buttonClick("*"))
mul.grid(row=408,column=2,ipadx=28)
equal=Button(root,text='=' ,width=7,height=3,bg="white",command=lambda:equalpress())
equal.grid(row=408,column=3,ipadx=28)
clear=Button(root,text='C',width=7,height=3,bg="white",command=lambda:clear())
clear.grid(row=408,column=4,ipadx=28)
equation=StringVar()
dis=Entry(root,textvariable=equation,width=30,border="5px",bg="green",font=("Arial",20,"bold") )
dis.grid(row=200,column=0,columnspan=15,ipady=20)
def buttonClick(num):
    global total
    global expression
    if total!=""and num=="+" or num=="-" or num=="+" or num=="/":
        expression =expression+str(num)+str(total)
    else:
        expression=expression+str(num)
    equation.set(expression)
def equalpress():
    try:
        global  expression
        total=(str(eval(expression)))
        (equation.set(total))
        #expression=""
    except:
        equation.set("error")
        expression=""
def clear():

    global  expression
    expression=""
    equation.set("")

root.pack()
root.mainloop()
