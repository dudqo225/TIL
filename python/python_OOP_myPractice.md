# python | OOP_Practice



### 객체지향 프로그래밍(OOP) 이해를 위한 코드 연습

- `class` 생성 및 `instance` , `method` 등과 관련된 예시 코드를 작성해보자.
- `class` 생성시 생성자 `__init__()` 이 기본적으로 들어가야 된다.
  - 필요 없는 경우도 있다. 부모-자식 클래스 상속할 때, 똑같은 생성자이면 굳이 만들 필요 X!

- `super()` : 부모 클래스의 내용을 사용하면서 자식 클래스에 메서드를 추가를 구현하고자 할 때 사용
- 메서드 오버라이딩 : 부모 클래스의 메서드를 자식 클래스에서 재정의하는 것



#### 코드 예시

```python
# Point(점) 클래스 생성
class Point():
    # 생성자 메서드 : x, y 축 값을 매개변수로 받아온다. self 인자는 첫 번째 인자로 들어간다.
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Rectangle(사각형) 클래스 생성 - Point 클래스를 부모클래스로 받아옴.
class Rectangle(Point):
    
    # 생성자 메서드 : Point 클래스를 통해 만들어진 2개의 인스턴스를 매개변수로 받아온다. 마찬가지로 self 인자는 첫번째 인자.
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        # point1 ~ point2 x 값 차이 = 가로 | point1 ~ point2 y 값 차이 = 세로
        self.width = abs(self.point1.x - self.point2.x)
        self.height = abs(self.point1.y - self.point2.y)
    
    # 넓이 구하는 메서드 : 가로 x 세로
    def get_area(self):
        return self.width * self.height
    
    # 둘레 구하는 메서드 : (가로 + 세로) * 2
    def get_perimeter(self):
        return (self.width + self.height) * 2
    
    # 정사각형인지 판단하는 메서드 : 가로와 세로의 길이가 같으면 정사각형이므로, True를 반환
    def is_square(self):
        return self.width == self.height
```



> ✨ 객체지향 프로그래밍(OOP) 는 하루이틀한다고 100% 이해되는 것이 아니다. 절대로!!!
>
> 그러니까 꾸준히 코드를 짜보고, 예시를 보면서 서서히 익히자.

