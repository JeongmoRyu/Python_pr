# 회문(Palindrome)& 애너그램(Anagram)
   
   
## 회문(Palindrome)

‘이상한 변호사 우영우’

“기러기 토마토 스위스 인도인 별똥별 역삼역”

- 맞는 회문 단어를 print해보자  
  

```python
word_list = ['wow', 'radar', 'level', 'noon', 'mom', 'afaewds']

def is_palindrome(word_list):
    parlindrome_list = []
    for word in word_list:
        if word == word[::-1]:
            parlindrome_list.append(word)
    return parlindrome_list
print(is_palindrome(word_list))
```
   
    
```
word = 'input'
# 정석
result = ''
for i in range(len(word)-1, -1, -1):
    result += word[i]

print('result 1: ', result)

# 정석
result = ''
for char in word:
    result = char + result
print('result 1: ', result)

# 파이썬 식
print('result 1: ', word[::-1])
```
  
  
## 애너그램(Anagram)

- ‘다빈치코드’
    - O, Draconian devil!  = leonardo da vinci!
- ‘해리포터’
    - Tom Marvolo Riddle = I am Lord Voldemort
  
  
```python
list_x = ['eat','tea','tan','ate','nat','bat', 'o draconian devil', 'leonardo da vinci','tom marvolo riddle', 'i am lordvoldemort']
list_y = {}
for x in list_x:
    y = ''.join(sorted(x))
    list_y[y] = list_y.get(y,[]) + [x]
z = list_y.values()
print(list_y)
print(list(z))
```

- {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat'], ' aacddeiilnnoorv': ['o draconian devil', 'leonardo da vinci'], ' addeillmmooorrtv': ['tom marvolo riddle', 'i am lordvoldemort']}
- [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'], ['o draconian devil', 'leonardo
da vinci'], ['tom marvolo riddle', 'i am lordvoldemort']]