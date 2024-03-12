import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")

# Create the main Tkinter window
window = tk.Tk()
window.title("GUI with Image")

# Load the image (replace "path/to/your/image/logo.png" with your image file)
img = tk.PhotoImage(file="C:/Users/marut/Desktop/pythonproject/venv/source/jaddu.jpeg")


# Create and place a label with the image
image_label = tk.Label(window, image=img)
image_label.pack(pady=10)

# Create and customize a button
button = tk.Button(window, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Create and place a label for displaying text
label = tk.Label(window, text="Welcome to GUI with Image")
label.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
