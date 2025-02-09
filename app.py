import tkinter as tk
from tkinter import messagebox

# Function to handle button click
def on_button_click():
    label.config(text="Button Clicked!")

def show_message():
    value = entry.get()
    messagebox.showinfo("Info", f"You entered: {value}")

# Create main window
root = tk.Tk()
root.title("TikTok")

# Configure column widths
root.columnconfigure(0, weight=1, minsize=100)
root.columnconfigure(1, weight=2, minsize=200)
root.columnconfigure(2, weight=1, minsize=100)

# First row
label = tk.Label(root, text="Số video xem:")
label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

# Second row
button = tk.Button(root, text="Submit", command=show_message)
button.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

# Allow resizing

# Run the application
root.mainloop()
