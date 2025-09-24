# 代码生成时间: 2025-09-24 09:25:19
import tkinter as tk
from tkinter import ttk
import psutil
import os

"""
A simple GUI application to display system memory usage statistics using Python and Tkinter.
"""

class MemoryAnalysisGUI:
    def __init__(self, root):
        """Initialize the GUI application."""
        self.root = root
        self.root.title("Memory Usage Analysis")
        self.root.geometry("400x300")

        # Create a frame for holding the label and canvas
        frame = ttk.Frame(self.root)
        frame.pack(pady=20)

        # Create a label to display memory usage
        self.memory_usage_label = ttk.Label(frame, text="Memory Usage: 0%", font=("Helvetica", 16))
        self.memory_usage_label.pack(pady=10)

        # Create a canvas to display the memory usage graph
        self.canvas = tk.Canvas(frame, width=380, height=200)
        self.canvas.pack()

        # Draw the initial memory usage graph
        self.draw_memory_graph(0)

        # Update memory usage every second
        self.update_memory_usage()

    def update_memory_usage(self):
        """Update the memory usage statistics and graph."""
        try:
            mem = psutil.virtual_memory()
            usage_percent = mem.percent
            self.memory_usage_label.config(text=f"Memory Usage: {usage_percent}%")
            self.draw_memory_graph(usage_percent)
        except Exception as e:
            print(f"Error updating memory usage: {e}")
        finally:
            # Schedule the next update
            self.root.after(1000, self.update_memory_usage)

    def draw_memory_graph(self, usage_percent):
        """Draw the memory usage graph on the canvas."""
        self.canvas.delete("all")  # Clear the canvas
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        # Draw the background rectangle
        self.canvas.create_rectangle(10, 10, width - 10, height - 10, fill="white", outline="black")

        # Draw the memory usage bar
        bar_width = (width - 20) * usage_percent / 100
        self.canvas.create_rectangle(15, height - 15, 15 + bar_width, height - 30, fill="blue")

# Create the main window and pass it to the MemoryAnalysisGUI class
if __name__ == "__main__":
    root = tk.Tk()
    app = MemoryAnalysisGUI(root)
    root.mainloop()