import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Area Quiz")
root.geometry("1000x540")
root.configure(background='navajo white')

Label23 = tk.Label(root, text= "Quiz", font=("Impact", 45), bg='navajo white', padx=20, pady=10, borderwidth=2)
Label23.place(x=430, y=0)

button5 = tk.Button(root, text="Next Question", height=3, width=15, bg='gray20', fg='white', relief="raised")
button5.place(x=50, y=460)

button3 = tk.Button(root, text="Exit", height=3, width=15, bg='gray20', fg='white', relief="raised", command=root.destroy)
button3.place(x=215, y=460)

Label24 = tk.Label(root, text = "Question 3: What is the area of a rectangle with length 7 and width 3?", font=("Comic Sans MS", 17), bg='navajo white',padx=20, pady=10, borderwidth=2)
Label24.place(x=50, y=125)

img_5 = ImageTk.PhotoImage(Image.open("Star.png").resize((100, 100)))
Label25 = tk.Label(root, image=img_5, bg='navajo white')
Label25.place(x=300, y=0)

img_6 = ImageTk.PhotoImage(Image.open("Star.png").resize((100, 100)))
Label26 = tk.Label(root, image=img_6, bg='navajo white')
Label26.place(x=600, y=0)

r = tk.IntVar()

option_1 = tk.Radiobutton(root, text= "10", font= ('Comic Sans Ms', 15), value = 1, variable = r, bg= 'navajo white').place(x=60, y=200)
option_2 = tk.Radiobutton(root, text= "20", font= ('Comic Sans Ms', 15), value = 2, variable = r, bg= 'navajo white').place(x=60, y=250)
option_3 = tk.Radiobutton(root, text= "21", font= ('Comic Sans Ms', 15), value = 3, variable = r, bg= 'navajo white').place(x=60, y=300)
option_4 = tk.Radiobutton(root, text= "42", font= ('Comic Sans Ms', 15), value = 4, variable = r, bg= 'navajo white').place(x=60, y=350)

root.mainloop()