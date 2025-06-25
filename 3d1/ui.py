from tkinter import *
from joblib import load

model = load('model.joblib')

root = Tk()
root.title("Battery Life Predictor")
root.geometry("400x300")

def predict_battery_life():
    try:
        screen_time = float(screen_time_entry.get())
        app_usage = float(app_usage_entry.get())
        prediction = model.predict([[screen_time, app_usage]])
        result_label.config(text=f"Predicted Battery Life: {prediction[0]:.2f} hours")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

Label(root, text="Battery Life Predictor", font=("Arial", 16)).pack(pady=10)
Label(root, text="Enter ScreenTime in Hours:").pack(pady=5)
screen_time_entry = Entry(root)
screen_time_entry.pack(pady=5)

Label(root, text="Enter App Usage:").pack(pady=5)
app_usage_entry = Entry(root)
app_usage_entry.pack(pady=5)

Button(root, text="Predict", command=predict_battery_life).pack(pady=10)
result_label = Label(root, text="", fg="blue", font=("Arial", 12))
result_label.pack(pady=5)

root.mainloop()