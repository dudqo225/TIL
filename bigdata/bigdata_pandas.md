# Bigdata | Pandas

<br>

### Pandas

- Python Data Analysis Library

- 데이터 조작 및 분석을 위한 라이브러리
- SQL, Excel, CSV 파일 및 데이터베이스 데이터를 읽어서 활용 가능

![pandas](images/pandas.png)

#### Pandas 기본 메소드

```python
# pandas 불러오기
import pandas as pd
```

```python
# EXCEL / CSV 파일 읽어온 후 DataFrame으로 저장
df = pd.read_excel("파일 경로")
df1 = pd.read_csv("파일 경로")
```

```python
# 데이터 확인
df.head(5)
```

```python
# DataFrame 행, 열 개수 확인
df.shape
```

```python
## 필요없는 Rows or Columns 삭제
# 행 삭제
df.drop(["Row_Name", "Row_Name"])

# 열 삭제. axis=1 인자 설정
df.drop(["Column_Name", "Column_Name", ...], axis=1)
```

- 이외에도 다양한 데이터 관련 메소드 활용 가능

<br>

#### vs. Numpy

![numpy](images/numpy.png)

- **Numpy**
  - 다차원 배열인 `ndarray` 클래스. 배열의 모든 원소가 동일한 데이터 타입이어야 함
  - 난수 생성 가능
  - 연산 가능
- **Pandas**
  - `pandas.데이터.values = numpy` 구조
  - 각 열의 타입이 달라도 된다.
  - **Numpy**의 기능을 모두 포함함
  - But, **2차원 데이터만 활용 가능**

<br>

***

#### 참고 자료

- https://3months.tistory.com/292
- https://0ver-grow.tistory.com/1051
- https://data-make.tistory.com/125