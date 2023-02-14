# Python number 2

## 소금물 농도 구하기

학교 졸업하고 수학 때 머가 가장 기억에 남는지 생각해보면
근의 공식, 소금물의 농도 구하기, 그리고 거리와 속력이었던 것 같아요.
그래서 한번 소금물을 파이썬으로 구현해보기로 해요!

```python
x = int(input('소금의 양을 입력하세요 : '))
y = int(input('소금물의 양을 입력하세요 : '))
z = x*100/y
print(str(z) + '%')
```

ex) input(1, 2) = (30, 400) z = 7.5%


## 혼합 소금물 농도 구하기



```python
# 농도와 소금물이 주어지고 짜다라는 표시를 해주면 넣어준 만큼 혼합 농도를 표시해줘

s_list = []
x = 0
y = 0
for a in range(5):
    s_list.append(list(input('소금물의 농도와 양을 넣으세요 : ').split()))

    if 'salty' in s_list[a][0]:
        break
    else:
        x += int(s_list[a][0])*int(s_list[a][1])/100
        y += int(s_list[a][1])
    

print(round(x/y*100,2),'%')
```

## Generator



- 입력된 숫자와 자리 수들의 합을 구하는 함수를 만들어보자

```
n = int(input('제너레이터가 되는 숫자를 입력하세요 : '))

def fn_d(n):
    added = n
    for y in range(len(str(n))):
        added += int(str(n)[y])
    print(added)
    return added
fn_d(n)
```



```python
n = int(input('제너레이터가 되는 숫자를 입력하세요 : '))
fn_d = lambda n: sum([int(c) for c in str(n)] + [n])
print(fn_d(n))
```

ex) 159( 1 + 5 + 9 + 159 ) 는 174의 제너레이터가 된다.



## 셀프 넘버(Self-number)


```python
n = int(input('제너레이터가 되는 숫자를 입력하세요 : '))
fn_d = lambda n: sum([int(c) for c in str(n)] + [n])
print(fn_d(n))

x = int(input('셀프 넘버인지 확인해보자 : '))
def is_selfnumber(x):
    return len([i for i in range(x) if fn_d(i) == x]) == 0
if is_selfnumber(x) == True:
    print(x)
    print('셀프 넘버입니다.')
else:
    print('셀프 넘버가 아닙니다.')
```

## 숫자를 글자로 변경하기



<b>itoa()를 구현해보기</b>

```python 
# 정수를 문자로 변환하기

"""
5(test_case)숫자
3
1461134
938412
15768
-1213
"""
T = int(input())

for test_case in range(1, T+1):
    word = int(input())
    result = ''

    num_str = '0123456789'
		
		# 음수 일 경우 양수로 변경해 준다.
    is_negative = False
    if word < 0:
        word = word * -1
        is_negative = True

    while word > 0:
        # word의 숫자들을 빼다가 더 뺄게 없을때까지
        digit = word % 10
        # 1의 자리
        result = num_str[digit] + result
        word = word //10
    # 음수였던 숫자를 문자로 바꾸어 줬기에 -문자를 더 적어줘야한다.
		if is_negative:
        result = '-' + result
		print(type(result))
		# 확인해보면 문자열로 변경되어 있는 것을 알 수 있을 것이다.
    print(f'#{test_case} {result}')

```