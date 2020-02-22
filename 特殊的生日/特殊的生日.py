# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 10:39:19 2019
a.strftime('%Y%m%d')
datetime.timedelta(days=1)
@author: yumi
"""

import datetime
# 获取今天日期
n_days = datetime.date.today()
while True:
    # 从今天起往前减一天循环
    n_days -= datetime.timedelta(days=1)
    # 获得格式化的时间
    str_time = n_days.strftime('%Y%m%d')
    # 第一个出现的不重复日就是他的生日
    if len(set(str_time)) == 8:
        print(str_time)
        break