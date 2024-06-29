# 3 두 배열의 원소 교체 
# 내 코드

n, k = map(int, input().split())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

# 내림차순으로 정렬하기
lst1.sort(reverse = -1)
lst2.sort(reverse = -1)

# 숫자 바꿔치기 
for i in range(k):
    if lst1[len(lst1)-1-i] < lst2[i]:
        lst1[len(lst1)-1-i] = lst2[i]

# 출력 
ans = 0
ans = sum(lst1)
print(ans)
​
