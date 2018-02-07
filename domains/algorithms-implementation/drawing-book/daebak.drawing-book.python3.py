##drawing-book
# 책은 n page까지 있다.
# 책은 무조건 1장씩 넘긴다.
# 선생님은 p page를 펴라고 했다.
# 항상 시작은 1page에서 시작한다.
# output은 1page가 보이는 부분에서 몇 장을 넘기냐이다.
# n = 6
# p = 2

import sys

def solve(n, p):

    li = [j for j in range(n+2)]
    li2 = []

    try:
        for i in range(0, len(li), 2):
            # print(i)
            li2.append([li[i], li[i + 1]])
            # print(li2)

    except IndexError:
        pass

    li3 = sorted(li2, reverse=True)
    # 책을 1page에서 부터 시작하면
    i = 0
    for a in li2:
        if p in a:
            start = i
        i += 1
    # 책을 마지막page 부터 시작하면
    i = 0
    for b in li3:
        if p in b:
            end = i
        i += 1

    return min(start, end)
    #책을 마지막 page에서 부터 시작하면

# Complete this function

n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)