import tkinter as tk
root=tk.Tk()
root.title("login form")
root.geometry('500x500')
root.minsize(500,500)
root.maxsize(600,600)
s=""
l=tk.Label(root,text="Name",bg='yellow')
l1=tk.Label(root,text="contact",bg='yellow')
t1=tk.Entry(width=50,text=s)
t2=tk.Entry(width=50)
def show():
    print('button clicked')
    s="gahro"
b=tk.Button(text='click',command=show)
l.grid(row=0,column=0,padx=10,pady=10)
l1.grid(row=1,column=0,padx=1)
t1.grid(row=0,column=1)
t2.grid(row=1,column=1)
b.grid(row=2,column=1)

    
root.mainloop() 


