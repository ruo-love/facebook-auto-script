import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from facebook import FacebookScript
from common import log


def submit():
    # 获取用户名和密码
    username = entry_username.get()
    password = entry_password.get()
    friend_url = entry_friend_url.get()
    log(log_text, "开始运行")
    log(log_text, "用户名: " + username)
    log(log_text, "密码: " + password)
    log(log_text, "好友列表URL: " + friend_url)
    # 创建一个 FacebookScript 实例
    facebook_script = FacebookScript(username, password, friend_url, log_text)
    # 运行
    # facebook_script.run()


root = ttk.Window()
root.geometry("1000x600")
root.title("Facebook Script")
root.resizable(False, False)
# 创建一个 Root Frame
root_frame = ttk.Frame(root)
root_frame.pack(expand=True, fill="both")
root_frame.columnconfigure(0, weight=1)
root_frame.columnconfigure(1, weight=20)
# 创建一个 login Frame
form_frame = ttk.Frame(root_frame)
form_frame.grid(row=0, column=0, sticky="nsew")
form_frame.columnconfigure(0, weight=1)
form_frame.columnconfigure(1, weight=4)

# 创建用户名标签和输入框
label_username = ttk.Label(form_frame, text="用户名：")
label_username.grid(row=0, column=0, padx=5, pady=5, sticky='ew')
entry_username = ttk.Entry(form_frame)
entry_username.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')

# 创建密码标签和输入框
label_password = ttk.Label(form_frame, text="密码：")
label_password.grid(row=1, column=0, padx=5, pady=5, sticky='ew')
entry_password = ttk.Entry(form_frame, show="*")
entry_password.grid(row=1, column=1, padx=5, pady=5, sticky='nsew')

# Friend url
label_friend_url = ttk.Label(form_frame, text="好友列表URL")
label_friend_url.grid(row=2, column=0, padx=5, pady=5, sticky='ew')
entry_friend_url = ttk.Entry(form_frame)
entry_friend_url.grid(row=2, column=1, padx=5, pady=5, sticky='nsew')

# message
label_message = ttk.Label(form_frame, text="发送内容")
label_message.grid(row=3,column=0, padx=5, pady=5, sticky='ew')
text_message = ttk.Text(form_frame, wrap=WORD, height=5,width=50)
text_message.grid(row=3,  column=1, padx=5, pady=5)

# 创建登录按钮
button_login = ttk.Button(form_frame, text="运行", command=submit)
button_login.grid(row=4, columnspan=2, padx=5, pady=20, sticky='nsew')

# 创建一个运行日志 Frame
log_frame = ttk.Frame(root_frame)
log_frame.grid(row=0, column=1, sticky='nsew')
log_frame.columnconfigure(0, weight=1)

# 创建一个运行日志显示框
log_text = ttk.Text(log_frame, state="disabled", height=16, background="#f9a461", foreground="#1c63d3")
log_text.grid(row=0, column=0, padx=5, sticky='nsew')

# 创建一个滚动条，用于滚动文本框中的内容
scrollbar = ttk.Scrollbar(log_frame, bootstyle="default-round", orient="vertical", command=log_text.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
# 将文本框与滚动条关联
log_text.config(yscrollcommand=scrollbar.set)

# 创建一个用户信息日志 Frame
user_log_frame = ttk.Frame(root_frame)
user_log_frame.grid(row=1, columnspan=2, sticky="nsew")
user_log_frame.columnconfigure(0, weight=1)

# 创建一个用户信息日志显示框
user_log_text = ttk.Text(user_log_frame, state="normal")
user_log_text.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
# 创建一个滚动条，用于滚动文本框中的内容
scrollbar = ttk.Scrollbar(user_log_frame, bootstyle="default-round", orient="vertical", command=user_log_text.yview)
scrollbar.grid(row=1, column=2, sticky="nsew")
# 将文本框与滚动条关联
user_log_text.config(yscrollcommand=scrollbar.set)
# 创建进度条
progress = ttk.Progressbar(user_log_frame, length=100, mode="determinate", bootstyle=SUCCESS)
progress["value"] = 50
progress.grid(row=0, columnspan=2, padx=5, sticky="nsew")
root.mainloop()
