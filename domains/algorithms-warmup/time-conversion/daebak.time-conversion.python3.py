##TimeConversion
#input 07:05:45PM
import sys
from time import strptime, strftime
def timeConversion(s):
    a = strftime("%H:%M:%S", strptime(s, "%I:%M:%S%p")) #날짜/시간 형식의 문자열(str)을 datetime형태로 만들려면 strptime을 이용
    #strptime %p >>> Locale’s equivalent of either AM or PM
    #%I >>> Hour (12-hour clock) as a zero-padded decimal number.
    #%H >>> Hour (24-hour clock) as a zero-padded decimal number.
    # from time import localtime, strftime
    # print(localtime())
    # print(type(localtime))
    # strftime("%Y:%m:%d %H:%M:%S", localtime())
    return a
s = input().strip()
result = timeConversion(s)
print(result)