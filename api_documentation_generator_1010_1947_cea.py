# 代码生成时间: 2025-10-10 19:47:24
import tkinter as tk
from tkinter import filedialog, messagebox
import json
import os

"""
API文档自动生成器
通过TKINTER框架实现的简单GUI应用程序，用于生成API文档。
"""

class ApiDocumentationGenerator:
    def __init__(self, master):
        """
        初始化GUI界面
        :param master: Tkinter主窗口对象
        """
        self.master = master
        master.title('API文档自动生成器')
        master.geometry('600x400')

        # 创建菜单栏
        menubar = tk.Menu(master)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label='打开', command=self.open_file)
        file_menu.add_command(label='保存', command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label='退出', command=master.quit)
        menubar.add_cascade(label='文件', menu=file_menu)
        master.config(menu=menubar)

        # 创建输入框
        self.input_label = tk.Label(master, text='输入API信息（JSON格式）：')
        self.input_label.pack()
        self.input_text = tk.Text(master, height=15, width=70)
        self.input_text.pack()

        # 创建输出框
        self.output_label = tk.Label(master, text='生成的API文档：')
        self.output_label.pack()
        self.output_text = tk.Text(master, height=15, width=70)
        self.output_text.pack()

    def open_file(self):
        """
        打开文件对话框，加载API信息文件
        """
        filepath = filedialog.askopenfilename()
        if not filepath:
            return

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                api_info = json.load(f)
                self.input_text.delete('1.0', tk.END)
                self.input_text.insert('1.0', json.dumps(api_info, indent=4, ensure_ascii=False))
        except json.JSONDecodeError as e:
            messagebox.showerror('错误', f'文件格式错误：{e}')
        except Exception as e:
            messagebox.showerror('错误', f'读取文件失败：{e}')

    def save_file(self):
        """
        保存生成的API文档到文件
        """
        self.generate_documentation()
        filepath = filedialog.asksaveasfilename(defaultextension='.md')
        if not filepath:
            return

        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(self.output_text.get('1.0', tk.END))
            messagebox.showinfo('成功', '文档保存成功！')
        except Exception as e:
            messagebox.showerror('错误', f'保存文件失败：{e}')

    def generate_documentation(self):
        """
        根据输入的API信息生成API文档
        """
        try:
            api_info = json.loads(self.input_text.get('1.0', tk.END))
            documentation = '# API文档

'
            # 遍历API信息，生成文档内容
            for api in api_info.get('apis', []):
                # 获取API基本信息
                name = api.get('name', '')
                path = api.get('path', '')
                method = api.get('method', '')
                description = api.get('description', '')

                # 生成API基本信息部分
                documentation += f"## {name}
路径：{path}
方法：{method}
描述：{description}

"
                # 获取请求参数和响应参数
                params = api.get('params', {})
                if params:
                    documentation += '### 请求参数
'
                    # 遍历请求参数，生成参数列表
                    for param, info in params.items():
                        documentation += f"- {param}：{info.get('description', '')}
类型：{info.get('type', '')}
是否必填：{'是' if info.get('required', False) else '否'}
"

                # 获取响应参数
                responses = api.get('responses', {})
                if responses:
                    documentation += '### 响应参数
'
                    # 遍历响应参数，生成参数列表
                    for status, response in responses.items():
                        documentation += f"状态码：{status}
"
                        for param, info in response.items():
                            documentation += f"- {param}：{info.get('description', '')}
类型：{info.get('type', '')}
"

            self.output_text.delete('1.0', tk.END)
            self.output_text.insert('1.0', documentation)
        except json.JSONDecodeError as e:
            messagebox.showerror('错误', f'API信息格式错误：{e}')
        except Exception as e:
            messagebox.showerror('错误', f'生成文档失败：{e}')

if __name__ == '__main__':
    # 创建主窗口
    root = tk.Tk()

    # 创建应用对象
    app = ApiDocumentationGenerator(root)

    # 运行主循环
    root.mainloop()