# 代码生成时间: 2025-10-26 21:42:11
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import json

"""
Certificate Management System
This program allows users to manage digital certificates using a graphical interface.
"""

class CertificateManager:
    def __init__(self, root):
        """Initialize the CertificateManager with the root window."""
        self.root = root
        self.root.title("Certificate Management System")
        self.certificates = {}

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        "