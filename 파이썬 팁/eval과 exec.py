#eval:문자열로 된 식을 실행
a = '3 + 4'
print(eval(a)) # result : 7

#exec:문자열로 된 문장 실행
b = 'k = 3 + 4'
exec(b)
print(k) #result : 7
