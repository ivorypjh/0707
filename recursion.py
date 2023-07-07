import functools
@functools.lru_cache() # 메모이제이션 : 함수의 호출 결과를 저장해두고 재사용
# 피보나치 재귀 함수
def fibo(n : int) -> int:
    if n == 1 or n == 2:
        return 1
    return fibo(n-1) + fibo(n-2)

fibo.__doc__ = "재귀 방식을 사용해서 피보나치 수열의 값을 리턴하는 함수"
help(fibo)
