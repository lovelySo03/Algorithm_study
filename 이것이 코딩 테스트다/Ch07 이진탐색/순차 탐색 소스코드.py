# 순차 탐색
# n개의 데이터가 있을 때, 그 데이터를 차례대로 확인하며 어떤 처리를 해주는 것
# 리스트 안에 있는 특정한 데이터를 찾기 위해, 앞에서부터 데이터를 확인하는 방법

def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인하며, 현재 원소가 찾고자 하는 원소와 동일할 경우
    # 현재의 위치를 반환한다
    for i in range(n):
        if array[i] == target:
            return i

print("보기에 넣을 단어를 몇 개 입력할 지 적고, 찾을 단어도 적어주세요")
print("숫자 단어")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("앞서 적은 숫자 만큼 단어를 입력하세요. 띄어쓰기로 구분해주세요.")
array = input().split()

# 순차적으로 탐색한 결과 출력
print("찾는 단어의 인덱스 번호입니다. 0부터 시작해요")
print(sequential_search(n, target, array))
