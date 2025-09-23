# 代码生成时间: 2025-09-23 12:05:10
import tkinter as tk
from tkinter import messagebox

# 用户身份认证类
class UserAuth:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # 验证用户名和密码
    def authenticate(self):
        if self.username == 'admin' and self.password == 'admin123':
            return True
        else:
            return False

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('用户身份认证')
        self.geometry('300x150')
        self.create_widgets()

    # 创建界面元素
    def create_widgets(self):
        self.username_label = tk.Label(self, text='用户名:')
        self.username_label.pack()
        self.username_entry = tk.Entry(self, width=20)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text='密码:')
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show='*', width=20)
        self.password_entry.pack()

        self.login_button = tk.Button(self, text='登录', command=self.login)
        self.login_button.pack()

    # 登录函数
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        auth = UserAuth(username, password)

        if auth.authenticate():
            messagebox.showinfo('成功', '登录成功！')
        else:
            messagebox.showerror('错误', '用户名或密码错误！')

# 主程序入口
if __name__ == '__main__':
    app = Application()
    app.mainloop()