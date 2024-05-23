import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Area Quiz")
root.geometry("1000x540")
root.configure(background='navajo white')

Label79 = tk.Label(root, text= "Quiz", font=("Impact", 45), bg='navajo white', padx=20, pady=10, borderwidth=2)
Label79.place(x=430, y=0)

button5 = tk.Button(root, text="Next Question", height=3, width=15, bg='gray20', fg='white', relief="raised")
button5.place(x=50, y=460)

button3 = tk.Button(root, text="Exit", height=3, width=15, bg='gray20', fg='white', relief="raised", command=root.destroy)
button3.place(x=215, y=460)

Label80 = tk.Label(root, text = "Question 14 CHALLANGE: What is the shaded area of the following shape?", font=("Comic Sans MS", 17), bg='navajo white',padx=20, pady=10, borderwidth=2)
Label80.place(x=50, y=125)

Label81 = tk.Label(root, text = "Enter Your Answer Below", font=("Comic Sans MS", 10), bg='navajo white',padx=20, pady=10, borderwidth=2)
Label81.place(x=50, y=175)

entry_values=tk.Entry(root, width=20, font=("Comic Sans MS", 15))
entry_values.place(x=70, y=220)

Label82 = tk.Label(root, text = "HINT:*Cut it into different shapes*", font=("Comic Sans MS", 10), bg='navajo white',padx=20, pady= 10, borderwidth= 2)
Label82.place(x=50, y=250)

img_5 = ImageTk.PhotoImage(Image.open("Star.png").resize((100, 100)))
Label83 = tk.Label(root, image=img_5, bg='navajo white')
Label83.place(x=300, y=0)

img_6 = ImageTk.PhotoImage(Image.open("Star.png").resize((100, 100)))
Label57 = tk.Label(root, image=img_6, bg='navajo white')
Label57.place(x=600, y=0)

img_13 = ImageTk.PhotoImage(Image.open("img13.png").resize((370, 370)))
Label84 = tk.Label(root, image=img_13, bg='navajo white')
Label84.place(x=530, y=170)

root.mainloop() 