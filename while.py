counter = 5

while counter >= 1:
    print(counter)
    counter = counter -1
    if counter == 1:
        break 
# break 를 만나서 정지되면 else 를 처리하지 않음
# break 뿐만 아니라 예외가 발생하는 경우에도 else를 처리하지 않음
# 정상적으로 반복을 완료했는지 확인하는 용도로 사용 가능
else: 
    print("반복 정상적으로 종료")

# counter는 1에서 끝나는게 아니라 0까지 내려감
print(counter) 

# 무한 반복
while True:
    counter += 1
    if counter == 10:
        break

print(counter)
