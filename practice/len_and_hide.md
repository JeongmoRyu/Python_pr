# 글자 수 알아보기 & 주민번호 숨기기

# 글자 수 알아보기



주어진 문자열에서 숫자, 문자, 기호가 각각 몇 개 인지를 판단하는 함수를 작성해보세요

- def check(target_str):

문자와 숫자, 기호가 몇 개 인지 알아보자

- “문자 : 10개,  숫자 : 2개,  기호 : 7개” 이러한 형식으로 한번 표현해보자
   


```python
def check(input_str):
    char_count = 0
    digit_count = 0
    symbol_count = 0

    for char in input_str:
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            symbol_count += 1
    return (char_count, digit_count, symbol_count)

input_str = '123#$%^&aiden-snow'
char_count, digit_count, symbol_count = check(input_str)
print(f"char : {char_count}, digit : {digit_count}, symbol : {symbol_count}")
```  
  
    


# 주민 번호 숨기기

```python
def de_identify(num):
    if len(num) == 14:
        return num[0:6] + "*******"   
    elif len(num) == 13:
        return num[0:6] + "*******"

# def de_identify(social_num):
#     social_num = social_num.replace('-', '')
#     social_num = social_num[:-7]
#     social_num += '*******'
#     return social_num

# def de_identify(social_num):
#			return social_num.replace(',','')[:-7] + '*******'

print(de_identify('970103-1234567'))
print(de_identify('8611232345678'))
```