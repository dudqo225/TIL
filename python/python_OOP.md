# python | Object-Oriented Programming (OOP)

### 객체

- 파이썬에서 사용되는 모든 것. 변수, 자료 구조, 함수, 메서드 등등

- 파이썬은 모두 객체(object)로 이루어져 있다.
- 객체(object)는 특정 타입의 인스턴스(instance) 이다.
- 특징
  - 타입(type) : 어떤 연산자(operator)와 조작(method)이 가능한가?
  - 속성(attribute) : 어떤 상태(데이터)를 가지는가?
  - 조작법(method) : 어떤 행위(함수)를 할 수 있는가?

- `is` 연산자

  - 객체의 아이덴티티를 검사하는 연산자

- `isinstance` 함수

  - `isinstance(object, classinfo)`
    - classinfo의 instance거나 subclass인 경우 `True`
    - classinfo가 type으로 구성된 tuple인 경우 하나라도 일치하면 `True`
    - classinfo가 type이거나 type으로 구성되지 않은 경우 `TypeError`

- **속성(attribute)**

  - `<object>.<attribute>`
  - 속성은 객체의 상태/데이터
  - 속성에는 `()` 괄호가 없다.

  ```python
  (3 + 4j).real
  3.0
  
  (3 + 4j).imag
  4.0
  ```

- **메서드(method)**

  - `<object>.<method>()`
  - 메서드는 특정 객체에 적용될 수 있는 행위를 뜻하며, 일반적으로 클래스에 정의된 함수임

  ```python
  [1, 2, 3].pop()
  3
  
  'hello!'.capitalize()
  'Hello!'
  
  {'a': 'apple'}.items()
  dict_items([('a', 'apple')])
  ```



### 객체지향 프로그래밍(OOP)

- OOP는 컴퓨터 프로그래밍의 패러다임 중 하나이다.
- OOP는 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러개의 독립된 단위, 즉 "객체" 들의 모임으로 파악하려는 것

- vs. 절차지향 프로그래밍
  - 함수 호출을 통해서 프로그램의 변화를 일으킴
- 객체지향 프로그래밍은
  - 데이터와 기능(메서드)를 분리, 추상화된 구조(인터페이스)
  - 현실세계를 프로그램 설계에 반영(**추상화**)

- 예시

```python
# 사각형 넓이 구하기

# 1. 절차지향 프로그래밍
def area(x, y):
    return x * y

def circumference(x, y):
    return 2 * (x + y)

a = 10
b = 30
c = 300
d = 20
square1_area = a * b
square1_circumference = 2 * (a + b)
square1_area = c * d
square1_circumference = 2 * (C + d)


# 2. 객체지향 프로그래밍
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def area(self):
        return self.x * self.y
    
    def circumference(self):
        return 2 * (self.x + self.y)
    

r1 = Rectangle(10, 30)
r1.area()
r1.circumference()

r2 = Rectangle(300, 20)
r2.area()
r2.circumference()
```

- 예시 정리
  - 사각형 : `class`
  - 사각형의 정보 (가로 , 세로 길이) : `attribute`
  - 사각형의 행동 (넓이, 높이) : `method`
  - 사각형 1, 사각형 2 : `instance`
- 클래스(class)와 인스턴스(instance)
  - 클래스를 **정의**하고, 인스턴스들을 만들어서 **활용**함
    - 클래스 : 객체들의 분류 (class)
    - 인스턴스 :  하나하나의 실체/예시 (instance)
- 속성(attribute)
  - 특정 데이터 타입/클래스의 객체들이 가지게 될 상태/데이터를 의미
- 메서드(method)
  - 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위(**함수**)
- **self**
  - 인스턴스 자기 자신
  - 인스턴스 메서드는 호출시 첫번째 인자로 인스턴스 자신이 전달되도록 설계
    - 매개변수 이름으로 `self` 를 첫번째 인자로 정의
- 생성자(constructor)
  - 인스턴스 객체가 생성될 때 호출되는 메서드
  - `__init__()`
- 소멸자(destructor)
  - 인스턴스 객체가 소멸(파괴)되기 직전에 호출되는 메서드
  - `__del__()`
- 매직 메서드
  - Double underscore(__) 혹은 던더 스코어가 있는 메서드는 특수한 동작을 위해 만들어진 메서드
  - 스페셜 메서드 혹은 매직 메서드라고 불림
  - 예시
    - `__str__(self)` : 해당 객체의 출력 형태를 지정
    - ``__gt__(self, other)` : 부등호 연산자
    - 생성자
    - 소멸자



### 클래스와 인스턴스

- 인스턴스 변수
  - 인스턴스의 속성(attribute)
  - 각 인스턴스들의 고유한 변수
    - 메서드에서 `self.<name>` 으로 정의
    - 인스턴스가 생성된 이후 `<instance>.<name>` 으로 접근 및 할당
- 클래스 변수
  - 클래스 속성(attribute)
  - 모든 인스턴스가 공유
  - 클래스 선언 내부에서 정의
  - `<classname>.<name>` 으로 접근 및 할당
- 인스턴스와 클래스 간의 이름 공간 (namespace)
  - 클래스를 정의하면, 클래스와 해당하는 이름 공간을 생성
  - 인스턴스를 만들면, 인스턴스 객체가 생성되고 이름 공간 새엉
  - 인스턴스에서 특정 속성에 접근하면, **인스턴스 → 클래스 순으로 탐색**
- 메서드의 종류
  - 인스턴스 메서드
    - 인스턴스가 사용할 메서드
    - 클래스 내부에 정의되는 메서드의 기본
    - **호출 시, 첫번째 인자로 인스턴스 자기자신(`self`)이 전달됨**
  - 클래스 메서드
    - 클래스가 사용할 메서드
    - **`@classmethod`** 데코레이터를 사용하여 정의
    - **호출 시, 첫번째 인자로 클래스(`cls`)가 전달됨**
  - 스태틱 메서드
    - 클래스가 사용할 메서드
    - **`@staticmethod`** 데코레이터를 사용하여 정의
    - **호출 시, `self` 나 `cls` 인자가 전달되지 않음** (클래스 정보에 접근 및 수정이 불가)
- 메서드 정리
  - 메서드는 해당 함수에서 어떤 값을 활용하고 변경하는지에 따라 정의
    - 인스턴스는 **모든 메서드를 호출** 할 수 있음. ☝ **But, != 사용한다**
    - **인스턴스 동작은 반드시 인스턴스 메서드로 정의**
    - 클래스는 클래스 속성 접근 여부에 따라 클래스 메서드 or 스태틱 메서드로 정의

- 객체지향 프로그래밍 정리
  - 클래스 구현
    - 클래스 정의
    - 데이터 속성 정의 (객체의 정보가 무엇인지)
    - 메서드 정의 (객체를 어떻게 사용할 것인지)
  - 클래스 활용
    - 해당 객체 타입의 인스턴스를 생성하고 조작



### 상속

- 클래스는 상속이 가능
  - 모든 파이썬 클래스는 `object` 를 상속 받음
- 상속을 통해 객체 간 관계를 구축
- 부모 클래스의 속성, 메서드가 자식 클래스에 상속되므로 **코드 재사용성**이 높아짐

```pyhton
class ChildClass(ParentClass):
    pass
```

- 상속 `isinstance`
  - `isinstance(object, classinfo)` : classinfo의 instance거나 subclass 인 경우 `True`

- `issubclass`

  - `issublcass(class, classinfo)`
    - class 가 classinfo 의 subclass 이면 `True`
    - classinfo 는 클래스 객체의 튜플일 수 있으며, classinfo 의 모든 항목을 검사

- `super()`

  - 자식 클래스에서 부모 클래스를 사용하고 싶은 경우

- 메서드 오버라이딩(method overriding)

  - 상속 받은 메서드를 재정의
    - 상속 받은 클래스에서 같은 이름의 메서드로 덮어씀
    - 부모 클래스의 메서드를 실행시키고 싶은 경우 `super` 를 활용

- 다중 상속

  - 두 개 이상의 클래스를 상속받는 경우 다중 상속이 됨

    - 상속 받은 모든 클래스의 요소 활용 가능
    - 중복된 속성, 메서드가 있는 경우 상속 순서에 의해 결정됨

    ```python
    # class A와 B가 있다고 가정
    
    class C(A, B): # 상속순서 A, B
        pass
    class D(B, A): # 상속순서 B, A
        pass
    ```

- 상속 정리

  - 파이썬 모든 클래스는 `object` 로부터 상속됨
  - 부모 클래스의 모든 요소(속성, 메서드)가 상속됨
  - `super()` 를 통해 부모 클래스의 요소 호출이 가능
  - 메서드 오버라이딩을 통해 자식 클래스에서 재정의가 가능함
  - 상속관계에서의 이름 공간은 인스턴스 → 자식 클래스 → 부모 클래스 순으로 탐색





> 너무 어렵다 🤣 2021.07.28
>
> 파이썬 이스터에그 `import this`

