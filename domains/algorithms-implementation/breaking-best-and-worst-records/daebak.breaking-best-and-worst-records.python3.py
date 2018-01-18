##breaking-best-and-worst-records
# n = 9
# score = [10,5,20,20,4,5,2,25,1]
# n = 10
# score = [3,4,21,36,10,28,35,5,24,42]
import sys
def breakingRecords(score):
    li = []
    High = []
    Low = []
    #Highest Score
    for i in range(n):
        li.append(score[i])
        if score[i] == max(li) and score[i] != score[0]:
            High.append(score[i])
        elif score[i] == min(li) and score[i] != score[0]:
            Low.append(score[i])
        else:
            pass
    # print(High)
    # print(Low)
    High = set(High)
    Low = set(Low)

    # print(len(High), len(Low))
    return len(High), len(Low)
    # Complete this function

if __name__ == "__main__":
    n = int(input().strip())
    score = list(map(int, input().strip().split(' ')))
    result = breakingRecords(score)
    print (" ".join(map(str, result)))