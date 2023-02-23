# 입 출입 기록으로 도둑 찾기, 비밀번호 입력


## 입 출입 기록으로 도둑 찾기  
  
input
```python
entry_record = ['E', 'B', 'A', 'E', 'A', 'F', 'C', 'A', 'A', 'E', 'H', 'C', 'G', 'F', 'H', 'D', 'B', 'A', 'G', 'A', 'D', 'B', 'C', 'C', 'E', 'C', 'F', 'A', 'D', 'C', 'B', 'G', 'H', 'D', 'C', 'B', 'E', 'H', 'C', 'F', 'G', 'H', 'E', 'F', 'H', 'E', 'B', 'B', 'H', 'H', 'H', 'D', 'G', 'F', 'F', 'G', 'E', 'C', 'H']

exit_record = ['G', 'A', 'E', 'H', 'C', 'H', 'E', 'F', 'D', 'B', 'G', 'E', 'D', 'D', 'B', 'C', 'E', 'B', 'H', 'D', 'E', 'A', 'A', 'C', 'B', 'E', 'A', 'B', 'F', 'H', 'A', 'C', 'H', 'H', 'C', 'A', 'G', 'H', 'C', 'D', 'E', 'C', 'H', 'F', 'H', 'F', 'C', 'D', 'C', 'B', 'A', 'E', 'G', 'G', 'F', 'F', 'D', 'F', 'H', 'B']




from collections import Counter

Counter_entry = Counter(entry_record)
Counter_exit = Counter(exit_record)
print('입장 기록이 많은 Top 3')
print(str(Counter_entry.most_common()[0][0]) + ' ' + str(Counter_entry.most_common()[0][1]) + '회')
print(str(Counter_entry.most_common()[1][0]) + ' ' + str(Counter_entry.most_common()[1][1]) + '회')
print(str(Counter_entry.most_common()[2][0]) + ' ' + str(Counter_entry.most_common()[2][1]) + '회')

print('')
print('출입 기록이 수상한 사람')

for a in range(len(Counter_entry.items())):
    if sorted(Counter_entry.items())[a][0] == sorted(Counter_exit.items())[a][0]:
        
        if sorted(Counter_entry.items())[a][1] > sorted(Counter_exit.items())[a][1]:

            print(str(sorted(Counter_entry.items())[a][0]) + '(이/가)' + str(sorted(Counter_entry.items())[a][1] - sorted(Counter_exit.items())[a][1]) + '회 입장을 많이 하여 수상합니다.')

        elif sorted(Counter_entry.items())[a][1] < sorted(Counter_exit.items())[a][1]:

            print(str(sorted(Counter_entry.items())[a][0]) + '(이/가)' + str(sorted(Counter_exit.items())[a][1] - sorted(Counter_entry.items())[a][1]) + '회 퇴장을 많이 하여 수상합니다.')

```


## 비밀번호 입력하기

```python
# 예시 비밀 번호를 만들어둔다.
valid_password = '123456'
input_password = []
count = 0
while True:
    input_password.append(input('비밀번호를 입력하세요 : '))
    count += 1
    if count < 3:  
        if valid_password in input_password:
            print('비밀번호가 맞습니다.')
            break
        else:
            print('비밀번호가 틀렸습니다.')    
    else:
        print('비밀번호를 너무 많이 입력하셨습니다.')
        break
```

