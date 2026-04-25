import re
import tkinter as tk

# Rule base (pattern → response)
rules = [
    ("hello(X)", "Hello X! How can I help you?"),
    ("order(X)", "Your order for X has been placed."),
    ("bye", "Goodbye!")
]

# Unification function
def unify(pattern, user_input):
    pattern = pattern.replace("(", "\\(").replace(")", "\\)")
    pattern = pattern.replace("X", "(.*)")
    
    match = re.match(pattern, user_input)
    if match:
        return match.group(1) if match.groups() else None
    return None

# Find best match
def get_response(user_input):
    for pattern, response in rules:
        result = unify(pattern, user_input)
        if result is not None:
            return pattern, response.replace("X", result)
    return "No match", "Sorry, I didn't understand."

# GUI
def send():
    user_input = entry.get()
    pattern, reply = get_response(user_input)

    output.delete("1.0", tk.END)
    output.insert(tk.END, f"User Input: {user_input}\n")
    output.insert(tk.END, f"Matched Rule: {pattern}\n")
    output.insert(tk.END, f"Response: {reply}")

# GUI window
root = tk.Tk()
root.title("AI Chatbot Logic Engine")

entry = tk.Entry(root, width=40)
entry.pack()

button = tk.Button(root, text="Send", command=send)
button.pack()

output = tk.Text(root, height=10, width=50)
output.pack()

root.mainloop()
