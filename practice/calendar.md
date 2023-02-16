# Leap year, Common year and Calendar


## Leap year, Common year 윤년, 평년 구별하기


- 윤년, 평년 구별하여 표시하기

```python
year = int(input('년도를 입력하세요 : '))

if year%4 == 0 and not year%100 == 0:
    print('윤년')
elif year%400 == 0:
    print('윤년')
else:
    print('평년')
```

- 좀더 짧게 해보면

```python

if ((year%4 == 0) and not (year%100 == 0)) or (year%400 == 0):
        print('윤년')
else:
		print('평년')
```




## 달력 표시하기

```python
year = int(input('년도를 입력하세요 : '))

- 입력하는 달력 년도 전체를 print하기

print(calendar.calendar(year))

month = int(input('월을 입력하세요 : '))

- 입력하는 달력 년도, 월 print하기

print(calendar.month(year, month)

print(calendar.weekday(year, month, day))
 - 요일까지 표시하기(요일은 0,7으로 표시됨 주의)
```

- 보다 많은 정보를 얻고 싶으면
- [https://docs.python.org/ko/3/library/calendar.html](https://docs.python.org/ko/3/library/calendar.html)  공홈에서 더 확인해볼 수 있습니다.

- 위의 윤년 함수를 조금 수정해서 날짜 및 요일까지 표시를 해보자
    - 월요일에는 ‘월요병’이 도지는데 표현해보자

```python
import calendar

year = int(input('년도를 입력하세요 : '))
while True:
    if ((year%4 == 0) and not (year%100 == 0)) or (year%400 == 0):
        print('윤년입니다.')
        year = int(input('년도를 다시 입력하세요 : '))
    else:
        month = int(input('월을 입력하세요 : '))
        day = int(input('일을 입력하세요 : '))
        yymmdd = {
            '년': year,
            '월': month,
            '일': day,
            '요일': calendar.weekday(year, month, day)
            }
        if calendar.weekday(year, month, day) == 0:
            print('월요병 싫어 ㅠㅠ')
            print(yymmdd)
            break
        else:
            print(yymmdd)
            break
```

숫자가 아닌 요일로 표현하고 싶으면 

```python
A = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일'] 를
else의 day와 yymmdd사이에 넣어주시고 
요일표시를 A[calendar.weekday(year, month, day)] 변경들 해주시고
숫자 0도 '월요일' 바꿔야겠죠??
```

마무리를 해보자면


```python
import calendar

year = int(input('년도를 입력하세요 : '))
while True:
    if ((year%4 == 0) and not (year%100 == 0)) or (year%400 == 0):
        print('윤년입니다.')
        year = int(input('년도를 다시 입력하세요 : '))
    else:
        month = int(input('월을 입력하세요 : '))
        day = int(input('일을 입력하세요 : '))

        print(calendar.calendar(year)) # '1년 달력도 넣어주시고'

        A = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
        yymmdd = {
            '년': year,
            '월': month,
            '일': day,
            '요일': A[calendar.weekday(year, month, day)]
            }
        if A[calendar.weekday(year, month, day)] == '월요일':
            print('경고! 월요일입니다.')
            print(yymmdd)
            break
        else:
            print(yymmdd)
            break
```