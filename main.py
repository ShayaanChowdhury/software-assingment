import tkinter as tk

root =tk.Tk()
root.title("Area Quiz")
root.geometry("1000x600") 

Label1=tk.Label(root, text="Learn Area Of Shapes", font=("Times New Roman",30), bg='deep sky blue', padx=20, pady=10, borderwidth =2)
Label1.pack() 
Label1.place(x=325,y=100)
root.configure(background='deep sky blue')

def button_click():
    label2=tk.Label(root,)
    label2.pack()

def button_click2():
    label3=tk.Label(root,)
    label3.pack()

button1=tk.Button(root,text="Formula Sheet", height=3, width=15, bg='gray20', fg='white', relief="raised", command=button_click)
button1.place(x=455,y=200)

button2=tk.Button(root,text="Start Quiz", height=3, width=15, bg='gray20', fg='white', relief="raised", command=button_click2)
button2.place(x=455,y=300)


root.mainloop()