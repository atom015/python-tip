def sum_two(num):
    return num+2
arr = list(map(int,input().split()))
print(list(map(sum_two,arr)))
