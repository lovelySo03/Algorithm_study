# 예제 4-1
# 내 코드
n = int(input())
key1 = list(input().split())
arr = [[0]*n for i in range(n)]

directx = [0,0,-1,1]
directy = [-1,1,0,0]

x = 0
y = 0
sumdx = 0
sumdy = 0

for i in range(len(key1)):
    if key1[i] == 'U':
        dx = x + directx[0]
        dy = y + directy[0]
        print(f"U : dx {dx} dy {dy}")
    if key1[i] == 'D':
        dx = x + directx[1]
        dy = y + directy[1]
        print(f"D : dx {dx} dy {dy}")
    if key1[i] == 'L':
        dx = x + directx[2]
        dy = y + directy[2]
        print(f"L : dx {dx} dy {dy}")
    if key1[i] == 'R':
        dx = x + directx[3]
        dy = y + directy[3]
        print(f"R : dx {dx} dy {dy}")

    if dx < 0 or dy < 0 or dx >= n or dy >= n:
        dx = x
        dy = y
    # 시작점 업데이트
    x = dx
    y = dy

x = x + 1
y = y + 1

print(y,x)
