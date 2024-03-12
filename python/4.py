import tkinter as tk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")

        self.entry = tk.Entry(master, width=20, font=('Arial', 16), justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, pady=10)

        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', 'C', '=', '+')
        ]

        for i, row in enumerate(buttons, start=1):
            for j, text in enumerate(row):
                button = tk.Button(master, text=text, width=5, height=2, command=lambda t=text: self.on_button_click(t))
                button.grid(row=i, column=j, padx=5, pady=5)

    def on_button_click(self, value):
        if value == 'C':
            self.clear_entry()
        elif value == '=':
            self.calculate_result()
        else:
            current = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current + str(value))

    def clear_entry(self):
        self.entry.delete(0, tk.END)

    def calculate_result(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

# Create the main Tkinter window
root = tk.Tk()
app = CalculatorApp(root)

# Run the Tkinter event loop
root.mainloop()
