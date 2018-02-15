##counting-valleys
#개리는 자전거를 탄다.
#sea level이라 불리는 것은 시작 높이다.
#시작 높이보다 올라갔다 다시 시작 높이까지 내려온 것을 1개의 mountain이라 한다.
#시작 높이보다 내려갔다 다시 시작 높이까지 올라온 것을 1개의 valley라 한다.
#자전거로 n번을 간다.
#올라가는 U 을 +1, D를 -1이라 생각해보면 0에서 시작해서 다시 0으로 돌아오는 것을 생각해보면 될 것 같다.
#output은 valley를 몇 번 했냐는 것 이므로 마이너스가 되었다가 다시 0이 되는 횟수를 반환하면 된다.
# n = 8
# s = "UDDDUDUU"

import sys

def countingValleys(n, s):

    li = []
    num = 0
    for i in s:
        if i == "U":
            num += 1
            li.append(num)
        elif i == "D":
            num -= 1
            li.append(num)
        # print(li)

    count = 0
    for i in range(len(li)):
        if li[i] < 0 and li[i+1] == 0:
            count += 1
            # print(count)

    return count
    # Complete this function

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    result = countingValleys(n, s)
    print(result)

