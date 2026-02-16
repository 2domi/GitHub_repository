right = [1,1,2,2,2,8]
input = input().split(" ")

for i in range(6):
    print(int(right[i]) - int(input[i]), end=" ")