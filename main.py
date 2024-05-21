import tkinter as tk
from PIL import Image, ImageTk

def open_main_window():
    root = tk.Tk()
    root.title("Area Quiz")
    root.geometry("1000x540")
    root.configure(background='navajo white')

    Label1 = tk.Label(root, text="Learn Area Of Shapes", font=("Impact", 40), bg='navajo white', padx=20, pady=10, borderwidth=2)
    Label1.pack()
    Label1.place(x=280, y=80)

    def open_formula_sheet():
        root.destroy()
        open_formula_window()

    button1 = tk.Button(root, text="Formula Sheet", height=3, width=15, bg='gray20', fg='white', relief="raised", command=open_formula_sheet)
    button1.place(x=455, y=210)

    def button_click2():
        Label3 = tk.Label(root,)
        Label3.pack()

    button2 = tk.Button(root, text="Start Quiz", height=3, width=15, bg='gray20', fg='white', relief="raised", command=button_click2)
    button2.place(x=455, y=310)

    img_1 = ImageTk.PhotoImage(Image.open("img1.png").resize((195, 195)))
    Label4 = tk.Label(root, image=img_1, bg='navajo white')
    Label4.place(x=20, y=195)

    img_2 = ImageTk.PhotoImage(Image.open("img2.png").resize((195, 195)))
    Label5 = tk.Label(root, image=img_2, bg='navajo white')
    Label5.place(x=220, y=195)

    img_3 = ImageTk.PhotoImage(Image.open("img3.png").resize((195, 195)))
    Label6 = tk.Label(root, image=img_3, bg='navajo white')
    Label6.place(x=615, y=195)

    img_4 = ImageTk.PhotoImage(Image.open("img4.png").resize((195, 195)))
    Label7 = tk.Label(root, image=img_4, bg='navajo white')
    Label7.place(x=805, y=195)

    root.mainloop()

def open_formula_window():
    formula_window = tk.Tk()
    formula_window.title("Formula Sheet")
    formula_window.geometry("1000x600")
    formula_window.configure(background='navajo white')

    Label8 = tk.Label(formula_window, text="Formula Sheet", font=("Impact", 40), bg='navajo white', padx=20, pady=10, borderwidth=2)
    Label8.pack()
    Label8.place(x=340, y=20)

    Label9 = tk.Label(formula_window, text="Triangle", font=("Impact", 25), bg='navajo white', padx=20, pady=10, borderwidth=2)
    Label9.pack()
    Label9.place(x=35, y=155)

    Label10 = tk.Label(formula_window, text="Circle", font=("Impact", 25), bg='navajo white', padx=20, pady=10, borderwidth=2)
    Label10.pack()
    Label10.place(x=260, y=155)

    Label11 = tk.Label(formula_window, text="Rectangle", font=("Impact", 25), bg='navajo white', padx=20, pady=10, borderwidth=2)
    Label11.pack()
    Label11.place(x=520, y=155)

    Label12 = tk.Label(formula_window, text="Square", font=("Impact", 25), bg='navajo white', padx=20, pady=10, borderwidth=2)
    Label12.pack()
    Label12.place(x=770, y=155)

    def back_to_home():
        formula_window.destroy()
        open_main_window()

    button3 = tk.Button(formula_window, text="Back to Home", height=3, width=15, bg='gray20', fg='white', relief="raised", command=back_to_home)
    button3.place(x=850, y=500)

    img_5 = ImageTk.PhotoImage(Image.open("Triangle.png").resize((250, 250)))
    Label13 = tk.Label(formula_window, image=img_5, bg='navajo white')
    Label13.image = img_5  # Keep a reference to avoid garbage collection
    Label13.place(x=0, y=220)

    img_6 = ImageTk.PhotoImage(Image.open("Circle.png").resize((250, 250)))
    Label14 = tk.Label(formula_window, image=img_6, bg='navajo white')
    Label14.image = img_6  # Keep a reference to avoid garbage collection
    Label14.place(x=260, y=210)

    img_7 = ImageTk.PhotoImage(Image.open("Rectangle.png").resize((250, 250)))
    Label15 = tk.Label(formula_window, image=img_7, bg='navajo white')
    Label15.image = img_7  # Keep a reference to avoid garbage collection
    Label15.place(x=520, y=210)

    img_8 = ImageTk.PhotoImage(Image.open("Square.png").resize((230, 230)))
    Label16 = tk.Label(formula_window, image=img_8, bg='navajo white')
    Label16.image = img_8  # Keep a reference to avoid garbage collection
    Label16.place(x=770, y=210)

    formula_window.mainloop()

open_main_window()