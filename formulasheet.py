import tkinter as tk
from PIL import Image, ImageTk

root =tk.Tk()
root.title("Area Quiz")
root.geometry("1000x600") 

Label8=tk.Label(root, text="Formula Sheet", font=("Impact",40), bg='navajo white', padx=20, pady=10, borderwidth =2)
Label8.pack() 
Label8.place(x=340,y=20)
root.configure(background='navajo white')

Label9=tk.Label(root, text="Triangle", font=("Impact",25), bg='navajo white', padx=20, pady=10, borderwidth =2)
Label9.pack() 
Label9.place(x=35,y=155)
root.configure(background='navajo white')

Label10=tk.Label(root, text="Circle", font=("Impact",25), bg='navajo white', padx=20, pady=10, borderwidth =2)
Label10.pack() 
Label10.place(x=260,y=155)
root.configure(background='navajo white')

Label11=tk.Label(root, text="Rectangle", font=("Impact",25), bg='navajo white', padx=20, pady=10, borderwidth =2)
Label11.pack() 
Label11.place(x=520,y=155)
root.configure(background='navajo white')

Label12=tk.Label(root, text="Square", font=("Impact",25), bg='navajo white', padx=20, pady=10, borderwidth =2)
Label12.pack() 
Label12.place(x=770,y=155)
root.configure(background='navajo white')

def button_click():
    Label13=tk.Label(root,)
    Label13.pack()

button3=tk.Button(root,text="Back to Home", height=3, width=15, bg='gray20', fg='white', relief="raised", command=button_click)
button3.place(x=850,y=500)

img_5 = ImageTk.PhotoImage(Image.open("Triangle.png").resize((250,250)))
Label13= tk.Label(root, image=img_5, bg= 'navajo white')
Label13.place(x=0,y=220)

img_6 = ImageTk.PhotoImage(Image.open("Circle.png").resize((250,250)))
Label14= tk.Label(root, image=img_6, bg= 'navajo white')
Label14.place(x=260,y=210)

img_7 = ImageTk.PhotoImage(Image.open("Rectangle.png").resize((250,250)))
Label15= tk.Label(root, image=img_7, bg= 'navajo white')
Label15.place(x=520,y=210)

img_8 = ImageTk.PhotoImage(Image.open("Square.png").resize((230,230)))
Label16= tk.Label(root, image=img_8, bg= 'navajo white')
Label16.place(x=770,y=210)




root.mainloop()
