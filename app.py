import tkinter as tk
from tkinter import messagebox
import main

# Create main window
root = tk.Tk()
root.title("TikTok")

# Configure column widths
root.columnconfigure(0, weight=1, minsize=100)
root.columnconfigure(1, weight=2, minsize=200)
root.columnconfigure(2, weight=1, minsize=100)

# Biến lưu trạng thái của radio button
selected_option = tk.StringVar(value="Option 1")  # Giá trị mặc định
selected_option2 = tk.StringVar(value="Option 1")  # Giá trị mặc định

# First row
label = tk.Label(root, text="Số video xem:")
label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

# Second row
label = tk.Label(root, text="Có muốn tim video:")
label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

radio1 = tk.Radiobutton(root, text="Có", variable=selected_option, value="Có")
radio2 = tk.Radiobutton(root, text="Không", variable=selected_option, value="Không")

radio1.grid(row=1, column=1, padx=5, pady=5, sticky="w")
radio2.grid(row=1, column=2, padx=5, pady=5, sticky="w")

# Third row
label = tk.Label(root, text="Có muốn bình luận:")
label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

radio3 = tk.Radiobutton(root, text="Có", variable=selected_option2, value="Có")
radio4= tk.Radiobutton(root, text="Không", variable=selected_option2, value="Không")

radio3.grid(row=2, column=1, padx=5, pady=5, sticky="w")
radio4.grid(row=2, column=2, padx=5, pady=5, sticky="w")

# Fourth row
button = tk.Button(root, text="Submit")
button.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

# Run the application
root.mainloop()