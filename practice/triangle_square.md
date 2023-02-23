# 삼각형, 사각형 유형 확인하기

## 삼각형

```python
s_triangle = []
s_triangle.append((input('삼각형 변의 길이 작은 순서대로 3개를 입력하세요 : ').split()))

if int(s_triangle[0][2]) < (int(s_triangle[0][0]) + int(s_triangle[0][1])):
    if s_triangle[0][0] == s_triangle[0][1] and s_triangle[0][1] == s_triangle[0][2]:
        print("정삼각형입니다.")
    elif (s_triangle[0][0] == s_triangle[0][1]) or (s_triangle[0][1] == s_triangle[0][2]) or (s_triangle[0][2] == s_triangle[0][0]):
        print("이등변삼각형입니다.")
    elif (int(s_triangle[0][2])**2) == (int(s_triangle[0][0])**2) + (int(s_triangle[0][1])**2):
        print("직각삼각형입니다.")
    else:
        print("삼각형입니다.")
else:
    print("삼각형이 아닙니다.")
```

## 사각형(oop 형태)

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # def __repr__(self):
    #     return f'({self.x}, {self.y})'
    

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    # def __repr__(self):
    #     return f'(({self.a.x}, {self.a.y}), ({self.b.x}, {self.b.y}))'
    
    def get_area(self):
        return (self.b.x - self.a.x)*(self.a.y - self.b.y)
        
    def get_perimeter(self):
        return (2*((self.b.x - self.a.x) + (self.a.y - self.b.y)))     
    
    def is_square(self):
        if ((self.b.x == self.a.x) or (self.a.y == self.b.y)):
            return 'False'
        else:
            return 'True'
  

# 입력 예시
p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)

print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())

# 출력 예시
# 4
# 8
# True

# 9
# 12
# True
```