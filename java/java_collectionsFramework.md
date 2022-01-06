# JAVA | Collections Framework

### 목차

> 1. 배열과 ArrayList
> 2. Collections Framework

<br>

***

### 1. 배열과 ArrayList

#### 배열

- 배열의 크기를 한번 정하면, 변경할 수 없음
- 값의 개수를 구할 때 - `.length()`
- 값을 가져올 때 - `[인덱스번호]`

```java
// 배열 예시 코드
String[] arrayObj = new String[2];
arrayObj[0] = "one";
arrayObj[1] = "two";
// arrayObj[2] = "three"; 오류 발생
```

<br>

#### ArrayList

- 크기를 미리 지정하지 않기 때문에, 많은 수의 값을 저장할 수 있음

- 값의 개수를 구할 때 - `.size()`
- 값을 가져올 때 - `.get(인덱스번호)`

```java
// ArrayList 예시 코드
ArrayList al = new ArrayList();
al.add("one");
al.add("two");
al.add("three");
```

##### ArrayList 사용시 주의할 부분

```java
// ArrayList 반복문 - 컴파일 오류 발생
for(int i=0; i<al.size(); i++){
    String val = al.get(i);
    System.out.println(val);
}
```

- 컴파일 오류가 발생
  - `.add()` 메소드는 인자로 어떤 형태의 값이 올지 알 수 없기 때문에, `Object` 타입으로 데이터를 받음
  - 따라서 `.get()` 메소드로 데이터를 꺼낼 때 `Object` 데이터 타입을 가지고 있음
  - 형변환이 필요함 `al.get(i)` → `(String)al.get(i)`

<br>

```java
// ArrayList 반복문 - 형변환 코드
for(int i=0; i<al.size(); i++){
    String val = (String)al.get(i);
    System.out.println(val);
}
```

- 예전의 방식. 제네릭을 사용해야 한다

<br>

```java
// ArrayList 제네릭 사용
ArrayList<String> al = new ArrayList<String>();
al.add("one");
al.add("two");
al.add("three");

for(int i = 0; i < al.size(); i++){
    String val = al.get(i);
    System.out.println(val);
}
```

- 제네릭 `<>` 을 사용하여 데이터 타입을 `String` 으로 설정하였기 때문에 데이터를 꺼낼 때 별도의 형변환을 하지 않아도 됨

<br>

***

### 2. Collections Framework

