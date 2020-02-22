# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 10:39:19 2019

@author: yumi
1.压缩一张图片

"""

import os
from PIL import Image
def process(addrs, dest, ratio, delete):
    # addrs 为所有待处理的图片地址 类型为　list
    #　dest 为某个文件夹路径 类型为 str
    # ratio 为缩小比例，　类型为 float
    # delete 为是否删除原文件标记，　类型为 bool
    for file in addrs:
        # 缩小图片并保存
        im = Image.open(file)
        adjusted_size = tuple([int(i*ratio) for i in im.size])
        new = im.resize(adjusted_size)
        name = file.split('/')[-1]
        file_path = os.path.join(dest, name)
        # 查看目的文件夹是否已经存在该文件
        # 存在则在文件名前添加 _ 
        while os.path.exists(file_path):
            name = '_' + name
            file_path = os.path.join(dest, name)
        new.save(file_path)
        print('文件 {0} 经处理后保存为 {1}'.format(file, name))    # 是否删除
    if delete:
        for file in addrs:
            os.remove(file)
        print('原文件已经删除')