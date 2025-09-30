# 代码生成时间: 2025-09-30 18:20:34
import tkinter as tk
from tkinter import messagebox
import hashlib

"""
版权保护系统，使用TKINTER框架创建GUI界面，
实现文件哈希值计算和版权信息展示功能。
"""

class CopyrightProtectionSystem:
    def __init__(self, master):
        """
        初始化版权保护系统GUI界面
        :param master: tkinter主窗口对象
        """
        self.master = master
        self.master.title("版权保护系统")
        self.master.geometry("400x200")

        # 创建标签和输入框
        self.label = tk.Label(master, text="输入文件路径：")
        self.label.pack()

        self.entry = tk.Entry(master, width=40)
        self.entry.pack()

        # 创建计算哈希值按钮
        self.button = tk.Button(master, text="计算哈希值", command=self.calculate_hash)
        self.button.pack()

        # 创建版权信息标签
        self.copyright_label = tk.Label(master, text="")
        self.copyright_label.pack()

    def calculate_hash(self):
        """
        计算文件的哈希值并显示版权信息
        """
        try:
            file_path = self.entry.get()
            with open(file_path, "rb") as file:
                # 读取文件内容并计算哈希值
                file_hash = hashlib.sha256(file.read()).hexdigest()

                # 显示版权信息
                self.copyright_label.config(text=f"文件哈希值：{file_hash}")
        except FileNotFoundError:
            messagebox.showerror("错误", "文件不存在，请检查路径是否正确")
        except Exception as e:
            messagebox.showerror("错误", f"计算哈希值时出现错误：{e}")


def main():
    """
    程序入口函数
    """
    root = tk.Tk()
    app = CopyrightProtectionSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()