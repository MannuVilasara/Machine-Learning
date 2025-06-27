from tkinter import *
from joblib import load

model = load("model.joblib")

root = Tk()
root.title("Performance Index Predictor")
root.geometry("400x300")


def predict_performance_index():
    try:
        study_hours = float(study_hours_entry.get())
        papers_practiced = float(papers_practiced_entry.get())
        prediction = model.predict([[study_hours, papers_practiced]])
        result_label.config(text=f"Performance Index: {prediction[0]:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")


Label(root, text="Performance Index Predictor", font=("Arial", 16)).pack(pady=10)
Label(root, text="Enter Study Hours:").pack(pady=5)
study_hours_entry = Entry(root)
study_hours_entry.pack(pady=5)

Label(root, text="Enter Papers Practiced:").pack(pady=5)
papers_practiced_entry = Entry(root)
papers_practiced_entry.pack(pady=5)

Button(root, text="Predict", command=predict_performance_index).pack(pady=10)
result_label = Label(root, text="", fg="blue", font=("Arial", 12))
result_label.pack(pady=5)

root.mainloop()
