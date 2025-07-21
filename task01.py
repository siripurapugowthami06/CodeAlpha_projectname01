import tkinter as tk
import random

quotes = [
    ("The best way to get started is to quit talking and begin doing.", "Walt Disney"),
    ("Success is not in what you have, but who you are.", "Bo Bennett"),
    ("Your time is limited, so don’t waste it living someone else’s life.", "Steve Jobs")
]

def new_quote():
    quote, author = random.choice(quotes)
    quote_label.config(text=f'"{quote}"')
    author_label.config(text=f"- {author}")

app = tk.Tk()
app.title("Random Quote Generator")

quote_label = tk.Label(app, text="", wraplength=400, font=("Arial", 12), pady=20)
quote_label.pack()

author_label = tk.Label(app, text="", font=("Arial", 10, "italic"))
author_label.pack()

button = tk.Button(app, text="New Quote", command=new_quote)
button.pack(pady=10)

new_quote()
app.mainloop()