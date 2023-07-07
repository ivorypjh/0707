"""
i       j : 1 * i
0 *     0 - 0
1 **    0 - 1
2 ***   0 - 2
3 ****  0 - 3
4 ***** 0 - 4
"""

rangeNum = 7

for index in range(rangeNum):
    if index < rangeNum/2:
        for j in range(index + 1):
            print("*", end="")
    else:
        for j in range(rangeNum - index):
            print("*", end="")
    print()

"""
    &
   & &
  &   &
 &     &
&&&&&&&&&
"""

for i in range(rangeNum):
    if i == 0 or i == rangeNum -1:
        print(" " * (rangeNum - i - 1), end="")
        print("&" * (2 * i + 1), end="")
    else:
        print(" " * (rangeNum - i - 1), end="")
        print("&", end="")
        print(" " * (2 * i - 1), end= "")
        print("&", end="")
    print()

"""
2부터 1000까지 완전수의 갯수
완전수는 자신을 제외한 약수의 합이 자신과 같은 수
"""

absSum = 0

for i in range(2, 1001):
    # 약수의 합을 저장하는 변수. 
    # #합계의 초기화가 항상 0일 필요는 없음
    arrSum = 1 
    for j in range(2, i // 2 + 1): # 나머지가 0인 숫자가 약수
        if i % j == 0:
            arrSum += j
    if arrSum == i: # 완전수 판별
        absSum += 1

print(absSum)

"""
피보나치 수열의 n번째 값 구하기
"""
#몇번째 수열을 구할지 입력 받기
n = int(input("n을 입력하세요 : "))

arr_0 = 1 # 2번 앞의 결과
arr_1 = 1 # 1번 앞의 결과
result = 0

if n == 1 or n == 2:
    print("1")

else:
    for i in range(3, n+1): # 앞의 2번은 규칙의 예외이므로 제외
        result = arr_0 + arr_1
        arr_0 = arr_1
        arr_1 = result
    print(result)

