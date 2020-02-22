"""
Created on Fri Dec 19 10:27:28 2019

@author: Zhou Yihong
"""
'''
#以下是常规法
R = 10000
R2 = R * R
count = 0
for x in range(-R, R+1):
    for y in range(-R, R+1):
        if x * x + y * y <= R2:
            count += 1
print(count / R2)
'''
#以下是蒙特卡洛法
import matplotlib.pyplot as plt
import random
R = 60
R2 = R * R
x_in = []
y_in = []
x_out = []
y_out = []
for i in range(1000000):
    x = random.random() * 2 * R - R
    y = random.random() * 2 * R - R
    if x * x + y * y > R2:
        x_out.append(x)
        y_out.append(y)
    else:
        x_in.append(x)
        y_in.append(y)
plt.figure(figsize=(16, 16))
plt.scatter(x_out, y_out, color='blue', marker='.', linewidths=0.1, alpha=0.3)
plt.scatter(x_in, y_in, color='red', marker='.', linewidths=0.1, alpha=0.3)
plt.scatter(0, 0, color='black')
plt.show()
print(4 * len(x_in) / (len(x_in) + len(x_out)))
