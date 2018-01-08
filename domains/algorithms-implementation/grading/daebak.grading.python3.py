##grading
#4
#73
#67
#38
#33
import sys

def solve(grades):
    result = []
    for i in grades:
        if i >= 38: #Rule4: below 38, the grade will not be modified
            if i % 5 >= 3: #%는 나눈 나머지
               i += (5 - (i % 5))
        result.append(i)

    return result

    # Complete this function
n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)
result = solve(grades)
print("\n".join(map(str, result)))
