import tkinter as tk
from tkinter import messagebox
from utils import caesar_encrypt, caesar_decrypt

def process_text():
    text = text_entry.get()
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")
        return

    if mode.get() == "Encrypt":
        result = caesar_encrypt(text, shift)
    else:
        result = caesar_decrypt(text, shift)

    result_label.config(text=f"Result: {result}")

window = tk.Tk()
window.title("Caesar Cipher")
window.geometry("500x350")
window.configure(bg="#FFFFFF")

title_label = tk.Label(window, text="Caesar Cipher", font=("Arial", 18, "bold"), bg="#FFFFFF", fg="#333333")
title_label.pack(pady=15)

tk.Label(window, text="Shift Value:", font=("Arial", 10), bg="#FFFFFF", fg="#333333").pack(pady=5)
shift_entry = tk.Entry(window, width=10, font=("Arial", 10), bg="#F0F0F0", fg="#333333", insertbackground="#333333", relief="flat", highlightbackground="#CCCCCC", highlightthickness=1)
shift_entry.pack(pady=5)

tk.Label(window, text="Enter Text:", font=("Arial", 10), bg="#FFFFFF", fg="#333333").pack(pady=5)
text_entry = tk.Entry(window, width=50, font=("Arial", 10), bg="#F0F0F0", fg="#333333", insertbackground="#333333", relief="flat", highlightbackground="#CCCCCC", highlightthickness=1)
text_entry.pack(pady=5)

mode = tk.StringVar(value="Encrypt")
frame = tk.Frame(window, bg="#FFFFFF")
frame.pack(pady=10)

encrypt_button = tk.Radiobutton(frame, text="Encrypt", variable=mode, value="Encrypt", bg="#FFFFFF", fg="#333333", selectcolor="#DDDDDD", activebackground="#DDDDDD", activeforeground="#000000", font=("Arial", 10))
decrypt_button = tk.Radiobutton(frame, text="Decrypt", variable=mode, value="Decrypt", bg="#FFFFFF", fg="#333333", selectcolor="#DDDDDD", activebackground="#DDDDDD", activeforeground="#000000", font=("Arial", 10))
encrypt_button.pack(side="left", padx=15)
decrypt_button.pack(side="left", padx=15)

process_button = tk.Button(window, text="Process", command=process_text, font=("Arial", 10, "bold"), bg="#007ACC", fg="#FFFFFF", activebackground="#005A99", activeforeground="#FFFFFF", relief="flat", padx=10, pady=5)
process_button.pack(pady=15)

result_label = tk.Label(window, text="Result: ", font=("Arial", 12), bg="#FFFFFF", fg="#333333")
result_label.pack(pady=10)

window.mainloop()
