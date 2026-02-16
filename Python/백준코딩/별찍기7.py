ipt = int(input())

for i in range(ipt * 2 - 1):
    print(" " * (ipt-1-i) + "*" * (9-abs(4-i)*2) + " " * (ipt-1-i))