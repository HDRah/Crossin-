"""
Created on Fri Dec 19 10:27:28 2019
money:贷款金额
year:贷款年限
rate:标准年利率
factor:利率浮动倍数
@author: Zhou Yihong
输出：
两种贷款方式
一、等额本息1.每月还款 2.总利息 二、等额本金 1.首月还款2.每月递减额3.总利息
"""

money = int(input('贷款金额（万）：'))
year = int(input('贷款期限（年）：'))
rate = float(input('年利率（%）：'))
factor = float(input('浮动倍数：'))

month = year * 12
month_rate = rate / 100 * factor / 12
money *= 10000

month_pay = (money * month_rate * (1 + month_rate) ** month) / ((1 + month_rate) ** month - 1)
all_pay = month_pay * month

print('等额本息')
print('每月还款 %.2f' % month_pay)
print('总支付利息 %.2f' % (all_pay - money))

month_pay = money / month + money * month_rate
pay_down = money / month * month_rate
all_pay = ((money / month + money * month_rate) + money / month * (1 + month_rate)) / 2 * month

print('等额本金')
print('首月还款 %.2f' % month_pay)
print('每月递减 %.2f' % pay_down)
print('总支付利息 %.2f' % (all_pay - money))

    