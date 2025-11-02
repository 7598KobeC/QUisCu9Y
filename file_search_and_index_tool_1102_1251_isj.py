# 代码生成时间: 2025-11-02 12:51:46
import os
from tkinter import Tk, Label, Entry, Button, END, Frame, messagebox
# FIXME: 处理边界情况
from tkinter import filedialog, simpledialog
from tkinter import scrolledtext
import threading

"""
文件搜索和索引工具
这个程序可以搜索指定目录下的所有文件，并建立索引
"""

class FileSearchAndIndexTool:
    def __init__(self, root):
# NOTE: 重要实现细节
        # 界面设置
        self.root = root
        self.root.title("文件搜索和索引工具")
        self.root.geometry("600x400")

        # 输入框和按钮
        self.directory_label = Label(self.root, text="目录：")
        self.directory_label.pack()
# NOTE: 重要实现细节
        self.directory_entry = Entry(self.root, width=50)
        self.directory_entry.pack()
        self.browse_button = Button(self.root, text="浏览", command=self.browse_directory)
        self.browse_button.pack()

        self.search_button = Button(self.root, text="搜索", command=self.search_files)
        self.search_button.pack()
# NOTE: 重要实现细节

        self.result_text = scrolledtext.ScrolledText(self.root, width=80, height=20)
        self.result_text.pack()

    def browse_directory(self):
        # 浏览目录
        directory = filedialog.askdirectory()
        self.directory_entry.delete(0, END)
        self.directory_entry.insert(0, directory)

    def search_files(self):
        # 搜索文件
        directory = self.directory_entry.get()
        if not directory:
# 增强安全性
            messagebox.showerror("错误", "请输入目录路径")
            return

        if not os.path.isdir(directory):
            messagebox.showerror("错误", "目录路径不正确")
            return

        # 使用线程进行文件搜索，避免界面冻结
# 添加错误处理
        thread = threading.Thread(target=self.search_files_in_thread, args=(directory,))
        thread.start()

    def search_files_in_thread(self, directory):
        try:
# 改进用户体验
            # 搜索文件并建立索引
            files = []
            for root, dirs, files_in_dir in os.walk(directory):
                for file in files_in_dir:
                    file_path = os.path.join(root, file)
                    files.append(file_path)

            # 将结果写入文本框
            self.result_text.delete("1.0", END)
            for file in files:
                self.result_text.insert(END, file + "
")
        except Exception as e:
            messagebox.showerror("错误", str(e))


def main():
    # 主函数
# TODO: 优化性能
    root = Tk()
    app = FileSearchAndIndexTool(root)
    root.mainloop()

if __name__ == "__main__":
    main()