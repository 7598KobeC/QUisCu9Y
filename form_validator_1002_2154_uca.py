# 代码生成时间: 2025-10-02 21:54:28
import tkinter as tk
from tkinter import messagebox

"""
A simple form validator using Tkinter.

This script creates a basic GUI form with a text entry and a button.
The form includes a validator that checks if the input is a non-empty string.
"""

class FormValidator:
    def __init__(self, master):
        self.master = master
        self.master.title("Form Validator")
        
        # Create a label for the text entry
        self.label = tk.Label(master, text="Enter text: ")
        self.label.pack()
        
        # Create a text entry for user input
        self.entry = tk.Entry(master)
        self.entry.pack()
        
        # Create a button that triggers validation
        self.button = tk.Button(master, text="Validate", command=self.validate)
        self.button.pack()
        
    def validate(self):
        # Get the value from the text entry
        value = self.entry.get()
        
        # Check if the value is not empty
        if value:
            messagebox.showinfo("Validation", "Input is valid")
        else:
            messagebox.showerror("Validation", "Input cannot be empty")

# Create the main window
root = tk.Tk()

# Create an instance of FormValidator
form_validator = FormValidator(root)

# Start the Tkinter event loop
root.mainloop()