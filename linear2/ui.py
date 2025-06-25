from tkinter import *
import joblib
from tkinter import messagebox

model = joblib.load("linear_regression_model.joblib")

root = Tk()
root.title("Size to Rent ratio")
root.geometry("400x300")

TitleLabel = Label(root, text="Enter The Size of the House:", font=("Arial", 16))
TitleLabel.pack(pady=20)

SizeEntry = Entry(root, font=("Arial", 16))
SizeEntry.pack(pady=10)


def predict_rent_ratio():
    try:
        size = float(SizeEntry.get())
        if size < 260:
            raise ValueError("Size cannot be less than 260 square feet.")
        ratio = model.predict([[size]])[0]
        messagebox.showinfo(
            "Prediction", f"The predicted rent-to-size ratio is: {ratio:.2f}"
        )
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))


SubmitButton = Button(
    root, text="Submit", font=("Arial", 16), command=predict_rent_ratio
)
SubmitButton.pack(pady=20)

root.mainloop()

