"""
Created on Fri Dec 19 10:27:28 2019

@author: Zhou Yihong
"""
import numpy as np

def jiance(result):
    if result==1:
        return np.random.binomial(1, 0.9)
    else:
        return np.random.binomial(1, 0.09)
    
def main():
    N=1000000
    people=np.zeros([N, 2])
    people[0:int(N/100), 0]=1
    for i in range(N):
        people[i][1]=jiance(people[i][0])
    yangxing=0
    yangxing_bing=0
    for i in range(N):
        if people[i][1]==1:
            yangxing+=1
            if people[i][0]==1:
                yangxing_bing+=1
    print('检测阳性患病概率：', 100*yangxing_bing/yangxing, '%', sep='')
    
if __name__ == '__main__':
    main()

    