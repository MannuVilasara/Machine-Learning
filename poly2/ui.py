from tkinter import *
from joblib import load
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=3)
model = load("model.joblib")

root = Tk()
root.geometry("400x300")
root.title("Productivity calculator")


def calculate_productivity():
    try:
        caffeine_deviation = float(caffeine_entry.get())
        productivity = model.predict(poly.fit_transform([[caffeine_deviation]]))
        result_label.config(text=f"Estimated Productivity: {productivity[0]:.2f}")
    except ValueError as e:
        result_label.config(text=f"Error: {e}")
    except Exception as e:
        result_label.config(text="An unexpected error occurred.")


Label(root, text="Productivity Calculator", font=("Arial", 16)).pack(pady=10)
Label(root, text="Enter the Caffeine Deviation:").pack(pady=5)
caffeine_entry = Entry(root)
caffeine_entry.pack(pady=5)

Button(root, text="Calculate", command=calculate_productivity).pack(pady=10)
result_label = Label(root, text="", fg="blue", font=("Arial", 12))
result_label.pack(pady=5)

root.mainloop()
