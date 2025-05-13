import os
import datetime

os.chdir('tmp')
# 打开原始文件和目标文件
with open('.././data/rules/adblock.txt', 'r') as input_file, open('.././data/rules/dns.txt', 'w') as output_file:
    # 逐行读取原始文件内容
    for line in input_file:
        # 去除行尾的换行符
        line = line.strip()
        
        # 检查行长度是否大于等于2，并且首字符是"||"并且结尾是"^"
        if len(line) >= 2 and line.startswith("||") and line.endswith("^"):
            # 将满足条件的行写入目标文件
            output_file.write(line + '\n')
