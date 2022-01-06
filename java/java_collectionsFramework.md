# JAVA | Collections Framework

### 목차

> 1. 배열과 ArrayList
> 2. Collections Framework
> 3. 참고 자료

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

#### Collections Framework란?

- Collections Framework, 컨테이너라고도 부른다. 값을 담는 그릇이라는 의미
- 구성
  - Collection
    - Set (중복 허용 X)
      - HashSet
      - LinkedHashSet
      - TreeSet
    - List (중복 허용 O)
      - ArrayList
      - Vector
      - LinkedList
    - Queue
      - PriorityQueue
  - Map
    - SortedMap
      - TreeMap
    - Hashtable
    - LinkedHashMap
    - HashMap

<br>

```java
// Collections Framework - Collection 인터페이스 사용 예시
package ...
    
import java.util.ArrayList;
import java.util.HashSet;

import java.util.Iterator;

public class ListSetDemo {
    
    public static void main(Strin[] args) {
        // ArrayList 예시
        ArrayList<String> al = new ArrayList<String>();
        al.add("one");
        al.add("two");
        al.add("two");
        al.add("three");
        al.add("three");
        al.add("five");
       	System.out.printIn("array");
        
        Iterator ai = al.iterator();
        while(ai.hasNext()){
            System.out.printIn(ai.next());
        }
        
        // HashSet 예시
        HashSet<String> hs = new HashSet<String>();
        hs.add("one");
        hs.add("two");
        hs.add("two");
        hs.add("three");
        hs.add("three");
        hs.add("five");
        System.out.printIn("\nhashset");
        
        Iterator hi = hs.iterator();
        while(hi.hasNext()){
            System.out.printIn(hi.next());
        }
    }
}
```

```java
// 결과
array
one
two
two
three
three
five

hashset
two
five
one
three
```

- 메소드 `iterator()`
  - 인터페이스 Collection에 정의되어 있음
  - 이 메소드의 호출 결과는 인터페이스 iterator를 구현한 객체를 리턴
    - `hasNext` : 반복할 데이터가 더 있으면 `true`, 없으면 `false`를 리턴
    - `next` : hasNext가 `true`라는 것은 next가 리턴할 데이터가 존재한다는 의미
  - for 문을 사용하는 것과 동일하게 데이터의 순차적인 처리 가능

<br>

#### Set

- 집합
- 순서가 없고 중복되지 않는 특성이 있다.
- 교집합(intersect), 차집합(difference), 합집합(union) 연산이 가능함

##### 부분집합(subset)

- `A.containsAll(B)`
  - `true` : B는 A의 부분집합이다
  - `false` : B는 A의 부분집합이 아니다

##### 합집합(union)

- `A.addAll(B)`
  - A와 B의 합집합

##### 교집합(intersect)

- `A.retainAll(B)`
  - A와 B의 교집합

##### 차집합(difference)

- `A.removeAll(B)`
  - A와 B의 차집합

<br>

#### Map

- key - value 상으로 값을 저장하는 컬렉션

```java
// Map 컬렉션 활용 예시
package ...;

import java.util.*;

public class MapDemo {
    public static void main(String[] args) {
        HashMap<String, Integer> a = new HashMap<String, Integer>();
        a.put("one", 1);
        a.put("two", 2);
        a.put("three", 3);
        a.put("four", 4);
        System.out.printIn(a.get("one"));
        System.out.printIn(a.get("two"));
        System.out.printIn(a.get("three"));
        
        iteratorUsingForEach(a);
        iteratorUsingIterator(a);
    }
    
    // for-each 활용
    static void iteratorUsingForEach(HashMap map) {
        Set<Map.Entry<String, Integer>> entries = map.entrySet();
        for (Map.Entry<String, Integer> entry : entries) {
            System.out.printIn(entry.getKey() + " : " + entry.getValue());
        }
    }
    
    // while 활용
    static void iteratorUsingIterator(HashMap map) {
        Set<Map.Entry<String, Integer>> entries = map.entrySet();
        Iterator<Map.Entry<String, Integer>> i = entries.iterator();
        while(i.hasNext()) {
            Map.Entry<String, Integer> entry = i.next();
            System.out.printIn(entry.getKey() + " : " + entry.getValue());
        }
    }
}
```

- `put()`
  - 데이터를 추가할 때 사용하는 API
  - 첫번째 인자 - key
  - 두번째 인자 - value
  - key를 이용해서 값을 가져올 수 있음 (`.get(key)`)

- `.entrySet()`
  - Map의 데이터를 담고 있는 Set을 반환
  - 반환된 Set이 사용하는 데이터 타입은 `Map.Entry`(인터페이스)
    - `.getKey()` - 키 조회
    - `.getValue()` - 값 조회

<br>

#### 데이터 타입의 교체

- 컬렉션을 사용할 때 데이터 타입은 해당 컬레션을 대표하는 인터페이스를 사용하는 것이 좋다.
- ex.
  - HashMap의 대표 인터페이스인 Map으로 데이터 타입을 설정하면,
  - 나중에 HaspMap 대신 HashTable을 사용하고 싶으면 컬렉션만 바꾸면 된다.

```java
// 컬렉션의 대표 인터페이스를 데이터 타입으로 설정

// 1. 기존 코드
HashMap<String, Integer> a = new HashMap<String, Integer>();

// 2. HashMap의 대표 인터페이스 Map으로 데이터 타입 변경
Map<String, Integer> a = new HashMap<String, Integer>();

// 3. HashMap을 HashTable로 변경하고자 할 때
Map<String, Integer> a = new HashTable<String, Integer>();
```

<br>

#### 정렬

- 컬렉션 사용 이유 중 하나

 ```java
 // 정렬 사용 예시
 package ... ;
 
 import java.util.*;
 
 class Computer implements Comparable{
     int serial;
     String owner;
     Computer(int serial, String owner) {
         this.serial = serial;
         this.owner = owner;
     }
     public int compareTo(Object o) {
         return this.serial - (Computer)o.serial;
     }
     public String toString() {
         return serial + " " + owner;
     }
 }
 
 public class CollectionDemo {
     public static void main(String[] args) {
         List<Computer> computers = new ArrayList<Computer>();
         computers.add(new Computer(500, "son"));
         computers.add(new Computer(200, "lee"));
         computers.add(new Computer(2323, "kim"));
         
         Iterator i = computers.iterator();
         System.out.printIn("Before");
         while(i.hasNext()) {
             System.out.printIn(i.next());
         }
         
         // Collections의 sort 메소드
         Collections.sort(computers);
         
         i = computers.iterator();
         System.out.printIn("\nAfter");
         while(i.hasNext()) {
             System.out.printIn(i.next());
         }
     }
 }
 ```

```java
// 결과
Before
500 son
200 lee
2323 kim
    
After
200 lee
500 son
2323 kim
```

- 클래스 `Collections` 는 다양한 클래스 메소드를 가지고 있음. `.sort()` 메소드는 그 중 하나로 List의 정렬을 수행함
- `.sort()` 메소드는 List 형식의 컬렉션을 지원함
  - 따라서 sort의 인자 list의 제네릭은 `comparable`을 extends 하고 있어야 함
  - 인터페이스 `comparable`을 구현하고 있는 클래스는 `compareTo(T o)` 메소드를 가지고 있어야 함
    - `compareTo` 메소드를 실행하고 그 결과에 따라서객체의 선후 관계를 판별함
    - 선후 관계를 판별하여 List를 정렬하는 로직

<br>

***

### 3. 참고 자료

[생활코딩 - JAVA | Collections Framework](https://opentutorials.org/course/1223/6446)

<br>

✨ 생활코딩의 JAVA 수업을 한 바퀴 끝냈다. 비전공자로써 파이썬을 먼저 배우고 자바를 배우는 입장이지만 재미있으면서도 어렵다. 타입을 명시하는 점에서 파이썬에 비해 자바가 훨씬 탄탄한 언어라는 생각이 들었다. 그만큼 코드가 좀 더 복잡해지는 점이 있긴 하다. 1주일간 자바 기초를 공부하면서 정어어어엉말로 쌩기초적인 문법은 어느정도 익숙해졌다고 생각한다. 

이제 필요한 것은... 실제로 Java 코드를 작성하고 컴파일해보는 작업을 해봐야겠지?

첫째, 쉬운 알고리즘 문제를 Java로 풀어보는 것

둘째, Back-End에서 많이 쓰는 Spring.. Spring Boot를 RESTful API로 구현하는 것

위 사항들이 단기적인 목표이다.

화이팅💪 2022.01.06

