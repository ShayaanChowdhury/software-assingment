import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Area Quiz")
root.geometry("1000x540")
root.configure(background='navajo white')

Label65 = tk.Label(root, text= "Quiz", font=("Impact", 45), bg='navajo white', padx=20, pady=10, borderwidth=2)
Label65.place(x=430, y=0)

button5 = tk.Button(root, text="Next Question", height=3, width=15, bg='gray20', fg='white', relief="raised")
button5.place(x=50, y=460)

button3 = tk.Button(root, text="Exit", height=3, width=15, bg='gray20', fg='white', relief="raised", command=root.destroy)
button3.place(x=215, y=460)

Label66 = tk.Label(root, text = "Question 12 CHALLANGE: What is the area of the following composite shape?", font=("Comic Sans MS", 17), bg='navajo white',padx=20, pady=10, borderwidth=2)
Label66.place(x=50, y=125)

Label67 = tk.Label(root, text = "Enter Your Answer Below", font=("Comic Sans MS", 10), bg='navajo white',padx=20, pady=10, borderwidth=2)
Label67.place(x=50, y=175)

entry_values=tk.Entry(root, width=20, font=("Comic Sans MS", 15))
entry_values.place(x=70, y=220)

Label68 = tk.Label(root, text = "HINT:*Cut it into different shapes*", font=("Comic Sans MS", 10), bg='navajo white',padx=20, pady= 10, borderwidth= 2)
Label68.place(x=50, y=250)

img_5 = ImageTk.PhotoImage(Image.open("Star.png").resize((100, 100)))
Label69 = tk.Label(root, image=img_5, bg='navajo white')
Label69.place(x=300, y=0)

img_6 = ImageTk.PhotoImage(Image.open("Star.png").resize((100, 100)))
Label70 = tk.Label(root, image=img_6, bg='navajo white')
Label70.place(x=600, y=0)

img_11 = ImageTk.PhotoImage(Image.open("img11.png").resize((400, 400)))
Label71 = tk.Label(root, image=img_11, bg='navajo white')
Label71.place(x=550, y=175)

root.mainloop() 