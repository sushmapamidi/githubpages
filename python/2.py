import tkinter as tk

def send_message():
    user_message = user_input.get()
    chat_history.insert(tk.END, f"User: {user_message}\n")

    # Simple chatbot response
    if "is python oop" in user_message.lower():
        chat_history.insert(tk.END, "Chatbot: yes python is oop!\n")
    elif "bye" in user_message.lower():
        chat_history.insert(tk.END, "Chatbot: Goodbye!\n")
    else:
        chat_history.insert(tk.END, "Chatbot: I'm just a basic chatbot. Ask me anything!\n")

    user_input.delete(0, tk.END)

# Create the main Tkinter window
window = tk.Tk()
window.title("Simple Chatbot GUI")

# Create and place a text widget for chat history
chat_history = tk.Text(window, width=40, height=10)
chat_history.pack(padx=10, pady=10)

# Create and place an entry widget for user input
user_input = tk.Entry(window, width=40)
user_input.pack(pady=10)

# Create and place a button to send messages
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack()

# Run the Tkinter event loop
window.mainloop()
