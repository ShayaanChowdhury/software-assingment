import tkinter as tk
from PIL import Image, ImageTk
root =tk.Tk()
root.title("Area Quiz")
root.geometry("1000x600") 

Label1=tk.Label(root, text="Learn Area Of Shapes", font=("Times New Roman",30), bg='light sky blue', padx=20, pady=10, borderwidth =2)
Label1.pack() 
Label1.place(x=325,y=100)
root.configure(background='light sky blue')

def button_click():
    Label2=tk.Label(root,)
    Label2.pack()

def button_click2():
    Label3=tk.Label(root,)
    Label3.pack()

button1=tk.Button(root,text="Formula Sheet", height=3, width=15, bg='gray20', fg='white', relief="raised", command=button_click)
button1.place(x=455,y=210)

button2=tk.Button(root,text="Start Quiz", height=3, width=15, bg='gray20', fg='white', relief="raised", command=button_click2)
button2.place(x=455,y=310)


img_1 = ImageTk.PhotoImage(Image.open("img1.png").resize((195,195)))
Label4= tk.Label(root, image=img_1, bg= 'light sky blue')
Label4.place(x=35,y=195)

img_2 = ImageTk.PhotoImage(Image.open("img2.png").resize((195,195)))
Label5= tk.Label(root, image=img_2, bg= 'light sky blue')
Label5.place(x=230,y=195)

img_3 = ImageTk.PhotoImage(Image.open("img3.png").resize((195,195)))
Label6= tk.Label(root, image=img_3, bg= 'light sky blue')
Label6.place(x=615,y=195)

img_4 = ImageTk.PhotoImage(Image.open("img4.png").resize((195,195)))
Label7= tk.Label(root, image=img_4, bg= 'light sky blue')
Label7.place(x=805,y=195)

root.mainloop()