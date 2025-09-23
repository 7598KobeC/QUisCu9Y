# 代码生成时间: 2025-09-24 01:17:56
import tkinter as tk
from tkinter import messagebox

import sqlite3

# 数据库连接函数，使用参数化查询防止SQL注入
def get_connection():
    conn = sqlite3.connect('example.db')
    return conn

# 插入数据函数，演示如何防止SQL注入
def insert_data(name, age):
    try:
        # 连接数据库
        conn = get_connection()
# 改进用户体验
        cursor = conn.cursor()

        # 使用参数化查询
        query = "INSERT INTO users (name, age) VALUES (?, ?)"
        cursor.execute(query, (name, age))

        # 提交事务
# 扩展功能模块
        conn.commit()
        print("Data inserted successfully")
    except sqlite3.Error as e:
        print("An error occurred: ", e)
    finally:
        # 关闭数据库连接
        if conn:
            conn.close()

# Tkinter GUI界面
class SqlInjectionProtectionApp(tk.Tk):
    def __init__(self):
# 改进用户体验
        super().__init__()
        self.title("SQL Injection Protection")
        self.geometry("400x200")
# 扩展功能模块

        # 输入框
        self.name_label = tk.Label(self, text="Name: ")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1)

        self.age_label = tk.Label(self, text="Age: ")
# 添加错误处理
        self.age_label.grid(row=1, column=0)
        self.age_entry = tk.Entry(self)
        self.age_entry.grid(row=1, column=1)

        # 提交按钮
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_data)
        self.submit_button.grid(row=2, column=0, columnspan=2)
# 添加错误处理

    def submit_data(self):
        # 获取输入框数据
        name = self.name_entry.get()
        age = self.age_entry.get()

        try:
            # 将字符串转换为整数
            age = int(age)
            # 插入数据
            insert_data(name, age)
            messagebox.showinfo("Success", "Data submitted successfully")
# 扩展功能模块
        except ValueError:
# 增强安全性
            messagebox.showerror("Error", "Invalid age. Please enter a number.")

# 主程序
if __name__ == "__main__":
# 增强安全性
    app = SqlInjectionProtectionApp()
    app.mainloop()
# 改进用户体验