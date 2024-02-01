# 숫자 카드 게임
# 내 코드
n, m = map(int, input().split())
arr  = [list(map(int, input().split())) for _ in range(n)]

# 가장 작은 값 넣기 위해 잠시 사용
temp1 = []
# 가장 큰 값 구하기 위해 잠시 사용
temp2 = []
Min = 0

for i in range(n):
    temp1 = []
    for j in range(n):
        temp1.append(arr[i][j])
    Min = min(temp1)
    temp2.append(Min)

Max = max(temp2)
print(Max)
