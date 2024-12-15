import tkinter as tk
from tkinter import messagebox
import pyttsx3  

 
engine = pyttsx3.init()

def play_text():

    text = entry.get()
    if text.strip():
        engine.say(text)
        engine.runAndWait()
    else:
        messagebox.showwarning

def clear_text():
    
    entry.delete(0, tk.END)

def exit_program():
    
    root.destroy()


root = tk.Tk()
root.title("Text to Speech GUI")
root.geometry("400x200")  


tk.Label(root, text="Enter your text:").pack(pady=10)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)


play_button = tk.Button(root, text="Play", command=play_text, bg="lightgreen", width=10)
play_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", command=exit_program, bg="red", fg="white", width=10)
exit_button.pack(pady=5)

set_button = tk.Button(root, text="Set", command=clear_text, bg="lightblue", width=10)
set_button.pack(pady=5)


root.mainloop()