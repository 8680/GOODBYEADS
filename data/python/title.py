import datetime
import pytz
import glob
import os

# 获取当前时间并转换为北京时间
utc_time = datetime.datetime.now(pytz.timezone('UTC'))
beijing_time = utc_time.astimezone(pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')

# 需要处理的特定文件名集合
target_files = {'adblock.txt', 'allow.txt', 'dns.txt'}

# 获取文件列表
file_list = glob.glob('./data/rules/*.txt')

# 遍历文件列表
for file_path in file_list:
    filename = os.path.basename(file_path)
    if filename not in target_files:
        continue  # 跳过不在目标列表中的文件

    # 打开文件并读取内容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 计算文件的行数
    line_count = content.count('\n') + 1 if content else 0

    # 在文件顶部插入内容
    new_content = (
        f"[Adblock Plus 2.0]\n"
        f"! Title: GOODBYEADS\n"
        f"! Homepage: https://github.com/8680/GOODBYEADS\n"
        f"! Expires: 12 Hours\n"
        f"! Version: {beijing_time}（北京时间）\n"
        f"! Description: 适用于AdGuard的去广告规则，合并优质上游规则并去重整理排列\n"
        f"! Total count: {line_count}\n"
        f"{content}"
    )

    # 将更新后的内容写入文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)
