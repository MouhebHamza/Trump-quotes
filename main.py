from tkinter import *
import requests


def get_quote():
    response = requests.get(url="https://api.whatdoestrumpthink.com/api/v1/quotes/random/")
    response.raise_for_status()
    data = response.json()
    quote = data["message"]
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Trump Says...")
window.config(padx=50, pady=20)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png", width=300, height=414)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 200, text="Trump Quotes Generator\n\n\n\n \t M hamza", width=250,
                                font=("Arial", 15, "bold"), fill="white")
canvas.grid(row=0, column=0, pady=20)

trump_img = PhotoImage(file="trump.png")
trump_button = Button(image=trump_img, highlightthickness=0, command=get_quote, width=100, height=131)
trump_button.grid(row=1, column=0)

window.mainloop()
