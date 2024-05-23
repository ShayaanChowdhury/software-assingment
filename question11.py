import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Area Quiz")
root.geometry("1000x540")
root.configure(background='navajo white')

Label61 = tk.Label(root, text= "Quiz", font=("Impact", 45), bg='navajo white', padx=20, pady=10, borderwidth=2)
Label61.place(x=430, y=0)

button5 = tk.Button(root, text="Next Question", height=3, width=15, bg='gray20', fg='white', relief="raised")
button5.place(x=50, y=460)

button3 = tk.Button(root, text="Exit", height=3, width=15, bg='gray20', fg='white', relief="raised", command=root.destroy)
button3.place(x=215, y=460)

Label62 = tk.Label(root, text = "Question 11: What is the radius of a circle with an area of 2401π?", font=("Comic Sans MS", 17), bg='navajo white',padx=20, pady=10, borderwidth=2)
Label62.place(x=50, y=125)


img_5 = ImageTk.PhotoImage(Image.open("Star.png").resize((100, 100)))
Label63 = tk.Label(root, image=img_5, bg='navajo white')
Label63.place(x=300, y=0)

img_6 = ImageTk.PhotoImage(Image.open("Star.png").resize((100, 100)))
Label64 = tk.Label(root, image=img_6, bg='navajo white')
Label64.place(x=600, y=0)

r = tk.IntVar()

option_1 = tk.Radiobutton(root, text= "49π", font= ('Comic Sans Ms', 15), value = 1, variable = r, bg= 'navajo white').place(x=60, y=200)
option_2 = tk.Radiobutton(root, text= "98π", font= ('Comic Sans Ms', 15), value = 2, variable = r, bg= 'navajo white').place(x=60, y=250)
option_3 = tk.Radiobutton(root, text= "65π", font= ('Comic Sans Ms', 15), value = 3, variable = r, bg= 'navajo white').place(x=60, y=300)
option_4 = tk.Radiobutton(root, text= "1200π", font= ('Comic Sans Ms', 15), value = 4, variable = r, bg= 'navajo white').place(x=60, y=350)

root.mainloop() 