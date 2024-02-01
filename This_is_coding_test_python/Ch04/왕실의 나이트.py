# 왕실의 나이트
# 내 코드

def check(directx,directy,x,y,arr):

    for i in range(4):
        dx = x + directx[i]
        dy = y + directy[i]
        
        # 범위를 넘으면, 0을 리턴하면서 함수가 종료됨. 
        if dx < 0 or dy < 0 or dx >= len(arr) or dy >= len(arr):
            return 0

    return 1

arr = [[0]*8 for i in range(8)]
lst = list(input())
directx = [0]*4
directy = [0]*4
# 좌표값을 내가 원하는대로 변경해주기
# (0,0)을 시작점으로 하는 8*8 배열로
x = int(lst[1]) - 1
y = ord(lst[0]) - ord('a')

# 방향배열 설정
# RRRU
directx[0] = [0,0,0,-1]
directy[0] = [0,1,2,2]

# RRRD
directx[1] = [0,0,0,1]
directy[1] = [0,1,2,2]

# DDDR
directx[2] = [0,1,2,2]
directy[2] = [0,0,0,1]

# DDDL
directx[3] = [0,1,2,2]
directy[3] = [0,0,0,-1]

count = 0
for i in range(4):
    # 갈 수 있는지 없는지 체크하기 
    # 갈 수 있는 경우 count로 세기 
    count += check(directx[i],directy[i],x,y,arr)
print(count)
