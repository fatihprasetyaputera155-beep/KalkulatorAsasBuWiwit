import tkinter as tk

class Calculator:
    pass
def on_button_click(value):
    current = entry.get()
    if value == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif value == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, value)

root = tk.Tk()
root.title("ProjectCalculattorAsas")
root.geometry("400x530")
root.config(bg="#90e0ef")

entry = tk.Entry(root, font=("Sans", 24), width=20, borderwidth=10, relief="raised", bg="black", fg="white", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=15)

buttons = [
    ("C", 1, 0), ("%", 1, 1), ("=", 4, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), 
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), 
    ("0", 5, 0), (".", 5, 1)
]

buttons2 = [
    ("/", 1, 2),
    ("-", 1, 3),
    ]

buttons3 = [
     ("*", 2, 3),
     ("+", 3, 3),
  
    ]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 18), relief ="raised" , bg="#beedf4", fg="black", width=5, height=2, command=lambda value=text: on_button_click(value))
    button.grid(row=row, column=col, padx=10,pady=5)

for (text, row, col) in buttons2:
    button = tk.Button(root, text=text, font=("Arial", 18), relief="raised", bg="#beedf4", fg="#ef6666", width=5, height=2, command=lambda value=text: on_button_click(value))
    button.grid(row=row, column=col, padx=10,pady=5)

for (text, row, col) in buttons3:
    button = tk.Button(root, text=text, font=("Arial", 18), relief="raised", bg="#beedf4", fg="#77dd77", width=5, height=2, command=lambda value=text: on_button_click(value))
    button.grid(row=row, column=col, padx=10,pady=5)


root.mainloop()