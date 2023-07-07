def displayHello() -> None :
    for index in range (2):
        print("hello")

displayHello()
print(displayHello) # 함수의 이름은 함수를 저장한 곳을 참조(가리킴)

def intOp(a, b):
    return a+b, a-b
#튜플 전체를 하나의 변수로 받기
t = intOp(100, 200)
print(t)
# 튜플을 분해해서 받기
add, sub = intOp(10, 20)
print(add, sub)

def callByValue(a : int) -> None:
    a = 10
    print(a)

x = 20
callByValue(x) # 10
print(x) # 20

def callByReference(li : list) -> None:
    li[0] = 10
    print(li)

Lis = [20, 20, 20]
callByReference(Lis) # [10, 20, 20]
print(Lis) # [10, 20, 20]

LisAdd = sum(Lis, start=5)
print(LisAdd)

def collection(a, b):
    print(a, b)
collection(10, 20)
collection(*[10, 20]) # list를 분할해서 a에 10, b에 20이 대입
collection(*{"a" : 10, "b": 20}) # a b
# * 이 1개이므로 key 값이 매개변수에 전달됨
collection(**{"a" : 10, "b": 20}) # 10 20
# * 이 2개이므로 value 값이 매개변수에 전달됨
# 이 때 key 이름과 매개변수 이름이 같아야 함.