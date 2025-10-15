# 代码生成时间: 2025-10-16 02:04:23
import tkinter as tk
from tkinter import messagebox

"""
会员积分系统使用TKINTER框架实现，包含会员信息的输入、积分的增加和查询功能。
"""

class MembershipPointSystem:
    """会员积分系统类"""
    def __init__(self, root):
        """初始化主界面"""
        self.root = root
        self.root.title('会员积分系统')
        self.root.geometry('400x300')
        self.members = {}  # 存储会员信息

        # 会员姓名输入框
        self.name_label = tk.Label(self.root, text='会员姓名:', font=('Arial', 12))
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(self.root, font=('Arial', 12))
        self.name_entry.grid(row=0, column=1)

        # 会员积分输入框
        self.point_label = tk.Label(self.root, text='会员积分:', font=('Arial', 12))
        self.point_label.grid(row=1, column=0)
        self.point_entry = tk.Entry(self.root, font=('Arial', 12))
        self.point_entry.grid(row=1, column=1)

        # 增加会员积分按钮
        self.add_button = tk.Button(self.root, text='增加积分', command=self.add_member_point)
        self.add_button.grid(row=2, column=0, columnspan=2)

        # 显示会员积分信息按钮
        self.show_button = tk.Button(self.root, text='显示所有会员积分', command=self.show_all_members)
        self.show_button.grid(row=3, column=0, columnspan=2)

    def add_member_point(self):
        """增加会员积分"""
        name = self.name_entry.get()
        points = self.point_entry.get()
        if not name or not points:
            messagebox.showwarning('错误', '姓名和积分不能为空')
            return
        if not points.isdigit():
            messagebox.showwarning('错误', '积分必须是整数')
            return
        points = int(points)
        if name in self.members:
            self.members[name] += points
        else:
            self.members[name] = points
        messagebox.showinfo('成功', '会员积分增加成功')

    def show_all_members(self):
        """显示所有会员积分信息"""
        message = ''
        for name, points in self.members.items():
            message += f'{name}: {points}积分
'
        if not message:
            message = '没有会员信息'
        messagebox.showinfo('会员积分信息', message)

def main():
    """程序入口函数"""
    root = tk.Tk()
    app = MembershipPointSystem(root)
    root.mainloop()

if __name__ == '__main__':
    main()