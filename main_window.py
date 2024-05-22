import tkinter as tk
from PIL import Image, ImageTk
import formula_sheet

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
        formula_sheet.open_formula_window()

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

open_main_window()

