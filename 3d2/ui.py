from tkinter import *
from joblib import load

model = load("model.joblib")

root = Tk()
root.title("Revenue Predictor")
root.geometry("400x300")


def predict_revenue():
    try:
        funding = float(funding_entry.get())
        team = float(team_entry.get())
        prediction = model.predict([[funding, team]])
        result_label.config(text=f"Predicted Revenue in 1 Year: ${prediction[0]:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")


Label(root, text="Revenue Predictor", font=("Arial", 16)).pack(pady=10)
Label(root, text="Enter Funding Amount in USD:").pack(pady=5)
funding_entry = Entry(root)
funding_entry.pack(pady=5)

Label(root, text="Enter Team Size:").pack(pady=5)
team_entry = Entry(root)
team_entry.pack(pady=5)

Button(root, text="Predict", command=predict_revenue).pack(pady=10)
result_label = Label(root, text="", fg="blue", font=("Arial", 12))
result_label.pack(pady=5)

root.mainloop()
