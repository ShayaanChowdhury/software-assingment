import tkinter as tk

root =tk.Tk()
root.title("Area Quiz")
root.geometry("1000x600") 

Label1=tk.Label(root, 
             text="Learn Area Of Shapes",
             font=("Times New Roman",30),
             padx=20,
             pady=10,
             borderwidth =2
             )
Label1.pack() #showing the label on the screen
Label1.place(x=325,y=100)

root.mainloop()