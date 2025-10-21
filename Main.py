import tkinter as tk

count = 0

def add():
    global count
    count += 1
    label.config(text=f"Count: {count}")
    if count >= 10:
        label.config(text="YOU DID IT!")
        button.pack_forget()

root = tk.Tk()
root.title("Job Tracker")
root.geometry("250x100")

label = tk.Label(root, text=f"Count: {count}")
label.pack(anchor='center', expand=True)

# Button to up value
button = tk.Button(root, text="Anotha one!", command=add)
button.pack(anchor='center', expand=True)

root.mainloop()