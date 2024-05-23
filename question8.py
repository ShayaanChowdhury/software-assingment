import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Area Quiz")
root.geometry("1000x540")
root.configure(background='navajo white')

Label46 = tk.Label(root, text= "Quiz", font=("Impact", 45), bg='navajo white', padx=20, pady=10, borderwidth=2)
Label46.place(x=430, y=0)

button5 = tk.Button(root, text="Next Question", height=3, width=15, bg='gray20', fg='white', relief="raised")
button5.place(x=50, y=460)

button3 = tk.Button(root, text="Exit", height=3, width=15, bg='gray20', fg='white', relief="raised", command=root.destroy)
button3.place(x=215, y=460)

Label47 = tk.Label(root, text = "Question 8: What is the area of the triangle shown?", font=("Comic Sans MS", 17), bg='navajo white',padx=20, pady=10, borderwidth=2)
Label47.place(x=50, y=125)

Label48 = tk.Label(root, text = "Enter Your Answer Below", font=("Comic Sans MS", 10), bg='navajo white',padx=20, pady=10, borderwidth=2)
Label48.place(x=50, y=175)

entry_values=tk.Entry(root, width=20, font=("Comic Sans MS", 15))
entry_values.place(x=70, y=210)

img_5 = ImageTk.PhotoImage(Image.open("Star.png").resize((100, 100)))
Label49 = tk.Label(root, image=img_5, bg='navajo white')
Label49.place(x=300, y=0)

img_6 = ImageTk.PhotoImage(Image.open("Star.png").resize((100, 100)))
Label50 = tk.Label(root, image=img_6, bg='navajo white')
Label50.place(x=600, y=0)

img_9 = ImageTk.PhotoImage(Image.open("img9.png").resize((350, 350)))
Label51 = tk.Label(root, image=img_9, bg='navajo white')
Label51.place(x=630, y=150)

root.mainloop() 