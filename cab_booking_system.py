import tkinter as tk
from tkinter import messagebox
import random
from datetime import datetime

# Fare rates per km for each cab type
FARE_RATES = {
    "Mini": 10,
    "Sedan": 15,
    "SUV": 20
}

def calculate_fare():
    try:
        pickup = entry_pickup.get()
        drop = entry_drop.get()
        distance = float(entry_distance.get())
        cab_type = cab_var.get()

        if not pickup or not drop or cab_type not in FARE_RATES:
            raise ValueError("Incomplete or invalid data")

        fare = distance * FARE_RATES[cab_type]
        booking_id = random.randint(10000, 99999)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        result = (
            f"Booking ID: #{booking_id}\n"
            f"Time: {timestamp}\n"
            f"Pickup: {pickup}\n"
            f"Drop: {drop}\n"
            f"Cab Type: {cab_type}\n"
            f"Distance: {distance} km\n"
            f"Estimated Fare: ₹{fare:.2f}"
        )

        text_output.config(state='normal')
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, result)
        text_output.config(state='disabled')

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid input for all fields.")

# GUI setup
root = tk.Tk()
root.title("Cab Booking System")
root.geometry("400x500")
root.resizable(False, False)

tk.Label(root, text="Cab Booking System", font=("Helvetica", 16, "bold")).pack(pady=10)

tk.Label(root, text="Pickup Location").pack()
entry_pickup = tk.Entry(root, width=30)
entry_pickup.pack()

tk.Label(root, text="Drop Location").pack()
entry_drop = tk.Entry(root, width=30)
entry_drop.pack()

tk.Label(root, text="Distance (in km)").pack()
entry_distance = tk.Entry(root, width=30)
entry_distance.pack()

tk.Label(root, text="Cab Type").pack()
cab_var = tk.StringVar()
cab_var.set("Mini")
tk.OptionMenu(root, cab_var, *FARE_RATES.keys()).pack()

tk.Button(root, text="Book Now", command=calculate_fare, bg="green", fg="white", padx=10, pady=5).pack(pady=15)

tk.Label(root, text="Booking Summary").pack()
text_output = tk.Text(root, height=10, width=45, state='disabled', borderwidth=2, relief="groove")
text_output.pack()

root.mainloop()
