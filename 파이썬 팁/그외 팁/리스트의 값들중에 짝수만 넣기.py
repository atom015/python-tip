def checking(num):
    return True if num%2 == 0 else False
arr = list(map(int,input().split()))
li = list(filter(checking,arr))
print(li)
