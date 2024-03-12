import tkinter as tk
from tkinter import colorchooser

def choose_color():
    color_code, color_name = colorchooser.askcolor(title="Choose Your Favorite Color")
    if color_name:
        color_label.config(text=f"Your Favorite Color: {color_name}")
        color_label.config(bg=color_code)
        color_button.config(bg=color_code)

# Create the main Tkinter window
root = tk.Tk()
root.title("Color Picker App")

# Create and place a button to open the color picker
color_button = tk.Button(root, text="Choose Color", command=choose_color)
color_button.pack(pady=20)

# Create and place a label to display the selected color
color_label = tk.Label(root, text="Your Favorite Color:", font=('Arial', 14), pady=10)
color_label.pack()

# Run the Tkinter event loop
root.mainloop()
