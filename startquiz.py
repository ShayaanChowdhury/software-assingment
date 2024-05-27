import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

Questions = [
    {"Question": "Question 1: What is the area of a square with side lengths 6?", "options": ["12", "36", "24", "32"], "answer": "36"},
    {"Question": "Question 2: What is the area of the following shape?", "options": ["8", "26", "24", "16"], "answer": "16", "image": "img7.png"},
    {"Question": "Question 3: What is the area of a rectangle with length 7 and width 3?", "options": ["10", "20", "21", "42"], "answer": "21"},
    {"Question": "Question 4: What is the following shape?", "options": ["Rhombus", "Square", "Rectangle", "Parallelogram"], "answer": "Rectangle", "image": "img8.png"},
    {"Question": "Question 5: What is the length of a rectangle with area of 44 and width 11?", "options": None, "answer": "4"},
    {"Question": "Question 6: What is the area of a triangle with base 13 and height 4?", "options": None, "answer": "26"},
    {"Question": "Question 7: What is the base of a triangle with an area of 20 and height of 5?", "options": None, "answer": "8"},
    {"Question": "Question 8: What is the area of the triangle shown?", "options": None, "answer": "72", "image": "img9.png"},
    {"Question": "Question 9: What is the area of the circle shown?", "options": ["36π", "20π", "49π", "25π"], "answer": "49π", "image": "img10.png"},
    {"Question": "Question 10: What is the area of the circle with diameter of 32?", "options": ["572π", "542π", "256π", "1024π"], "answer": "256π"},
    {"Question": "Question 11: What is the radius of a circle with an area of 2401π?", "options": ["49π", "98π", "65π", "1200π"], "answer": "49π"},
    {"Question": "Question 12 CHALLANGE: What is the area of the following composite shape?", "options": None, "answer": "57", "image": "img11.png"},
    {"Question": "Question 13 CHALLANGE: What is the area of the following composite shape?", "options": None, "answer": "96", "image": "img12.png"},
    {"Question": "Question 14 CHALLANGE: What is the shaded area of the following shape?", "options": None, "answer": "54", "image": "img13.png"},
    {"Question": "Question 15 CHALLANGE: What is the area of the arrow?", "options": None, "answer": "57", "image": "img14.png"},
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

img_5 = ImageTk.PhotoImage(Image.open("Star.png").resize((100, 100)))
Label21 = tk.Label(root, image=img_5, bg='navajo white')
Label21.place(x=300, y=0)

img_6 = ImageTk.PhotoImage(Image.open("Star.png").resize((100, 100)))
Label21 = tk.Label(root, image=img_6, bg='navajo white')
Label21.place(x=600, y=0)

answer_entry = None
question_image_label = None

def load_question(question_data):
    global answer_entry, question_image_label
    label_question.config(text=question_data["Question"])
    options = question_data["options"]
    destroy_previous_question_widgets()
    
    if options:
        for i, option in enumerate(options):
            tk.Radiobutton(root, text=option, font=('Comic Sans Ms', 15), value=option, variable=r, bg='navajo white').place(x=60, y=200 + i*50)
    else:
        answer_entry = tk.Entry(root, font=("Comic Sans MS", 15), width=30)
        answer_entry.place(x=50, y=200)
    
    if "image" in question_data:
        question_image = ImageTk.PhotoImage(Image.open(question_data["image"]).resize((350, 350)))
        question_image_label = tk.Label(root, image=question_image, bg='navajo white')
        question_image_label.image = question_image
        question_image_label.place(x=650, y=175)

def destroy_previous_question_widgets():
    global answer_entry, question_image_label
    if answer_entry:
        answer_entry.destroy()
        answer_entry = None
    if question_image_label:
        question_image_label.destroy()
        question_image_label = None

current_question_index = 0
r = tk.StringVar()
label_question = tk.Label(root, text="", font=("Comic Sans MS", 17), bg='navajo white', padx=20, pady=10, borderwidth=2)
label_question.place(x=50, y=125)
load_question(Questions[current_question_index])

correct_answers = 0

def show_final_score():
    final_screen = tk.Toplevel(root)
    final_screen.title("Quiz Results")
    final_screen.geometry("500x550")
    final_screen.configure(background='navajo white')

    score_label = tk.Label(final_screen, text=f"Your score is {correct_answers}/{len(Questions)}", font=("Comic Sans MS", 20), bg='navajo white')
    score_label.pack(pady=20)

    percentage = (correct_answers / len(Questions)) * 100
    percentage_label = tk.Label(final_screen, text=f"Percentage: {percentage:.2f}%", font=("Comic Sans MS", 20), bg='navajo white')
    percentage_label.pack(pady=10)

    star_img = ImageTk.PhotoImage(Image.open("Star.png").resize((150, 150)))
    star_label = tk.Label(final_screen, image=star_img, bg='navajo white')
    star_label.image = star_img
    star_label.pack(pady=10)

    button_return_home = tk.Button(final_screen, text="Return Home", height=3, width=15, bg='gray20', fg='white', relief="raised")
    button_return_home.pack(pady=20)

    button_exit = tk.Button(final_screen, text="Exit", height=3, width=15, bg='gray20', fg='white', relief="raised", command=root.destroy)
    button_exit.pack(pady=20)

    root.withdraw()

def next_question():
    global current_question_index, correct_answers
    selected_answer = r.get() if Questions[current_question_index]["options"] else answer_entry.get().strip()
    correct_answer = Questions[current_question_index]["answer"]
    
    if selected_answer == correct_answer:
        messagebox.showinfo("Result", "Correct!")
        correct_answers += 1
    else:
        messagebox.showinfo("Result", f"Incorrect! The correct answer is {correct_answer}.")
    
    current_question_index += 1
    if current_question_index < len(Questions):
        load_question(Questions[current_question_index])
    else:
        show_final_score()

button_next.config(command=next_question)
root.mainloop()