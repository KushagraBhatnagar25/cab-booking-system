import tkinter as tk
from tkinter import messagebox

# Fare rates per km for each cab type
FARE_RATES = {
    "Mini": 10,
    "Sedan": 15,
    "SUV": 20
}

def calculate_fare():
    try:
        distance = float(entry_distance.get())
        cab_type = cab_var.get()

        if cab_type not in FARE_RATES:
            raise ValueError("Invalid cab type selected")

        fare = distance * FARE_RATES[cab_type]

        result = (
            f"Pickup: {entry_pickup.get()}\n"
            f"Drop: {entry_drop.get()}\n"
            f"Cab Type: {cab_type}\n"
            f"Distance: {distance} km\n"
            f"Estimated Fare: ₹{fare:.2f}"
        )
        text_output.config(state='normal')
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, result)
        text_output.config(state='disabled')

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for distance.")

# GUI setup
root = tk.Tk()
root.title("Cab Booking System")
root.geometry("400x400")

tk.Label(root, text="Pickup Location").pack()
entry_pickup = tk.Entry(root)
entry_pickup.pack()

tk.Label(root, text="Drop Location").pack()
entry_drop = tk.Entry(root)
entry_drop.pack()

tk.Label(root, text="Distance (in km)").pack()
entry_distance = tk.Entry(root)
entry_distance.pack()

tk.Label(root, text="Select Cab Type").pack()
cab_var = tk.StringVar()
cab_var.set("Mini")
cab_options = tk.OptionMenu(root, cab_var, *FARE_RATES.keys())
cab_options.pack()

tk.Button(root, text="Calculate Fare", command=calculate_fare).pack(pady=10)

text_output = tk.Text(root, height=10, state='disabled')
text_output.pack()

root.mainloop()
