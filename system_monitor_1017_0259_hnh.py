# 代码生成时间: 2025-10-17 02:59:27
import tkinter as tk
from tkinter import ttk
import psutil
import threading
import time

"""
System Performance Monitor
This is a simple system performance monitoring tool using Python and Tkinter.
It provides real-time updates on CPU usage, memory usage, and disk usage.
"""

class SystemMonitor:
    def __init__(self, root):
        """Initialize the SystemMonitor class."""
# 添加错误处理
        self.root = root
        self.root.title("System Performance Monitor")

        # Create frames for each monitoring section
        self.cpu_frame = ttk.Frame(self.root, padding="3 3 12 12")
        self.cpu_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.mem_frame = ttk.Frame(self.root, padding="3 3 12 12")
        self.mem_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.disk_frame = ttk.Frame(self.root, padding="3 3 12 12")
        self.disk_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Create labels for each monitoring section
        self.cpu_label = ttk.Label(self.cpu_frame, text="CPU Usage")
        self.cpu_label.pack(side=tk.TOP)

        self.cpu_value = tk.StringVar()
        self.cpu_value_label = ttk.Label(self.cpu_frame, textvariable=self.cpu_value)
        self.cpu_value_label.pack(side=tk.TOP)

        self.mem_label = ttk.Label(self.mem_frame, text="Memory Usage")
        self.mem_label.pack(side=tk.TOP)

        self.mem_value = tk.StringVar()
        self.mem_value_label = ttk.Label(self.mem_frame, textvariable=self.mem_value)
        self.mem_value_label.pack(side=tk.TOP)

        self.disk_label = ttk.Label(self.disk_frame, text="Disk Usage")
        self.disk_label.pack(side=tk.TOP)

        self.disk_value = tk.StringVar()
        self.disk_value_label = ttk.Label(self.disk_frame, textvariable=self.disk_value)
        self.disk_value_label.pack(side=tk.TOP)

        # Start the monitoring thread
        self.monitor_thread = threading.Thread(target=self.monitor)
        self.monitor_thread.start()

    def monitor(self):
        """Monitor system performance and update the GUI."""
        while True:
# NOTE: 重要实现细节
            try:
                # Get CPU usage
                cpu_usage = psutil.cpu_percent(interval=1)
                self.cpu_value.set(f"{cpu_usage}%")

                # Get memory usage
                mem = psutil.virtual_memory()
# 优化算法效率
                mem_usage = mem.percent
# 添加错误处理
                self.mem_value.set(f"{mem_usage}%")

                # Get disk usage
# 添加错误处理
                disk_usage = psutil.disk_usage('/')
                self.disk_value.set(f"{disk_usage.percent}%")

                # Update the GUI
                self.root.update_idletasks()
                self.root.update()

                # Wait for 1 second before updating again
# NOTE: 重要实现细节
                time.sleep(1)

            except Exception as e:
                print(f"Error monitoring system performance: {e}")
                break

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    root.geometry("400x200")

    # Create an instance of SystemMonitor
    monitor = SystemMonitor(root)

    # Start the main loop
    root.mainloop()