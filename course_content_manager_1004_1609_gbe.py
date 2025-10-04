# 代码生成时间: 2025-10-04 16:09:48
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


# 数据存储结构
class Course:
    def __init__(self, name, content):
        self.name = name
        self.content = content

# 主窗口类
class CourseContentManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Course Content Manager')
        self.geometry('400x300')
        self.create_widgets()

    def create_widgets(self):
        # 输入框标签
        ttk.Label(self, text='Course Name:').grid(column=0, row=0, padx=10, pady=10)
        ttk.Label(self, text='Course Content:').grid(column=0, row=1, padx=10, pady=10)

        # 输入框
        self.name_entry = ttk.Entry(self)
        self.name_entry.grid(column=1, row=0, padx=10, pady=10)
        self.content_text = tk.Text(self, height=10)
        self.content_text.grid(column=1, row=1, padx=10, pady=10)

        # 按钮
        ttk.Button(self, text='Add Course', command=self.add_course).grid(column=0, row=2, padx=10, pady=10)
        ttk.Button(self, text='Delete Course', command=self.delete_course).grid(column=1, row=2, padx=10, pady=10)

    def add_course(self):
        # 获取输入
        name = self.name_entry.get()
        content = self.content_text.get('1.0', 'end')
        if not name or not content:
            messagebox.showerror('Error', 'Please fill in all fields')
            return

        # 添加课程，这里仅作为示例，实际应用中应存储到数据库
        self.courses.append(Course(name, content))
        messagebox.showinfo('Success', 'Course added successfully')
        self.name_entry.delete(0, tk.END)
        self.content_text.delete('1.0', 'end')

    def delete_course(self):
        # 获取输入
        name = self.name_entry.get()
        if not name:
            messagebox.showerror('Error', 'Please fill in course name to delete')
            return

        # 删除课程，这里仅作为示例，实际应用中应从数据库删除
        for course in self.courses:
            if course.name == name:
                self.courses.remove(course)
                messagebox.showinfo('Success', 'Course deleted successfully')
                return
        messagebox.showerror('Error', 'Course not found')

    # 初始化课程列表
    courses = []

# 运行应用
if __name__ == '__main__':
    manager = CourseContentManager()
    manager.mainloop()