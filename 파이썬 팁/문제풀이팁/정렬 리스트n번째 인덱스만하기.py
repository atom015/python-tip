#3번째 인덱스정렬
a = [[1,2,3],[5,4,1],[1,2,4],[4,2,4]]
a.sort(key=lambda t:(t[2]))
print(a)
#3번째 인덱스 내림차순 정렬
a.sort(key=lambda t:(-t[2]))
print(a)
