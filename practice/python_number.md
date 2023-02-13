# Python 숫자

## 절대값 구하기



<b>abs()</b>

```python
abs(-99) = 99
abs(99) = 99
abs(0) = 0
```


## 홀수, 짝수 구하기



```python
num = int(input('숫자 입력 : '))
if num%2 == 0:
    print('짝수입니다.'),
else:
    print('홀수입니다.')
```

## 오름차순, 내림차순 정렬하기



```python 
우선 정렬을 하기 위해서는 리스트로 되어야한다.
만약 리스트가 아닌 set, dict 이러한 경우일 때에는

L = list(set(X))
# 이런 식으로 변환해주어야 한다.
그 후 L.sort()로 정렬부터!!

보통 sort는 오름차순으로 정렬되기에 이렇게 두어도 되지만
만약 확실하게 정렬하고 싶다면
L = list(set(X))
L.sort(reverse = False)
print(L)

내림차순으로는
L = list(set(X))
L.sort(reverse = True)
# False를 True로 바꿔주기만 하면 된다.
print(L)

이외에도 다른 sort방식들이 존재하는데 따로 정리를 하겠습니다.
```


## 몇 자리 수 인지 확인하고 더하기



```python
x = 6789

a = x//10**3
b = (x - (a*1000))//10**2
c = (x - (a*1000) - (b*100))//10
d = x%10
print(a + b + c + d)
```

## input 하였을 때 자리 수 구하기



```python
s = input('숫자를 입력해주세요 : ')
sum = 0
for a in range(len(s)):
    sum += int(s[a])
		print((s[a], end = ',')) # 자리 수 구하기
print('\n', sum)   # 구한 자리 수 합하기
```

## Factorial



n = n * (n-1)  * (n-2) …… * 2 * 1

<b>while문을 사용해서 표현하기</b>

```python
def factorial(n):
    result = 1
    while n > 1:
        result = result * n
        n = n -1
    return result
print(factorial(숫자를 넣어보세요))
```

<b>if문으로도 표현해보자</b>

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(input(숫자를 넣어주세요 : )))
```