import tkinter as tk
from tkinter import messagebox

def validate_login():
    user_id = entry_user_id.get()
    password = entry_password.get()

    # Replace this with your actual login logic
    if user_id == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid user ID or password. Try again.")

# Create the main Tkinter window
root = tk.Tk()
root.title("Login Form")

label_user_id = tk.Label(root, text="User ID:", font=('Arial', 14))
label_user_id.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)

entry_user_id = tk.Entry(root, font=('Arial', 14))
entry_user_id.grid(row=0, column=1, padx=10, pady=10)

label_password = tk.Label(root, text="Password:", font=('Arial', 14))
label_password.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)

entry_password = tk.Entry(root, show="*", font=('Arial', 14))
entry_password.grid(row=1, column=1, padx=10, pady=10)

# Create and place a button to validate the login
login_button = tk.Button(root, text="Login", command=validate_login, font=('Arial', 14))
login_button.grid(row=2, column=0, columnspan=2, pady=20)

# Run the Tkinter event loop
root.mainloop()
