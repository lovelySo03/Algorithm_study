# 1 위에서 아래로 
# 내 코드

# 필요한 자료 입력받기 
n = int(input())
lst = []
for i in range(n):
    temp = int(input())
    lst.append(temp)

# DAT 방법 사용
bucket = list([0]*100000)

for i in range(len(lst)):
    num = lst[i]
    bucket[num] += 1 

# 조건에 맞으면 출력
for i in range(len(bucket)-1,0,-1):
    if bucket[i] != 0:
        print(i, end=" ")
