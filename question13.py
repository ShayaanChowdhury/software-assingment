import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Area Quiz")
root.geometry("1000x540")
root.configure(background='navajo white')

Label72 = tk.Label(root, text= "Quiz", font=("Impact", 45), bg='navajo white', padx=20, pady=10, borderwidth=2)
Label72.place(x=430, y=0)

button5 = tk.Button(root, text="Next Question", height=3, width=15, bg='gray20', fg='white', relief="raised")
button5.place(x=50, y=460)

button3 = tk.Button(root, text="Exit", height=3, width=15, bg='gray20', fg='white', relief="raised", command=root.destroy)
button3.place(x=215, y=460)

Label73 = tk.Label(root, text = "Question 13 CHALLANGE: What is the area of the following composite shape?", font=("Comic Sans MS", 17), bg='navajo white',padx=20, pady=10, borderwidth=2)
Label73.place(x=50, y=125)

Label74 = tk.Label(root, text = "Enter Your Answer Below", font=("Comic Sans MS", 10), bg='navajo white',padx=20, pady=10, borderwidth=2)
Label74.place(x=50, y=175)

entry_values=tk.Entry(root, width=20, font=("Comic Sans MS", 15))
entry_values.place(x=70, y=220)

Label75 = tk.Label(root, text = "HINT:*Cut it into different shapes*", font=("Comic Sans MS", 10), bg='navajo white',padx=20, pady= 10, borderwidth= 2)
Label75.place(x=50, y=250)

img_5 = ImageTk.PhotoImage(Image.open("Star.png").resize((100, 100)))
Label76 = tk.Label(root, image=img_5, bg='navajo white')
Label76.place(x=300, y=0)

img_6 = ImageTk.PhotoImage(Image.open("Star.png").resize((100, 100)))
Label77 = tk.Label(root, image=img_6, bg='navajo white')
Label77.place(x=600, y=0)

img_12 = ImageTk.PhotoImage(Image.open("img12.png").resize((400, 400)))
Label78 = tk.Label(root, image=img_12, bg='navajo white')
Label78.place(x=550, y=170)

root.mainloop() 