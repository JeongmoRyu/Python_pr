# Find_vowel_&_minvalue (모음 갯수 찾기 & 단어 중앙 값 찾기)

## 모음 갯수 찾기
- 아, 에, 이, 오, 우
- a, e, i, o, u  
  
```python
vowel_list = ['a', 'e', 'i', 'o', 'u']
def count_vowels(x):
    count = 0
    for a in range(len(x)):
        if x[a] in vowel_list:
            count += 1
    print(count)

count_vowels('apple') #=> 2
count_vowels('banana') #=> 3
```


## 단어 중앙 값 찾기
    
    
```python
A = input('문자열은? : ')

def middle_str(str):
    if len(str)%2:
        return str[len(str)//2]
    else:
        return str[len(str)//2-1 : len(str)//2+1]
print(middle_str(A))
```
