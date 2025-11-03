# 代码生成时间: 2025-11-04 00:45:57
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

"""License Management System Application"""

class LicenseManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("License Management System")
        self.root.geometry("400x300")

        # Initialize database (for demonstration purposes, using a simple dictionary)
        self.licenses = {}

        # Create main frame
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=10)

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Create entry widgets
        self.id_label = ttk.Label(self.main_frame, text="License ID:")
        self.id_label.pack(side=tk.LEFT)
        self.id_entry = ttk.Entry(self.main_frame)
        self.id_entry.pack(side=tk.LEFT, padx=10)

        self.name_label = ttk.Label(self.main_frame, text="License Name:")
        self.name_label.pack(side=tk.LEFT)
        self.name_entry = ttk.Entry(self.main_frame)
        self.name_entry.pack(side=tk.LEFT, padx=10)

        # Create buttons
        self.add_button = ttk.Button(self.main_frame, text="Add License", command=self.add_license)
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.remove_button = ttk.Button(self.main_frame, text="Remove License", command=self.remove_license)
        self.remove_button.pack(side=tk.LEFT, padx=10)

    def add_license(self):
        license_id = self.id_entry.get()
        license_name = self.name_entry.get()

        # Error handling for empty fields
        if not license_id or not license_name:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Add license to the database
        self.licenses[license_id] = license_name
        messagebox.showinfo("Success", "License added successfully.")
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)

    def remove_license(self):
        license_id = self.id_entry.get()

        # Error handling for empty fields
        if not license_id:
            messagebox.showerror("Error", "Please enter a license ID to remove.")
            return

        # Remove license from the database
        if license_id in self.licenses:
            del self.licenses[license_id]
            messagebox.showinfo("Success", "License removed successfully.")
        else:
            messagebox.showerror("Error", "License ID not found.")
        self.id_entry.delete(0, tk.END)

# Create the main application window
if __name__ == "__main__":
    root = tk.Tk()
    app = LicenseManagementSystem(root)
    root.mainloop()