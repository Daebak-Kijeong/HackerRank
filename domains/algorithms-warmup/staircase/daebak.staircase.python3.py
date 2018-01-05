import sys
def staircase(n):
    for i in range(1, n + 1):
        a = print(" " * (n - i) + "#" * i)
    return (a)
    # Complete this function
if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)