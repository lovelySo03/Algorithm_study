# 큰 수의 법칙
# 내 코드
# m : 더하는 횟수
# k : 연속해서 k번까지 더해질 수 있음
n, m , k = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
# 이미 정렬을 했으니까, 마지막이 제일 큰 값
Max = lst[len(lst)-1]
SecondMax = lst[len(lst)-2]

# lst_after에는 k의 발자취가 기록됨
lst_after =[]
for i in range(m):
    if i % (k + 1) == k:
        lst_after.append(SecondMax)
    else:
        lst_after.append(Max)
ans = sum(lst_after)
print(ans)
