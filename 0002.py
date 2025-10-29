import os
# ping 本机回环地址
print("正在ping 127.0.0.1...")
响应 = os.system("ping -n 4 127.0.0.1")  # Windows系统
# 响应 = os.system("ping -c 4 127.0.0.1")  # Linux/Mac系统

if 响应 == 0:
    print("✓ 本机网络连接正常")
else:
    print("✗ 本机网络连接异常")
