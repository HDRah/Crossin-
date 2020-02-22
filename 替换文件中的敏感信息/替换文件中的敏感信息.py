"""
Created on Fri Dec 19 10:27:28 2019

@author: Zhou Yihong
"""

import os
import re

path = r'C:\Users\yumi\Desktop\机器学习实战\python编程练习\替换文件中的敏感信息\替换内容'
filenames = os.listdir(path)
i=0
for filename in filenames:
    result='结果'+str(i)+'.txt'
    i+=1
    file = open(result, 'w+', encoding="utf-8")
    filepath = path + '/'
    filepath = filepath + filename
    # 遍历单个文件，读取行数
    for line in open(filepath, encoding="utf-8"):
        if re.search(r'\D1\d{9}\d$', line) is not None:
            a=re.search(r'\D1\d{9}\d$', line)
            line=line[0:a.start()+4]+'****'+line[a.start()+8:]

        elif re.search(r'\d{17}[\dA-Z]$', line) is not None:
            a=re.search(r'\d{17}[\dA-Z]$', line)
            line=line[0:a.start()+5]+'**********'+line[a.start()+15:]
        file.writelines(line)
    file.write('\n')
    file.close()
