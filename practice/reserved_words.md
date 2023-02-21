# 예약어(Reserved words)
   
   
- 프로그래밍 언어 중에서 의미가 고정되어 있고, 사용자가 작성하는 프로그램 상태에 따라서 의미를 변경할 수 없는 단어를 뜻한다.
- Python을 실행하였을 때 이미 사용할 수 있는 단어 및 명령어이다.

## 직접 찾아보고 싶다면

```python
import keyword
import pprint

print(type(keyword.kwlist))
print(len(keyword.kwlist))

pprint.pprint(keyword.kwlist, compact = True)
```

결과 값으로 이렇게 나온다.(python 3.9버전입니다)

```jsx
<class 'list'>
36
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert',
'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import',
'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
'return', 'try', 'while', 'with', 'yield']
```

- 문자열이 키워드가 맞는지 확인하는 방법

```python
print(keyword.iskeyword('False'))
print(keyword.iskeyword('false'))
```

+@ 참고로 print, list와 같은 내장 함수(Built_in function)의 경우에는 키워드는 아니지만 오류를 발생시킬 수 있으니 리스트명(?!)으로 사용하지 않는 것이 좋습니다.