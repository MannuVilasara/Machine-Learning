from tkinter import *
from joblib import load
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=3)

model = load("model.joblib")

root = Tk()
root.geometry("400x300")
root.title("Fuel Consumption Calculator")


def calculate_consumption():
    try:
        slope = float(slope_entry.get())
        consumption = model.predict(poly.fit_transform([[slope]]))
        result_label.config(text=f"Estimated Fuel Consumption: {consumption[0]:.2f} L")
    except ValueError as e:
        result_label.config(text=f"Error: {e}")
    except Exception as e:
        result_label.config(text="An unexpected error occurred.")


Label(root, text="Fuel Consumption Calculator", font=("Arial", 16)).pack(pady=10)
Label(root, text="Enter the slope of Road:").pack(pady=5)
slope_entry = Entry(root)
slope_entry.pack(pady=5)

Button(root, text="Calculate", command=calculate_consumption).pack(pady=10)
result_label = Label(root, text="", fg="blue", font=("Arial", 12))
result_label.pack(pady=5)

root.mainloop()
