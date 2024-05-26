import tkinter as tk
from PIL import Image, ImageTk

Questions = [
    {"Question": "Question 1: What is the area of a square with side lengths 6?", "options": ["12", "36", "24", "32"], "answer": "36"},
    {"Question": "Question 2: What is the area of the following shape?", "options": ["8", "26", "24", "16"], "answer": "16"},
    {"Question": "Question 3: What is the area of a rectangle with length 7 and width 3?", "options": ["10", "20", "21", "42"], "answer": "21"},
    {"Question": "Question 4: What is the following shape?", "options": ["Rhombus", "Square", "Rectangle", "Parallelogram"], "answer": "Rectangle"},
    {"Question": "Question 5: What is the length of a rectangle with area of 44 and width 11?", "options": None, "answer": "4"},
    {"Question": "Question 6: What is the area of a triangle with base 13 and height 4?", "options": None, "answer": "26"},
    {"Question": "Question 7: What is the base of a triangle with an area of 20 and height of 5?", "options": None, "answer": "8"},
    {"Question": "Question 8: What is the area of the triangle shown?", "options": None, "answer": "72"},
    {"Question": "Question 9: What is the area of the circle shown?", "options": ["36π", "20π", "49π", "25π"], "answer": "49π"},
    {"Question": "Question 10: What is the area of the circle with diameter of 32?", "options": ["572π", "542π", "256π", "1024π"], "answer": "256π"},
    {"Question": "Question 11: What is the radius of a circle with an area of 2401π?", "options": ["49π", "98π", "65π", "1200π"], "answer": "49π"},
    {"Question": "Question 12 CHALLENGE: What is the area of the following composite shape?", "options": None, "answer": "57"},
    {"Question": "Question 13 CHALLENGE: What is the area of the following composite shape?", "options": None, "answer": "96"},
    {"Question": "Question 14 CHALLENGE: What is the shaded area of the following shape?", "options": None, "answer": "54"},
    {"Question": "Question 15 CHALLENGE: What is the area of the arrow?", "options": None, "answer": "57"}
]

root = tk.Tk()
root.title("Area Quiz")
root.geometry("1000x540")
root.configure(background='navajo white')

label_quiz = tk.Label(root, text="Quiz", font=("Impact", 45), bg='navajo white', padx=20, pady=10, borderwidth=2)
label_quiz.place(x=430, y=0)

button_next = tk.Button(root, text="Next Question", height=3, width=15, bg='gray20', fg='white', relief="raised")
button_next.place(x=50, y=460)

button_exit = tk.Button(root, text="Exit", height=3, width=15, bg='gray20', fg='white', relief="raised", command=root.destroy)
button_exit.place(x=215, y=460)

def load_question(question_data):
    label_question.config(text=question_data["Question"])
    options = question_data["options"]
    if options:
        for i, option in enumerate(options):
            tk.Radiobutton(root, text=option, font=('Comic Sans Ms', 15), value=i+1, variable=r, bg='navajo white').place(x=60, y=200 + i*50)
        if "answer_entry" in globals():
            answer_entry.destroy()
    else:
        if "answer_entry" in globals():
            answer_entry.destroy()
        answer_entry = tk.Entry(root, font=("Comic Sans MS", 15), width=30)
        answer_entry.place(x=50, y=200)

current_question_index = 0
r = tk.IntVar()
label_question = tk.Label(root, text="", font=("Comic Sans MS", 17), bg='navajo white', padx=20, pady=10, borderwidth=2)
label_question.place(x=50, y=125)
load_question(Questions[current_question_index])

img_5 = ImageTk.PhotoImage(Image.open("Star.png").resize((100, 100)))
label_img_5 = tk.Label(root, image=img_5, bg='navajo white')
label_img_5.place(x=300, y=0)

img_6 = ImageTk.PhotoImage(Image.open("Star.png").resize((100, 100)))
label_img_6 = tk.Label(root, image=img_6, bg='navajo white')
label_img_6.place(x=600, y=0)

def next_question():
    global current_question_index
    current_question_index += 1
    if current_question_index < len(Questions):
        load_question(Questions[current_question_index])
    else:

        pass

button_next.config(command=next_question)

root.mainloop()