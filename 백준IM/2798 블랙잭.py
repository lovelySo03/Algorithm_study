# 백준 2798 
# 블랙잭 

def dfs(level):
    global Max1
    if level == 3:
        sum1 = 0
        # print(path)
        sum1 = path[0] + path[1] + path[2]
        if sum1 <= m:
            if sum1 > Max1:
                Max1 = sum1
        return
    for i in range(n):
        if used[i] == 1:
            continue
        path[level] = lst[i]
        used[i] = 1
        dfs(level + 1)
        used[i] = 0

n, m = map(int, input().split()) 
lst = list(map(int, input().split()))
path = [0]*3
used = [0]*n
Max1 = -21e8
dfs(0)
print(Max1)
