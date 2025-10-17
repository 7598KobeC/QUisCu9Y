# 代码生成时间: 2025-10-17 21:43:50
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

"""
校园管理平台主程序
"""

class CampusManagementSystem:
    def __init__(self, root):
        """初始化校园管理平台GUI界面"""
        self.root = root
        self.root.title('校园管理平台')
        self.root.geometry('800x600')

        # 菜单栏
        self.create_menu()

        # 主框架
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(expand=True, fill='both')

        # 登录区域
        self.login_frame = ttk.Frame(self.main_frame)
        self.login_frame.pack(side='top', fill='x')
        self.create_login_widgets()

    def create_menu(self):
        """创建菜单栏"""
        menubar = tk.Menu(self.root)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label='退出', command=self.root.quit)
        menubar.add_cascade(label='文件', menu=file_menu)

        self.root.config(menu=menubar)

    def create_login_widgets(self):
        """创建登录区域的控件"""
        ttk.Label(self.login_frame, text='用户名:').grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = ttk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(self.login_frame, text='密码:').grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = ttk.Entry(self.login_frame, show='*')
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        ttk.Button(self.login_frame, text='登录', command=self.login).grid(row=2, column=0, columnspan=2, pady=10)

    def login(self):
        """处理登录功能"""
        try:
            username = self.username_entry.get()
            password = self.password_entry.get()
            # 这里应该有实际的登录逻辑，比如验证用户名和密码
            # 目前只是简单的打印
            print(f'登录成功，用户名：{username}, 密码：{password}')
            messagebox.showinfo('登录成功', '欢迎进入校园管理平台')
        except Exception as e:
            messagebox.showerror('登录失败', str(e))


def main():
    """程序主入口"""
    root = tk.Tk()
    app = CampusManagementSystem(root)
    root.mainloop()

if __name__ == '__main__':
    main()
