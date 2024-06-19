# Step 1: Importing required packages
import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader
import os

# Step 4: Function to open file
def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        selected_file.set(file_path)

# Step 5: Function to convert the file
def convert_file():
    pdf_path = selected_file.get()
    if not pdf_path:
        messagebox.showerror("Error", "No PDF file selected")
        return

    output_dir = os.path.dirname(pdf_path)
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_path = os.path.join(output_dir, f"{base_name}.txt")

    with open(pdf_path, "rb") as pdf_file:
        reader = PdfReader(pdf_file)
        with open(output_path, "w", encoding="utf-8") as text_file:
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    text_file.write(text)
                    text_file.write("\n\n")
    messagebox.showinfo("Success", f"File Converted Successfully! Saved as {output_path}")

# Step 2: Create main window and frame
root = tk.Tk()
root.title("Basic PDF Converter")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

selected_file = tk.StringVar()

# Step 3: Create Widgets
tk.Label(frame, text="Selected PDF File:").grid(row=0, column=0, sticky="e")
tk.Entry(frame, textvariable=selected_file, state="readonly", width=50).grid(row=0, column=1, padx=5)
tk.Button(frame, text="Browse PDF", command=open_file).grid(row=0, column=2)
tk.Button(frame, text="Convert", command=convert_file).grid(row=1, columnspan=3, pady=5)
root.mainloop()