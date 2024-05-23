import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Area Quiz")
root.geometry("1000x540")
root.configure(background='navajo white')

Label32 = tk.Label(root, text= "Quiz", font=("Impact", 45), bg='navajo white', padx=20, pady=10, borderwidth=2)
Label32.place(x=430, y=0)

button5 = tk.Button(root, text="Next Question", height=3, width=15, bg='gray20', fg='white', relief="raised")
button5.place(x=50, y=460)

button3 = tk.Button(root, text="Exit", height=3, width=15, bg='gray20', fg='white', relief="raised", command=root.destroy)
button3.place(x=215, y=460)

Label33 = tk.Label(root, text = "Question 5: What is the length of a rectangle with area of 44 and width 11?", font=("Comic Sans MS", 17), bg='navajo white',padx=20, pady=10, borderwidth=2)
Label33.place(x=50, y=125)

Label34 = tk.Label(root, text = "Enter Your Answer Below", font=("Comic Sans MS", 10), bg='navajo white',padx=20, pady=10, borderwidth=2)
Label34.place(x=50, y=175)

entry_values=tk.Entry(root, width=20, font=("Comic Sans MS", 15))
entry_values.place(x=70, y=210)

img_5 = ImageTk.PhotoImage(Image.open("Star.png").resize((100, 100)))
Label35 = tk.Label(root, image=img_5, bg='navajo white')
Label35.place(x=300, y=0)

img_6 = ImageTk.PhotoImage(Image.open("Star.png").resize((100, 100)))
Label36 = tk.Label(root, image=img_6, bg='navajo white')
Label36.place(x=600, y=0)

root.mainloop()