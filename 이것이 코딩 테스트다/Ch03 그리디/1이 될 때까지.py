# 1이 될 때까지
# 내 코드
def divi(n,k):
    global count1
    if n == 1:
        return count1
    if n % k == 0:
        temp = n // k
        count1 += 1
        divi(temp,k)
    else:
        count1 += 1
        temp = n - 1
        divi(temp,k)
    return count1

n, k = map(int, input().split())
count1 = 0
# n이 k로 나누어 떨어지는지 확인
count1 = divi(n,k)
print(count1)
