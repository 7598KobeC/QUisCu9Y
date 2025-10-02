# 代码生成时间: 2025-10-03 01:31:23
import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

"""
数据加密传输工具使用Python和Tkinter框架。
该工具允许用户输入明文数据，并使用对称加密算法进行加密，
然后将加密后的密文显示给用户。
"""

class DataEncryptionCommunication:
    def __init__(self, master):
        """
        初始化应用程序窗口。
        :param master: Tkinter主窗口
        """
        self.master = master
        self.master.title("数据加密传输工具")
        self.fernet_key = None
        self.init_gui()

    def init_gui(self):
        """
        初始化GUI组件。
        """
        # 创建并放置输入框
        self.input_label = tk.Label(self.master, text="请输入明文数据：")
        self.input_label.pack()
        self.input_entry = tk.Entry(self.master, width=50)
        self.input_entry.pack()

        # 创建并放置加密按钮
        self.encrypt_button = tk.Button(self.master, text="加密", command=self.encrypt)
        self.encrypt_button.pack()

        # 创建并放置显示框
        self.output_label = tk.Label(self.master, text="加密后的密文：")
        self.output_label.pack()
        self.output_entry = tk.Entry(self.master, width=50, state='disabled')
        self.output_entry.pack()

        # 创建并放置生成密钥按钮
        self.generate_key_button = tk.Button(self.master, text="生成密钥", command=self.generate_key)
        self.generate_key_button.pack()

    def generate_key(self):
        """
        生成密钥并显示。
        """
        self.fernet_key = Fernet.generate_key()
        self.key_label = tk.Label(self.master, text=f"密钥：{self.fernet_key.decode()}")
        self.key_label.pack()

    def encrypt(self):
        """
        加密明文数据。
        """
        plaintext = self.input_entry.get()
        if not self.fernet_key:
            messagebox.showerror("错误", "请先生成密钥")
            return
        try:
            fernet = Fernet(self.fernet_key)
            encrypted = fernet.encrypt(plaintext.encode())
            self.output_entry.config(state='normal')
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, encrypted.decode())
            self.output_entry.config(state='disabled')
        except Exception as e:
            messagebox.showerror("错误", str(e))

def main():
    """
    程序入口点。
    """
    root = tk.Tk()
    app = DataEncryptionCommunication(root)
    root.mainloop()

if __name__ == "__main__":
    main()