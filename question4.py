import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Area Quiz")
root.geometry("1000x540")
root.configure(background='navajo white')

Label27 = tk.Label(root, text= "Quiz", font=("Impact", 45), bg='navajo white', padx=20, pady=10, borderwidth=2)
Label27.place(x=430, y=0)

button5 = tk.Button(root, text="Next Question", height=3, width=15, bg='gray20', fg='white', relief="raised")
button5.place(x=50, y=460)

button3 = tk.Button(root, text="Exit", height=3, width=15, bg='gray20', fg='white', relief="raised", command=root.destroy)
button3.place(x=215, y=460)

Label28 = tk.Label(root, text = "Question 4: What is the following shape?", font=("Comic Sans MS", 17), bg='navajo white',padx=20, pady=10, borderwidth=2)
Label28.place(x=50, y=125)

img_5 = ImageTk.PhotoImage(Image.open("Star.png").resize((100, 100)))
Label29 = tk.Label(root, image=img_5, bg='navajo white')
Label29.place(x=300, y=0)

img_6 = ImageTk.PhotoImage(Image.open("Star.png").resize((100, 100)))
Label30 = tk.Label(root, image=img_6, bg='navajo white')
Label30.place(x=600, y=0)

img_8 = ImageTk.PhotoImage(Image.open("img8.png").resize((400, 400)))
Label31 = tk.Label(root, image=img_8, bg='navajo white')
Label31.place(x=550, y=120)
r = tk.IntVar()

option_1 = tk.Radiobutton(root, text= "Rhombus", font= ('Comic Sans Ms', 15), value = 1, variable = r, bg= 'navajo white').place(x=60, y=200)
option_2 = tk.Radiobutton(root, text= "Square", font= ('Comic Sans Ms', 15), value = 2, variable = r, bg= 'navajo white').place(x=60, y=250)
option_3 = tk.Radiobutton(root, text= "Rectangle", font= ('Comic Sans Ms', 15), value = 3, variable = r, bg= 'navajo white').place(x=60, y=300)
option_4 = tk.Radiobutton(root, text= "Parallelogram", font= ('Comic Sans Ms', 15), value = 4, variable = r, bg= 'navajo white').place(x=60, y=350)

root.mainloop()