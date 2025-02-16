import tkinter as tk
from tkinter import messagebox, ttk
import pyperclip


# Function to convert the number between different bases
def convert_base(number: str, from_base: int, to_base: int) -> str:
    """ Convert a number from one base to another."""
    try:
        decimal_number = int(number, from_base)  # Convert to decimal
        if to_base == 10:
            return str(decimal_number)

        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        while decimal_number > 0:
            result = digits[decimal_number % to_base] + result
            decimal_number //= to_base
        return result or "0"
    except ValueError:
        return "Invalid Input"


# Function to handle conversion
def on_convert():
    number = entry_number.get().upper()
    from_base = int(from_base_var.get())
    to_base = int(to_base_var.get())

    result = convert_base(number, from_base, to_base)
    label_result.config(text=f"Result: {result}")

    if result != "Invalid Input":
        history_list.insert(0, f"{number} ({from_base}) → {result} ({to_base})")
        history_list.delete(5, tk.END)  # Keep only last 5 results


def copy_to_clipboard():
    pyperclip.copy(label_result.cget("text").replace("Result: ", ""))
    messagebox.showinfo("Copied", "Result copied to clipboard!")


# Create main window
window = tk.Tk()
window.title("Base Converter")
window.geometry("400x400")
window.configure(bg="#121212")

# Define custom font
font_style = ("Grostick", 12)

# Title
label_title = tk.Label(window, text="Base Converter", font=("Grostick", 16, "bold"), bg="#121212", fg="white")
label_title.pack(pady=10)

# Number Input
entry_number = tk.Entry(window, font=font_style, width=20, bg="#1E1E1E", fg="white", insertbackground="white")
entry_number.pack(pady=5)

# Base Selection Dropdowns
from_base_var = tk.StringVar(value="10")
to_base_var = tk.StringVar(value="2")
base_options = [str(i) for i in range(2, 37)]

label_from_base = tk.Label(window, text="From Base:", font=font_style, bg="#121212", fg="white")
label_from_base.pack()
from_base_menu = ttk.Combobox(window, textvariable=from_base_var, values=base_options, font=font_style,
                              state="readonly")
from_base_menu.pack()

label_to_base = tk.Label(window, text="To Base:", font=font_style, bg="#121212", fg="white")
label_to_base.pack()
to_base_menu = ttk.Combobox(window, textvariable=to_base_var, values=base_options, font=font_style, state="readonly")
to_base_menu.pack()

# Convert Button
button_convert = tk.Button(window, text="Convert", command=on_convert, font=font_style, bg="#F57C00", fg="black",
                           width=20)
button_convert.pack(pady=10)

# Result Display
label_result = tk.Label(window, text="Result: ", font=("Grostick", 14, "bold"), bg="#121212", fg="white")
label_result.pack(pady=5)

# Copy to Clipboard Button
button_copy = tk.Button(window, text="Copy Result", command=copy_to_clipboard, font=font_style, bg="#F57C00",
                        fg="black", width=20)
button_copy.pack(pady=5)

# Conversion History
history_label = tk.Label(window, text="History:", font=font_style, bg="#121212", fg="white")
history_label.pack()

history_list = tk.Listbox(window, font=font_style, bg="#1E1E1E", fg="white", width=40, height=5)
history_list.pack()

# Run the application
window.mainloop()
