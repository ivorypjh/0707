# polymorphism을 적용하는 예시
def attackAtype():
    print("A attack")

def attackBtype():
    print("B attack")

delegate = attackAtype
delegate()

delegate = attackBtype
delegate()

# 함수 내부에서 함수를 만들어서 리턴하면 고위 함수
def outerF():
    def innerF():
        print("내부 생성 함수")
    return innerF

# 함수를 호출해서 그 결과를 변수에 대입하고 그 변수를 통해서 함수를 호출
func = outerF()
func()