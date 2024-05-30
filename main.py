import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def open_main_window():
    root = tk.Tk()
    root.title("Area Quiz")
    root.geometry("1000x540")
    root.configure(background='navajo white')

    Label1 = tk.Label(root, 
                      text="Learn Area Of Shapes", 
                      font=("Impact", 40), 
                      bg='navajo white',
                      padx=20,
                      pady=10,
                      borderwidth=2)
    Label1.place(x=280, y=80)

    def open_formula_sheet():
        root.destroy()
        open_formula_window()

    button1 = tk.Button(root,
                        text="Formula Sheet",
                        height=3,
                        width=15,
                        bg='gray20',
                        fg='white',
                        relief="raised",
                        command=open_formula_sheet)
    button1.place(x=455, y=210)

    def open_quiz():
        root.destroy()
        open_quiz_window()

    button2 = tk.Button(root,
                        text="Start Quiz",
                        height=3,
                        width=15,
                        bg='gray20',
                        fg='white',
                        relief="raised",
                        command=open_quiz)
    button2.place(x=455, y=310)

    button3 = tk.Button(root,
                        text="Exit",
                        height=3,
                        width=15,
                        bg='gray20',
                        fg='white',
                        relief="raised",
                        command=root.destroy)
    button3.place(x=455, y=410)

    img_1 = ImageTk.PhotoImage(Image.open("img1.png").resize((195, 195)))
    Label4 = tk.Label(root,
                      image=img_1,
                      bg='navajo white')
    Label4.image = img_1
    Label4.place(x=20, y=195)

    img_2 = ImageTk.PhotoImage(Image.open("img2.png").resize((195, 195)))
    Label5 = tk.Label(root,
                      image=img_2,
                      bg='navajo white')
    Label5.image = img_2
    Label5.place(x=220, y=195)

    img_3 = ImageTk.PhotoImage(Image.open("img3.png").resize((195, 195)))
    Label6 = tk.Label(root,
                      image=img_3,
                      bg='navajo white')
    Label6.image = img_3
    Label6.place(x=615, y=195)

    img_4 = ImageTk.PhotoImage(Image.open("img4.png").resize((195, 195)))
    Label7 = tk.Label(root,
                      image=img_4,
                      bg='navajo white')
    Label7.image = img_4
    Label7.place(x=805, y=195)

    root.mainloop()

def open_formula_window():
    formula_window = tk.Tk()
    formula_window.title("Formula Sheet")
    formula_window.geometry("1000x540")
    formula_window.configure(background='navajo white')

    Label8 = tk.Label(formula_window,
                      text="Formula Sheet",
                      font=("Impact", 40),
                      bg='navajo white',
                      padx=20,
                      pady=10,
                      borderwidth=2)
    Label8.place(x=340, y=10)

    Label9 = tk.Label(formula_window,
                      text="Triangle",
                      font=("Impact", 25),
                      bg='navajo white',
                      padx=20,
                      pady=10,
                      borderwidth=2)
    Label9.place(x=35, y=115)

    Label10 = tk.Label(formula_window,
                       text="Circle",
                       font=("Impact", 25),
                       bg='navajo white',
                       padx=20,
                       pady=10,
                       borderwidth=2)
    Label10.place(x=260, y=115)

    Label11 = tk.Label(formula_window,
                       text="Rectangle",
                       font=("Impact", 25),
                       bg='navajo white',
                       padx=20,
                       pady=10,
                       borderwidth=2)
    Label11.place(x=520, y=115)

    Label12 = tk.Label(formula_window,
                       text="Square",
                       font=("Impact", 25),
                       bg='navajo white',
                       padx=20,
                       pady=10,
                       borderwidth=2)
    Label12.place(x=770, y=115)

    def back_to_home():
        formula_window.destroy()
        open_main_window()

    button4 = tk.Button(formula_window,
                        text="Back to Home",
                        height=3,
                        width=15,
                        bg='gray20',
                        fg='white',
                        relief="raised",
                        command=back_to_home)
    button4.place(x=850, y=450)

    img_5 = ImageTk.PhotoImage(Image.open("Triangle.png").resize((250, 250)))
    Label13 = tk.Label(formula_window,
                       image=img_5,
                       bg='navajo white')
    Label13.image = img_5
    Label13.place(x=0, y=180)

    img_6 = ImageTk.PhotoImage(Image.open("Circle.png").resize((250, 250)))
    Label14 = tk.Label(formula_window,
                       image=img_6,
                       bg='navajo white')
    Label14.image = img_6
    Label14.place(x=260, y=170)

    img_7 = ImageTk.PhotoImage(Image.open("Rectangle.png").resize((250, 250)))
    Label15 = tk.Label(formula_window,
                       image=img_7,
                       bg='navajo white')
    Label15.image = img_7
    Label15.place(x=520, y=180)

    img_8 = ImageTk.PhotoImage(Image.open("Square.png").resize((230, 230)))
    Label16 = tk.Label(formula_window,
                       image=img_8,
                       bg='navajo white')
    Label16.image = img_8
    Label16.place(x=770, y=180)

    formula_window.mainloop()

def open_quiz_window():
    quiz_window = tk.Tk()
    quiz_window.title("Area Quiz")
    quiz_window.geometry("1000x540")
    quiz_window.configure(background='navajo white')

    label_quiz = tk.Label(quiz_window,
                          text="Quiz",
                          font=("Impact", 45),
                          bg='navajo white',
                          padx=20,
                          pady=10,
                          borderwidth=2)
    label_quiz.place(x=430, y=0)

    button_next = tk.Button(quiz_window,
                            text="Next Question",
                            height=3,
                            width=15,
                            bg='gray20',
                            fg='white',
                            relief="raised")
    button_next.place(x=215, y=460)

    button_exit = tk.Button(quiz_window,
                            text="Exit",
                            height=3,
                            width=15,
                            bg='gray20', fg='white', relief="raised", command=quiz_window.destroy)
    button_exit.place(x=50, y=460)

    img_5 = ImageTk.PhotoImage(Image.open("Star.png").resize((100, 100)))
    Label21 = tk.Label(quiz_window,
                       image=img_5,
                       bg='navajo white')
    Label21.image = img_5
    Label21.place(x=300, y=0)

    img_6 = ImageTk.PhotoImage(Image.open("Star.png").resize((100, 100)))
    Label22 = tk.Label(quiz_window,
                       image=img_6,
                       bg='navajo white')
    Label22.image = img_6
    Label22.place(x=600, y=0)

    answer_entry = None
    question_image_label = None
    option_buttons = []

    def load_question(question_data):
        nonlocal answer_entry, question_image_label, option_buttons
        label_question.config(text=question_data["Question"])
        options = question_data["options"]
        destroy_previous_question_widgets()

        if options:
            option_buttons = []
            for i, option in enumerate(options):
                btn = tk.Radiobutton(quiz_window,
                                     text=option,
                                     font=('Comic Sans Ms', 15),
                                     value=option,
                                     variable=r,
                                     bg='navajo white')
                btn.place(x=60, y=200 + i * 50)
                option_buttons.append(btn)
        else:
            answer_entry = tk.Entry(quiz_window,
                                    font=("Comic Sans MS", 15),
                                    width=30)
            answer_entry.place(x=50, y=200)

        if "image" in question_data:
            question_image = ImageTk.PhotoImage(Image.open(question_data["image"]).resize((350, 350)))
            question_image_label = tk.Label(quiz_window,
                                            image=question_image,
                                            bg='navajo white')
            question_image_label.image = question_image
            question_image_label.place(x=650, y=175)

    def destroy_previous_question_widgets():
        nonlocal answer_entry, question_image_label, option_buttons, r
        if answer_entry:
            answer_entry.destroy()
            answer_entry = None
        if question_image_label:
            question_image_label.destroy()
            question_image_label = None
        for btn in option_buttons:
            btn.destroy()
        option_buttons = []
        r.set(None)

    current_question_index = 0
    r = tk.StringVar()
    label_question = tk.Label(quiz_window, text="",
                              font=("Comic Sans MS", 17),
                              bg='navajo white',
                              padx=20,
                              pady=10,
                              borderwidth=2)
    label_question.place(x=50, y=125)
    load_question(Questions[current_question_index])
    correct_answers = 0

    def show_final_score():
        final_screen = tk.Toplevel(quiz_window)
        final_screen.title("Final Score")
        final_screen.geometry("500x550")
        final_screen.configure(background='navajo white')

        score_label = tk.Label(final_screen,
                               text=f"Your score is: {correct_answers}/{len(Questions)}",
                               font=("Comic Sans MS", 20),
                               bg='navajo white')
        score_label.pack(pady=20)

        percentage = (correct_answers / len(Questions)) * 100
        percentage_label = tk.Label(final_screen,
                                    text=f"Percentage: {percentage:.2f}%",
                                    font=("Comic Sans MS", 20),
                                    bg='navajo white')
        percentage_label.pack(pady=10)

        star_count = 0
        if correct_answers >= 13:
            star_count = 3
        elif correct_answers >= 8:
            star_count = 2
        elif correct_answers >= 1:
            star_count = 1

        star_img = ImageTk.PhotoImage(Image.open("Star.png").resize((75, 75)))
        for _ in range(star_count):
            star_label = tk.Label(final_screen,
                                  image=star_img,
                                  bg='navajo white')
            star_label.image = star_img
            star_label.pack(pady=10)

        def back_to_home():
            final_screen.destroy()
            quiz_window.destroy()
            open_main_window()

        button_backhome = tk.Button(final_screen,
                                    text="Back Home",
                                    height=3,
                                    width=15,
                                    bg='gray20',
                                    fg='white',
                                    relief="raised",
                                    command=back_to_home)
        button_backhome.place(x=10, y=475)

        button_exit = tk.Button(final_screen,
                                text="Exit",
                                height=3,
                                width=15,
                                bg='gray20',
                                fg='white',
                                relief="raised",
                                command=quiz_window.destroy)
        button_exit.place(x=350, y=475)

        quiz_window.withdraw()

    def next_question():
        nonlocal current_question_index, correct_answers
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
    quiz_window.mainloop()

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
    {"Question": "Question 10: What is the area of the circle with a diameter of 32?", "options": ["572π", "542π", "256π", "1024π"], "answer": "256π"},
    {"Question": "Question 11: What is the radius of a circle with an area of 2401π?", "options": ["49π", "98π", "65π", "1200π"], "answer": "49π"},
    {"Question": "Question 12 CHALLENGE: What is the area of the following composite shape?", "options": None, "answer": "57", "image": "img11.png"},
    {"Question": "Question 13 CHALLENGE: What is the area of the following composite shape?", "options": None, "answer": "96", "image": "img12.png"},
    {"Question": "Question 14 CHALLENGE: What is the shaded area of the following shape?", "options": None, "answer": "54", "image": "img13.png"},
    {"Question": "Question 15 CHALLENGE: What is the area of the arrow?", "options": None, "answer": "57", "image": "img14.png"},
]
open_main_window()