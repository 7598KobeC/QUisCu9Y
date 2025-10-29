# 代码生成时间: 2025-10-29 19:58:06
import tkinter as tk
from tkinter import filedialog, messagebox
import zipfile
# 添加错误处理
import gzip
import bz2
import lzma


# 数据压缩和解压工具
class CompressionTool:
    def __init__(self, root):
        # 初始化GUI界面
        self.root = root
# 扩展功能模块
        self.root.title('数据压缩和解压工具')
        self.create_widgets()

    def create_widgets(self):
        # 创建GUI控件
        self.file_label = tk.Label(self.root, text='文件路径:')
        self.file_label.grid(row=0, column=0)
        self.file_entry = tk.Entry(self.root, width=50)
        self.file_entry.grid(row=0, column=1)
        self.browse_button = tk.Button(self.root, text='浏览', command=self.browse_file)
# 扩展功能模块
        self.browse_button.grid(row=0, column=2)
        self.compress_button = tk.Button(self.root, text='压缩', command=self.compress_file)
# NOTE: 重要实现细节
        self.compress_button.grid(row=1, column=0, columnspan=3)
        self.decompress_button = tk.Button(self.root, text='解压', command=self.decompress_file)
        self.decompress_button.grid(row=2, column=0, columnspan=3)

    def browse_file(self):
        # 选择文件
        file_path = filedialog.askopenfilename()
# 改进用户体验
        self.file_entry.delete(0, tk.END)
        self.file_entry.insert(0, file_path)

    def compress_file(self):
        # 压缩文件
        file_path = self.file_entry.get()
        try:
            if not file_path:
                messagebox.showerror('错误', '请选择文件')
                return
            compressed_path = file_path + '.zip'
            with zipfile.ZipFile(compressed_path, 'w') as zip_file:
                zip_file.write(file_path, arcname=os.path.basename(file_path))
            messagebox.showinfo('成功', '文件压缩成功')
        except Exception as e:
            messagebox.showerror('错误', str(e))

    def decompress_file(self):
        # 解压文件
        file_path = self.file_entry.get()
        try:
            if not file_path:
                messagebox.showerror('错误', '请选择文件')
                return
            if file_path.endswith('.zip'):
                with zipfile.ZipFile(file_path, 'r') as zip_file:
                    zip_file.extractall(os.path.dirname(file_path))
                messagebox.showinfo('成功', '文件解压成功')
            elif file_path.endswith('.gz'):
                with gzip.open(file_path, 'rb') as f_in:
# 优化算法效率
                    with open(file_path + '.decompressed', 'wb') as f_out:
                        f_out.write(f_in.read())
                messagebox.showinfo('成功', '文件解压成功')
            elif file_path.endswith('.bz2'):
                with bz2.open(file_path, 'rb') as f_in:
                    with open(file_path + '.decompressed', 'wb') as f_out:
                        f_out.write(f_in.read())
                messagebox.showinfo('成功', '文件解压成功')
            elif file_path.endswith('.xz'):
# 扩展功能模块
                with lzma.open(file_path, 'rb') as f_in:
                    with open(file_path + '.decompressed', 'wb') as f_out:
                        f_out.write(f_in.read())
# 优化算法效率
                messagebox.showinfo('成功', '文件解压成功')
# 改进用户体验
            else:
                messagebox.showerror('错误', '不支持的文件格式')
# 优化算法效率
        except Exception as e:
            messagebox.showerror('错误', str(e))

if __name__ == '__main__':
    root = tk.Tk()
    app = CompressionTool(root)
    root.mainloop()