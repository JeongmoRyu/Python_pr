# Python  input 입력하기

## 입력하기(Input)

```python 
a = input()
a = a.split() 분리해서 입력
print(a)

print()
```

## 파일 입력하기(Input)

- import sys
- sys.stdin = open(”number.txt”, “r”) - 지금부터 number.txt 파일에서 입력을 한다.

- **리스트 입력하기**

```python 
T = int(input())
a= list(map(int,input().split()))
```

- **T 행별(숫자로 입력하기)로 입력하기**

```python 
T = int(input())
for test_case in range(1, T + 1):
a= list(map(int,input().split()))
# a = input().split()
print(a)
```

[1, 2, 3, 4, 5, 6, 7, 8, 9]

[1, 2, 3, 4, 5, 6, 7, 8, 9]

[1, 2, 3, 4, 5, 6, 7, 8, 9]

- **T 행별(문자로 입력하기)로 입력하기**

```python 
T = int(input())
for test_case in range(1, T + 1):
    a= list(map(str,input().split()))
    # a = input().split()
    print(a)
```

[’1’, ‘2’, ‘3’, ‘4’, ‘5’, ‘6’, ‘7’, ‘8’, ‘9’]

[’1’, ‘2’, ‘3’, ‘4’, ‘5’, ‘6’, ‘7’, ‘8’, ‘9’]

[’1’, ‘2’, ‘3’, ‘4’, ‘5’, ‘6’, ‘7’, ‘8’, ‘9’]