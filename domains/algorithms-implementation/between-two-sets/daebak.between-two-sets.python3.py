import sys

def getTotalX(a, b):
    c = [[i for i in range(1, 101) if i % a[j] == 0] for j in range(len(a))]
    d = list(map(set, c))

    def inter(num, l):
        if num <= 1:
            return l[0]
        else:
            for k in range(num - 1):
                l[k + 1] = l[k] & l[k + 1]
            return l[k + 1]
    inter1 = inter(n, d)
    # 약수구하기
    s2 = []
    for i in range(m):  # i=0,1,2
        s = []
        num = int(b[i] / 2)  # b[0] = 16, num = 8
        s.append(b[i])  # b[0] = 16을 s 리스트의 0번째 insert
        while num >= 1:  # num이 1보다 크면
            if b[i] % num == 0:  # 16 % 8 == 0 이면
                s.append(num)  # s 리스트의 0번째에 8을 넣어라
            num -= 1

        s2.append(s)
    # s = []
    #
    # for i in range(m + 1):
    #     if n % i == 0:
    #         s.append(i)

    for i in range(len(s2)):
        s2[i] = set(s2[i])

    inter2 = inter(m, s2)
    inter3 = set.intersection(inter1, inter2)

    return len(inter3)
    # Complete this function

if __name__ == "__main__":
    n, m = map(int, input().strip().split(' '))
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)
