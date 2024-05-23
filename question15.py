import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Area Quiz")
root.geometry("1000x540")
root.configure(background='navajo white')

Label85 = tk.Label(root, text= "Quiz", font=("Impact", 45), bg='navajo white', padx=20, pady=10, borderwidth=2)
Label85.place(x=430, y=0)

button5 = tk.Button(root, text="Next Question", height=3, width=15, bg='gray20', fg='white', relief="raised")
button5.place(x=50, y=460)

button3 = tk.Button(root, text="Exit", height=3, width=15, bg='gray20', fg='white', relief="raised", command=root.destroy)
button3.place(x=215, y=460)

Label86 = tk.Label(root, text = "Question 15 CHALLANGE: What is the area of the arrow?", font=("Comic Sans MS", 17), bg='navajo white',padx=20, pady=10, borderwidth=2)
Label86.place(x=50, y=125)

Label87 = tk.Label(root, text = "Enter Your Answer Below", font=("Comic Sans MS", 10), bg='navajo white',padx=20, pady=10, borderwidth=2)
Label87.place(x=50, y=175)

entry_values=tk.Entry(root, width=20, font=("Comic Sans MS", 15))
entry_values.place(x=70, y=220)

img_5 = ImageTk.PhotoImage(Image.open("Star.png").resize((100, 100)))
Label88 = tk.Label(root, image=img_5, bg='navajo white')
Label88.place(x=300, y=0)

img_6 = ImageTk.PhotoImage(Image.open("Star.png").resize((100, 100)))
Label89 = tk.Label(root, image=img_6, bg='navajo white')
Label89.place(x=600, y=0)

img_14 = ImageTk.PhotoImage(Image.open("img14.png").resize((400, 400)))
Label90 = tk.Label(root, image=img_14, bg='navajo white')
Label90.place(x=475, y=165)

root.mainloop() 