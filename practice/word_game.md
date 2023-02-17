# 끝말잇기 게임하기
  
  
- **리스트가 주어졌을 경우**
    -  틀린 사람까지 찾기

  
```python
words = ["roll" , "liver", "rectangle" , "radar" , "radar", "risk", "kiwi"]

for a in range(0,6):   #리스트 수를 통해서 확인
    if words[a] == words[a+1]:
        print(a+1)
    elif words[a][-1] == words[a+1][0]:
        print('')
    elif input('done'):
        break
    else:
        print('you lose')
```
  

- **직접 입력해서 하는 끝말잇기 게임**
    - 틀린 x번째 사람 찾기  
  
```python
words = input('끝말잇기 단어를 넣어보자 : ').split(",")
next_words = input('now your turn : ').split(",")
words = words + next_words
a = 0
while True:
    a = a + 1
    if words.count(words[a]) == 2:
        print(a+1)
        break
    elif words[a-1][-1] == words[a][0]:
        words = words + input('now your turn! : ').split(",")
    elif input(' : ') == 'done':
        break
    else:
        print('you lose!!')

+@ 수정필요 practice
```