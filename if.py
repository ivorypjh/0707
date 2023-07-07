# 하나의 점수를 입력 받아서 60점 이상이면 합격

score = int(input("점수를 입력해주세요 : "))
# 실제 프로그램이라면 잘못된 입력을 할 수 있으므로
# 이에 대한 예외 처리가 필요.
# int를 사용해서 빈 공백도 알아서 처리

# int 형변환은 실수는 정수로 바꿀 수 있지만 문자열로 된 실수는
# 정수로 바꾸지 못함. 정수로 된 문자열만 정수로 바꿀 수 있음.
# int 형변환을 하기 전에 변환이 가능한 정수인지 확인하는 과정이 필요함.
# int가 필요하다면 int(float(input(...))) 형태로 처리 가능

# print(type(score))

# 숫자 데이터를 처리할 때 데이터의 범위를 확인해줘야 함
# 사용자의 입력은 랜덤하므로 잘못 될 수 있음

"""
if(score >= 60 and score <= 100): # &는 비트 연산이므로 and 를 사용해줘야 함
    {
        print("합격입니다")
    }
elif(score < 60 and score >= 0):
    {
        print("불합격입니다")
    }
else:
    {
        print("잘못된 입력입니다")
    }
"""

x = 12
y = False if x < 10 else True
print(y)

arr = {}
if arr:
    print(arr)
else:
    print("False입니다")

print("프로그램 종료")