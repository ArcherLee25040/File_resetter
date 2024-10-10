import tkinter as tk
from tkinter import filedialog
import os
from datetime import datetime

def merge_txt_files():
    # 选择文件夹
    folder_path = filedialog.askdirectory()
    if not folder_path:
        return

    # 获取当前时间并格式化
    current_time = datetime.now().strftime('%Y%m%d%H%M%S')
    new_file_name = f"{current_time}File.txt"

    # 合并文件内容
    with open(new_file_name, 'w', encoding='utf-8') as merged_file:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.txt'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as txt_file:
                        merged_file.write(txt_file.read())
                        merged_file.write('\n')  # 可以根据需要添加换行符

    label_result.config(text=f"文件已合并为 {new_file_name}")

# 创建主窗口
root = tk.Tk()
root.title("Txt 文件合并工具")

# 创建按钮
button = tk.Button(root, text="选择文件夹并合并", command=merge_txt_files)
button.pack(pady=20)

# 结果标签
label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()