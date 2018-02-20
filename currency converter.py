from tkinter import*
root=Tk()
root.geometry("400x300+150+150")
root.title("currency converter")
heading=Label(root,text="wellcome to currency converter",font=('arial 15 bold'),fg="steel blue").pack()
entr_amt=Label(root,text="enter ammount in dollar",font=('arial 20 bold')).place(x=10,y=50)
my_num=IntVar()
ent_box=Entry(root,width=50,textvariable=my_num).place(x=10,y=90)
def converter():
    here=my_num.get()
    final=here * 64.94
    lab=Label(root,text=("rs "+str(final)),font=("arial 25 bold"),fg="red").place(x=100,y=200)

def reverse():
    here=my_num.get()
    final=here/64.94
    lab=Label(root,text=("$ "+str(final)),font=("arial 25 bold"),fg="green").place(x=100,y=24)
btn1=Button(root,text="convert",width=12,height=2,bg="lightgreen",command=converter).place(x=100,y=130)
btn1=Button(root,text="reverse",width=12,height=2,bg="lightgreen",command=reverse).place(x=200,y=130)
