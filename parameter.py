# 가변 매개변수 사용
# 매개변수의 갯수와 상관 없이 대입해서 호출이 가능함
# 함수 내부에서는 튜플이 됨.
def merge(*li, name):
    for elements in li:
        print(elements)
    print(name)

#merge(10, 20, 30, 40, "lee") # 에러 발생
merge(10, 20, 30, 40, name = "lee") # li, name에 정상적으로 대입


# name 매개변수와 그 이외의 매개변수로 구성된 함수
def merge(name, **paramet):
    for elements in paramet:
        print(elements, paramet[elements])

merge(name = "lee", age = "23", gender = "남")