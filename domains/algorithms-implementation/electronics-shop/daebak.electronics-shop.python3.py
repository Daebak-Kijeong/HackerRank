##electronics-shop
#모니카에겐 s만큼의 돈이 있다. 1<= s <=10^6
#키보드의 종류는 n개다. 1<= n <= 1000
#드라이브의 종류는 m개다. 1<= m <= 1000
#키보드와 드라이브를 하나씩 살 껀데, 수중에 있는 돈의 범위 내에서 최대 가격으로 맞출꺼다.
#만약 키보드나 드라이브 중 하나라도 못 산다면 -1을 프린트
s,n,m = 10,2,3
keyboards = [3,1]
drives = [5,2,8]

import sys

def getMoneySpent(keyboards, drives, s):
    li = [(k+d) for k in keyboards for d in drives]

    li2 = []
    try:
        for v in li:
            if v <= s:
               li2.append(v)

        # print(max(li2))
        return max(li2)
    except:
        # print("-1")
        return "-1"


    # Complete this function

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)