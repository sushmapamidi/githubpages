import tkinter as tk

def convert_temperature():
    try:
        temperature = float(entry.get())
        if var.get() == 1:  # Celsius to Fahrenheit
            result = (temperature * 9/5) + 32
            result_label.config(text=f"Result: {result:.2f} °F")
        elif var.get() == 2:  # Fahrenheit to Celsius
            result = (temperature - 32) * 5/9
            result_label.config(text=f"Result: {result:.2f} °C")
    except ValueError:
        result_label.config(text="Invalid input. Enter a valid number.")

# Create the main Tkinter window
root = tk.Tk()
root.title("Temperature Converter")

# Create and place entry widget for temperature input
entry = tk.Entry(root, font=('Arial', 14))
entry.pack(pady=10)

# Create a radio button to choose the conversion direction
var = tk.IntVar()
celsius_to_fahrenheit = tk.Radiobutton(root, text="Celsius to Fahrenheit", variable=var, value=1)
fahrenheit_to_celsius = tk.Radiobutton(root, text="Fahrenheit to Celsius", variable=var, value=2)

celsius_to_fahrenheit.pack()
fahrenheit_to_celsius.pack()

# Create and place a button to perform the conversion
convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack(pady=20)

# Create and place a label for displaying the result
result_label = tk.Label(root, text="Result:", font=('Arial', 14))
result_label.pack()

# Run the Tkinter event loop
root.mainloop()
