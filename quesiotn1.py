import tkinter as tk

root = tk.Tk()
root.title("Area Quiz")
root.geometry("1000x540")
root.configure(background='navajo white')

Label17 = tk.Label(root, text= "Quiz", font=("Impact", 45), bg='navajo white', padx=20, pady=10, borderwidth=2)
Label17.pack()
Label17.place(x=430, y=25)

button5 = tk.Button(root, text="Next Question", height=3, width=15, bg='gray20', fg='white', relief="raised")
button5.place(x=850, y=460)

Label18 = tk.Label(root, text = "Question 1: What is the area of a square with side lengths 6?", font=("Comic Sans MS", 17), bg='navajo white',padx=20, pady=10, borderwidth=2)
Label18.pack()
Label18.place(x=100, y=155)
root.mainloop()