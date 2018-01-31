##day-of-the-programmer

# 256번째 날이 몇월 몇일 인지 반환해줘야함 13.09.2017
# 2월의 경우 2016년엔 윤달로 29일까지 있다. 윤달은 4년 주기로 온다.
# ...2012, 2016, 2020, 2024...
# 근데 1700~1917년까진 Julian calendar를 사용했다.
# 1919년도부턴 Gregorian calendar를 사용했다.
# 1918년에 바뀌었는데, 바뀔때 1918년 1월 31일 다음날이 1918년 2월 14일이었다.
# 이말은 결국, 1918년의 2월은 14일부터 28일까지 즉, 15일인 것이다.
# 이렇게 되면 1918년도엔 256번째되는 날이 26.09.2018 (8월까지 230일)이다.
# 문제는 Julian calendar은 4의 배수로 생각하면 되는데,
# Gregorian calendar 사용부턴 윤달을 조건1)400으로 나눠떨어지고a
# 조건2)4로 나눠떨어지지만 100으로 나눠떨어지면 윤달이 아니다

import sys

def solve(year):

    odd = [y for y in range(1919,2701) if (y%4 == 0 and y%100 !=0) or y%400 == 0]
    odd2 = [y for y in range(1700,1918) if y%4 == 0]
    odd = sorted(odd + odd2)
    # print(odd)
    if year in odd:
        a = "12.09." + str(year)
    elif year == 1918:
        a = "26.09." + str(year)
    else:
        a = "13.09." + str(year)
    # print(a)
    return a
    # Complete this function

year = int(input().strip())
result = solve(year)
print(result)




