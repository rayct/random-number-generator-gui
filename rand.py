
### Version 1.0.1-beta.1

import tkinter as tk
from tkinter import messagebox
import random
import os

def generate_numbers():
    """
    Generate random numbers based on the provided inputs and display them in the output text box.
    """
    try:
        input_numbers = [int(num) for num in num_entry.get().split(",")]
        input_weights = [int(weight) for weight in weight_entry.get().split(",")]
        num_samples = int(num_samples_entry.get())

        if len(input_numbers) != len(set(input_numbers)):
            messagebox.showerror("Input Error", "Duplicate numbers detected. Please provide unique numbers.")
            return

        # Shuffle input_numbers to ensure uniqueness
        shuffled_numbers = input_numbers.copy()
        random.shuffle(shuffled_numbers)

        random_numbers = random.choices(shuffled_numbers, weights=input_weights, k=num_samples)
        output_text.config(state=tk.NORMAL)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Generated Random Numbers: " + ", ".join(map(str, random_numbers)) + "\n")
        output_text.config(state=tk.DISABLED)

        log_directory = "logs"
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)
        log_filename = os.path.join(log_directory, f"log_{os.getpid()}.txt")  # Use process ID to generate unique log file name

        with open(log_filename, "a", encoding="utf-8") as log_file:
            log_file.write("Generated Numbers: " + ", ".join(map(str, random_numbers)) + "\n")

    except ValueError:
        messagebox.showerror("Input Error", "Invalid input format. Please enter valid numbers and weights.")

def open_log_file():
    """
    Open the log.txt file using the default text editor.
    """
    try:
        log_directory = "logs"
        log_filename = os.path.join(log_directory, f"log_{os.getpid()}.txt")  # Use process ID to open the correct log file

        if os.name == "nt":
            os.system(f"start {log_filename}")  # For Windows
        elif os.name == "posix":
            os.system(f"open {log_filename}")  # For macOS
        else:
            os.system(f"xdg-open {log_filename}")  # For Linux
    except FileNotFoundError:
        messagebox.showerror("Error", "Log file not found.")
    except OSError as os_error:
        messagebox.showerror("Error", f"Error opening log file: {os_error}")

# Create the main window
root = tk.Tk()
root.title("Random Number Generator")
root.geometry("600x600")

# Create labels and entry fields
tk.Label(root, text="Enter Numbers (comma-separated):").grid(row=0, column=0, padx=20, pady=10, sticky="e")
num_entry = tk.Entry(root)
num_entry.grid(row=0, column=1, padx=20, pady=10, columnspan=2)
num_entry.config(width=int(num_entry.cget("width")) * 3 // 2)  # Adjust width

tk.Label(root, text="Enter Weights (comma-separated):").grid(row=1, column=0, padx=20, pady=10, sticky="e")
weight_entry = tk.Entry(root)
weight_entry.grid(row=1, column=1, padx=20, pady=10, columnspan=2)
weight_entry.config(width=int(weight_entry.cget("width")) * 3 // 2)  # Adjust width

tk.Label(root, text="Number of Samples:").grid(row=2, column=0, padx=20, pady=10, sticky="e")
num_samples_entry = tk.Entry(root)
num_samples_entry.grid(row=2, column=1, padx=20, pady=10, columnspan=2)
num_samples_entry.config(width=int(num_samples_entry.cget("width")) * 3 // 2)  # Adjust width

# Create Generate button
generate_button = tk.Button(root, text="Generate Numbers", command=generate_numbers)
generate_button.grid(row=3, column=0, columnspan=3, padx=20, pady=20)

# Create Open Log button
open_log_button = tk.Button(root, text="Open Log File", command=open_log_file)
open_log_button.grid(row=4, column=0, columnspan=3, padx=20, pady=10)

# Create output text box
output_text = tk.Text(root, height=15, width=50, state=tk.DISABLED)
output_text.grid(row=5, column=0, columnspan=3, padx=20, pady=10)

# Add a scrollbar to the output text box
scrollbar = tk.Scrollbar(root, command=output_text.yview)
scrollbar.grid(row=5, column=3, sticky="ns")
output_text.config(yscrollcommand=scrollbar.set)

# Start the GUI event loop
root.mainloop()
