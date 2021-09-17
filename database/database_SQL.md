# Database | SQL

<br>

### SQL (Structured Query Language)

- RDBMS의 데이터 관리를 위해서 설계된 특수 목적의 프로그래밍 언어
- 데이터베이스 스키마 생성 및 수정
- 자료의 검색 및 관리
- 데이터베이스 객체 접근 조정 관리

<br>

### SQL 분류

- DDL (Data Definition Language)
  - 데이터 정의 언어
  - 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어
  - 예시
    - CREATE
    - DROP
    - ALTER
- DML (Data Manipulation Language)
  - 데이터 조작 언어
  - 데이터를 저장, 조회, 수정, 삭제 (CRUD) 등을 하기 위한 명령어
  - 예시
    - INSERT (C)
    - SELECT (R)
    - UPDATE (U)
    - DELETE (D)
- DCL (Data Control Language)
  - 데이터 제어 언어
  - 데이터베이스 사용자의 권한 제어를 위해 사용하는 명령어
  - 예시
    - GRANT
    - REVOKE
    - COMMIT
    - ROLLBACK

<br>

### SQL statement

```sql
-- 테이블 생성 및 삭제
CREATE TABLE <테이블명> (컬럼...);
DROP TABLE <테이블명>;

-- CRUD
# CREATE
INSERT INTO <테이블명> (컬럼1, 컬럼2, ...) VALUES (값1, 값2, ...);

# READ
SELECT 컬럼1, 컬럼2, ... FROM <테이블명>;
SELECT 컬럼1, 컬럼2, ... FROM <테이블명> LIMIT 숫자;
SELECT 컬럼1, 컬럼2, ... FROM <테이블명> LIMIT 숫자 OFFSET 숫자;
SELECT 컬럼1, 컬럼2, ... FROM <테이블명> WHERE 조건;
SELECT DISTINCT 컬럼 FROM <테이블명>;

# DELETE
DELETE FROM <테이블명> WHERE 조건;

# UPDATE
UPDATE <테이블명> SET 컬럼1=값1, 컬럼2=값2, ... WHERE 조건;
```

<br>

#### AUTOINCREMENT

- 컬럼 attribute
- 이전에 삭제된 행의 값을 재사용하는 것을 방지
- SQLite에서는 사용되지 않음
- 테이블을 생성하는 단계에서 설정 가능

```sql
CREATE TABLE <테이블명> (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	...
	);
```

<br>

### SQLite Aggregate Functions

- COUNT

  - 그룹의 항목 수를 가져옴

- AVG

  - 값 집합의 평균 값을 계산

- MAX

  - 그룹에 있는 모든 값의 최대값을 가져옴

- MIN

  - 그룹에 있는 모든 값의 최소값을 가져옴

- SUM

  - 모든 값의 합을 계산

  ```sqlite
  SELECT COUNT(컬럼) FROM <테이블명>;
  SELECT AVG(컬럼) FROM <테이블명>;
  SELECT MAX(컬럼) FROM <테이블명>;
  SELECT MIN(컬럼) FROM <테이블명>;
  SELECT SUM(컬럼) FROM <테이블명>;
  ```

<br>

#### LIKE

- 패턴 일치를 기반으로 데이터를 조회하는 방법
- sqlite는 패턴 구성을 위한 2개의 wildcards를 제공
  - % (percent sign)
    - 0개 이상의 문자
    - 이 자리에 문자열이 있을 수도, 없을 수도 있다.
  - _ (underscore)
    - 임의의 단일 문자
    - 반드시 이 자리에 한 개의 문자가 존재해야 한다.

```sql
SELECT * FROM 테이블 WHERE 컬럼 LIKE '와일드카드패턴';
```

<br>

#### ORDER BY

- 조회 결과 집합을 정렬
- SELECT 문에 추가하여 사용
- 정렬 순서를 위한 2개의 키워드 제공
  - ASC - 오름차순 (default)
  - DESC - 내림차순

```sql
SELECT * FROM 테이블 ORDER BY 커럼 ASC;
SELECT * FROM 테이블 ORDER BY 컬럼1, 컬럼2 DESC;
```

<br>

#### GROUP BY

- 행 집합에서 요약 행 집합을 만듦
- SELECT 문의 optional 절
- 선택된 행 그룹을 하나 이상의 열 값으로 요약 행으로 만듦
- 문장에 WHERE 절이 포함된 경우 반드시 WHERE 절 뒤에 작성해야 함

```SQL
SELECT 컬럼1, aggregate_function(컬럼2) FROM 테이블 GROUP BY 컬럼1, 컬럼2;
```

<br>

#### ALTER TABLE

- 테이블 이름 변경

```sql
ALTER TABLE current_table_name RENAME TO new_table_name;
```

- 테이블 컬럼 명 변경

```SQL
ALTER TABLE table_name
RENAME COLUMN current_name TO new_name;
```

- 테이블에 새로운 컬럼 추가

```sql
ALTER TABLE 테이블이름 ADD COLUMN 컬럼이름 데이터타입설정;
```

<br>

<br>

### SQL & ORM

#### READ

```sql
# ORM
User.objects.all()

# SQL
SELECT * FROM users_user;
```

<br>

#### CREATE

```sql
# ORM
User.objects.create(
	first_name='길동',
    ...
)

# SQL
INSERT INTO users_user VALUES ('길동', ...);
```

<br>

#### UPDATE

```sql
# ORM
user = User.objets.get(pk=102)
user.last_name = '김'
user.save()

# SQL
UPDATE users_user SET last_name='김' WHERE id=102;
```

<br>

#### DELETE

```sql
# ORM
User.objects.get(pk=102).delete()

# SQL
DELETE FROM users_user WHERE id=102;
```

<br>

#### 활용하기

- 참고 문서
  - https://docs.djangoproject.com/en/3.2/topics/db/queries/
  - https://docs.djangoproject.com/en/3.2/ref/models/querysets/

- 대/소 관계 비교 조건
  - `__gte`
  - `__gt`
  - `__lte`
  - `__lt`
- AND / OR
  - AND
    - `filter(조건, 조건)`
  - OR
    - Q ojbect 활용
    - `filter(Q(조건) | Q(조건))`

- LIKE
  - `filter(속성__startswith='조건')`

- 정렬, LIMIT, OFFSET, etc... 등

<br>

### Django Aggregation

- `aggregate()`
  - 무언가를 종합, 집합, 합계 한다는 사전적 의미
  - 특정 필드 전체의 합, 평균, 개수 등을 계산할 때 사용

```sql
# SQL
SELECT AVG(age) FROM users_user WHERE last_name='김';

# ORM
User.objects.filter(last_name='김').aggregate(Avg('age'))
```

- `annotate()`
  - 주석을 달다 라는 사전적 의미
  - 컬럼 하나를 추가하는 것과 같음
    - 특정 조건으로 계산된 값을 가진 컬럼을 하나 만들고 추가하는 개념
  - annotate()에 대한 각 인자는 반환되는 QuerySet의 각 객체에 추가될 주석이다.
  - **원본 테이블이 변하는 것은 아님**

```sql
# SQL
SELECT country, COUNT(country) FROM users_user GROUP BY country;

# ORM
User.objects.values('country').annotate(num_countries=Count('country'))
```