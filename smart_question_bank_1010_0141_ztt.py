# 代码生成时间: 2025-10-10 01:41:37
import tkinter as tk
from tkinter import messagebox
import json
import os

"""
智能题库系统
"""

# 题库文件路径
QUESTION_BANK_PATH = 'question_bank.json'

# 题库数据结构
QUESTION_BANK = {
    "question": "What is the capital of France?",
    "options": ["New York", "London", "Paris", "Berlin"],
    "answer": "Paris"
}

class SmartQuestionBank:
    """智能题库系统主类"""
    def __init__(self, master):
        """初始化GUI界面"""
        self.master = master
        self.master.title("智能题库系统")

        # 创建输入框
        self.question_label = tk.Label(master, text="Question: ")
        self.question_label.pack()
        self.question_var = tk.StringVar()
        self.question_entry = tk.Entry(master, textvariable=self.question_var)
        self.question_entry.pack()

        # 创建选项框
        self.option_label = tk.Label(master, text="Options: ")
        self.option_label.pack()
        self.option_vars = [tk.StringVar() for _ in range(4)]
        self.option_entries = [tk.Entry(master, textvariable=var) for var in self.option_vars]
        for entry in self.option_entries:
            entry.pack()

        # 创建答案框
        self.answer_label = tk.Label(master, text="Answer: ")
        self.answer_label.pack()
        self.answer_var = tk.StringVar()
        self.answer_entry = tk.Entry(master, textvariable=self.answer_var)
        self.answer_entry.pack()

        # 创建按钮
        self.save_button = tk.Button(master, text="Save", command=self.save_question)
        self.save_button.pack()
        self.load_button = tk.Button(master, text="Load", command=self.load_question)
        self.load_button.pack()
        self.clear_button = tk.Button(master, text="Clear", command=self.clear_question)
        self.clear_button.pack()

    def save_question(self):
        """保存题目到文件"""
        try:
            question = self.question_var.get()
            options = [var.get() for var in self.option_vars]
            answer = self.answer_var.get()
            data = {"question": question, "options": options, "answer": answer}
            with open(QUESTION_BANK_PATH, 'w') as f:
                json.dump(data, f)
            messagebox.showinfo("Success", "Question saved successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def load_question(self):
        """从文件加载题目"""
        try:
            with open(QUESTION_BANK_PATH, 'r') as f:
                data = json.load(f)
                self.question_var.set(data["question"])
                for i, var in enumerate(self.option_vars):
                    var.set(data["options"][i])
                self.answer_var.set(data["answer"])
            messagebox.showinfo("Success", "Question loaded successfully")
        except FileNotFoundError:
            messagebox.showerror("Error", "Question bank file not found")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_question(self):
        """清空题目"""
        self.question_var.set("")
        for var in self.option_vars:
            var.set("")
        self.answer_var.set("")

def main():
    """程序主入口"""
    root = tk.Tk()
    SmartQuestionBank(root)
    root.mainloop()

if __name__ == '__main__':
    main()
