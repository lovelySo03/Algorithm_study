# 5-10 음료수 얼려먹기 
# 내 코드 

def dfs(map1, x, y):
    # 주어진 범위를 벗어나면 종료한다. 
    if x < 0 or y < 0 or x >= n or y >= m:
        return 0
    # 만약 방문하지 않았다면
    if map1[x][y] == 0:
        # 방문처리 해주기 
        map1[x][y] = 1 
        # 다른 위치들도 호출해주기
        # 인접한 녀석들을 방문처리 하기위한 과정
        dfs(map1, x-1, y)
        dfs(map1, x+1, y)
        dfs(map1, x,y-1)
        dfs(map1, x,y+1)
        return 1
    # 다 끝나면 0 리턴해주기 
    return 0
        

n, m = map(int, input().split())
map1 = [list(map(int, input())) for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        ret = dfs(map1, i, j)
        if ret == 1:
            cnt += 1 
print(cnt)
