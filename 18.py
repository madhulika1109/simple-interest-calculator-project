import tkinter as tk
from tkinter import messagebox

# Function to calculate simple interest
def calculate_si():
    try:
        # Get user input values
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        time = float(time_entry.get())

        # Calculate simple interest
        si = (principal * rate * time) / 100
        total = principal + si

        # Display result
        result_label.config(text=f"Simple Interest: ₹{si:.2f}\nTotal Amount: ₹{total:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")

# Create main window
root = tk.Tk()
root.title("Simple Interest Calculator")
root.geometry("350x300")
root.config(bg="lightblue")

# Title Label
tk.Label(root, text="Simple Interest Calculator", font=("Arial", 16, "bold"), bg="lightblue", fg="black").pack(pady=10)

# Input fields
tk.Label(root, text="Principal Amount (₹):", bg="lightblue").pack()
principal_entry = tk.Entry(root, width=25)
principal_entry.pack(pady=5)

tk.Label(root, text="Rate of Interest (%):", bg="lightblue").pack()
rate_entry = tk.Entry(root, width=25)
rate_entry.pack(pady=5)

tk.Label(root, text="Time (years):", bg="lightblue").pack()
time_entry = tk.Entry(root, width=25)
time_entry.pack(pady=5)

# Calculate button
tk.Button(root, text="Calculate", command=calculate_si, bg="black", fg="white", width=15, font=("Arial", 10, "bold")).pack(pady=10)

# Result label
result_label = tk.Label(root, text="", bg="lightblue", font=("Arial", 12, "bold"), fg="black")
result_label.pack(pady=10)

# Run the GUI loop
root.mainloop()
