import tkinter as tk
from PIL import Image, ImageTk
import main_window

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
        main_window.open_main_window()

    button3 = tk.Button(formula_window, text="Back to Home", height=3, width=15, bg='gray20', fg='white', relief="raised", command=back_to_home)
    button3.place(x=850, y=500)

    img_5 = ImageTk.PhotoImage(Image.open("Triangle.png").resize((250, 250)))
    Label13 = tk.Label(formula_window, image=img_5, bg='navajo white')
    Label13.image = img_5 
    Label13.place(x=0, y=220)

    img_6 = ImageTk.PhotoImage(Image.open("Circle.png").resize((250, 250)))
    Label14 = tk.Label(formula_window, image=img_6, bg='navajo white')
    Label14.image = img_6 
    Label14.place(x=260, y=210)

    img_7 = ImageTk.PhotoImage(Image.open("Rectangle.png").resize((250, 250)))
    Label15 = tk.Label(formula_window, image=img_7, bg='navajo white')
    Label15.image = img_7  
    Label15.place(x=520, y=210)

    img_8 = ImageTk.PhotoImage(Image.open("Square.png").resize((230, 230)))
    Label16 = tk.Label(formula_window, image=img_8, bg='navajo white')
    Label16.image = img_8  
    Label16.place(x=770, y=210)

    formula_window.mainloop()

if __name__ == "__main__":
    open_formula_window()
