import sys
def miniMaxSum(arr):
    arr.sort() #arr에 뭐가 들어와도 sorting정렬, 거꾸로 정렬은 sort(reverse=True)
    a = sum(arr) #리스트 인자들의 합
    return print((a - arr[-1]), (a - arr[0]))
    # Complete this function

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)