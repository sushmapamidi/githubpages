import tkinter as tk
def on_button_click():
    label.config(text="Button Clicked!",font='bold')
# Create the main Tkinter window
window = tk.Tk()
window.title("Simple GUI Program")

label = tk.Label(window, text="welcome!")
label.pack(pady=20)
button = tk.Button(window, text="Click Me", command=on_button_click,bg='skyblue')
button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
