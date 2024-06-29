# 2 성적이 낮은 순서로 학생 출력하기 
# 내 코드

# 필요한 자료 입력받기 
n = int(input())
name1 = []
score = []
for i in range(n):
    temp1, temp2 = input().split()
    name1.append(temp1)
    score.append(int(temp2))

# DAT 방법 사용
bucket = list([0]*100000)

for i in range(len(score)):
    num = score[i]
    bucket[num] += 1 

temp3 = []
for i in range(len(bucket)):
    if bucket[i] != 0:
        temp3.append(i)

# 출력 
for i in range(len(temp3)):
    print(name1[i], end=" ")
