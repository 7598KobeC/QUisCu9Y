# 代码生成时间: 2025-10-12 02:41:21
import tkinter as tk
from tkinter import messagebox

# 直播带货系统主窗口类
class LiveCommerceSystem:
    def __init__(self, master):
        # 初始化主窗口
        self.master = master
        self.master.title('直播带货系统')

        # 产品列表框
        self.product_list_frame = tk.Frame(self.master)
        self.product_list_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.product_list = tk.Listbox(self.product_list_frame)
        self.product_list.pack(expand=True, fill=tk.BOTH)

        # 产品详细信息和下单按钮
        self.product_info_frame = tk.Frame(self.master)
        self.product_info_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.product_name_label = tk.Label(self.product_info_frame, text="产品名称")
        self.product_name_label.pack()
        self.product_name_var = tk.StringVar()
        self.product_name_entry = tk.Entry(self.product_info_frame, textvariable=self.product_name_var)
        self.product_name_entry.pack()
        self.place_order_button = tk.Button(self.product_info_frame, text="下单", command=self.place_order)
        self.place_order_button.pack()

        # 添加示例产品
        self.example_products = ["产品1", "产品2", "产品3"]
        for product in self.example_products:
            self.product_list.insert(tk.END, product)

    def place_order(self):
        # 下单逻辑
        selected_product = self.product_list.get(self.product_list.curselection())
        if not selected_product:
            messagebox.showerror("错误", "请选择一个产品")
        else:
            self.product_name_var.set(selected_product)
            messagebox.showinfo("下单成功", f"您已成功下单：{selected_product}")

# 创建主窗口并运行
if __name__ == '__main__':
    master = tk.Tk()
    app = LiveCommerceSystem(master)
    master.mainloop()