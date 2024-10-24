from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
data_dict = data.to_dict(orient="records")


def new_random_word():
    global timer, current_card
    window.after_cancel(timer)
    canvas.itemconfig(canvas_image, image=card_front)
    current_card = choice(data_dict)
    canvas.itemconfig(language_word, text="French", fill="Black")
    canvas.itemconfig(word_in_card, text=current_card["French"], fill="Black")
    timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(language_word, text="English", fill="White")
    canvas.itemconfig(word_in_card, text=current_card["English"], fill="White")


def check_card():
    data_dict.remove(current_card)
    new_data = pandas.DataFrame(data_dict)
    new_data.to_csv("data/french_words.csv", index=False)
    new_random_word()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, flip_card)

current_card = choice(data_dict)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
language_word = canvas.create_text(400, 150, text="French", font=("Arial", 32, "italic"))
word_in_card = canvas.create_text(400, 263, text=current_card["French"], font=("Ariel", 45, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Labels
# language_label = Label(text="French", font=("Ariel", 32, "italic"), bg="white")
# language_label.place(x=325, y=130) # Also works
#
# word_label = Label(text="trouve", font=("Ariel", 45, "bold"), bg="white")
# word_label.place(x=300, y=225) # Also works

# Buttons (❌ and ✅)
wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=new_random_word)
wrong_button.grid(column=0, row=1)

right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=check_card)
right_button.grid(column=1, row=1)

window.mainloop()
