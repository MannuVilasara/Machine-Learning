from tkinter import *
import joblib
from tkinter import messagebox

model = joblib.load("linear_regression_model.joblib")


def predict_books():
    try:
        hours = float(HoursEntry.get())
        if hours < 0:
            raise ValueError("Hours cannot be negative.")
        books = model.predict([[hours]])[0]
        messagebox.showinfo(
            "Prediction",
            f"You can read approximately {int(books)} books in {hours} hours.",
        )
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))


root = Tk()
root.title("Books read in hours")
root.geometry("400x300")

TitleLabel = Label(root, text="Enter The Number of Hours:", font=("Arial", 16))
TitleLabel.pack(pady=20)

HoursEntry = Entry(root, font=("Arial", 16))
HoursEntry.pack(pady=10)

SubmitButton = Button(root, text="Books", font=("Arial", 16), command=predict_books)
SubmitButton.pack(pady=20)

root.mainloop()

