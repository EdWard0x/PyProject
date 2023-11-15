import tkinter as tk

# 创建一个Tkinter窗口
root = tk.Tk()

# 隐藏窗口标题栏和边框
root.overrideredirect(True)

# 将窗口置顶
root.wm_attributes("-topmost", True)

# 设置窗口大小和位置
win_width = 300
win_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_pos = (screen_width // 2) - (win_width // 2)
# print(screen_width // 2)
# print(win_width // 2)
# print(x_pos)
y_pos = (screen_height // 2) - (win_height // 2)
root.geometry('{}x{}+{}+{}'.format(win_width, win_height, x_pos, y_pos))

# 将窗口背景设为透明
root.attributes('-transparentcolor', 'white')

# 将窗口的画布设为透明
canvas = tk.Canvas(root, bg='white', highlightthickness=0)
canvas.pack(fill='both', expand=True)

# 绘制一个绿色空心正方形
canvas.create_rectangle(5, 5, win_width - 5, win_height - 5, outline='red', width=2)

# 进入循环让窗口保持打开状态
root.mainloop()