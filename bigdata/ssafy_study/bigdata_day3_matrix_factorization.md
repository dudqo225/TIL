# Bigdata | Day3_Matrix Factorization

<br>

### Matrix Factorization

- Given
  - `R` 이라는 평점 매트릭스가 주어졌을 때
- Find
  - `U`, `V` 매트릭스를 찾는다
- 접근법
  - `U` 와 `V`를 임의의 값으로 초기화
  - `R`의 값과 비교를 하면서, `U` / `V` 매트릭스의 최적값을 찾아나간다.
  - **The gradient descent method**
    - `R`과 근사한 `U x V` 를 구할 때는 `R` 자체에 평점들이 많이 비어있기 때문에,  `U`와 `V` 원소가 0으로 채워질 수 있음
    - `R` 에 들어있는 non-zero 평점을 활용하여 근사한 `U x V`를 대신 구한다.

<br>

### Matrix Factorization 코딩

- `movieRecProject/matrixFactorization/data` 디렉토리
  - 평점 행렬 R은 Compressed Sparse Row (CSR) Matrix 형태로 저장되어 있음
  - `R.pkl` 에서 `R_train.pkl` 과 `R_valid.pkl` 을 나누는 방법
    - 전체 유저 평점 행렬이 `NxM` 형태로 `R.pkl` 에 저장되어 있음. MF 알고리즘의 종료 조건을 확인하는데 사용될 validation 데이터를 `R.pkl` 에서 일부 뽑아 `R_valid.pkl` 파일로 만들고, 나머지는 `R_train.pkl` 파일로 만든다.
    - 처음에 `R_trainpkl`은 R 행렬을 그대로 복사.  `R_valid`는 zero(0)로 모든 원소를 초기화. 이후 `R_train`에서 일부 유저와 평점을 뽑아 그 평점을 `R_valid`에 기록하고, `R_train`에서는 삭제
    - **`R_train + R_valid = R`**

- `movieRecProject/matrixFactorization/result` 디렉토리
  - Matrix factorization에서 학습 데이터를 이용해서 만든 U와 V 행렬 저장
  - 코드를 구현하는 동안에는 작은 데이터로 학습 시간을 적게 하자. `tiny/` 와 `small/` 디렉토리의 데이터를 이용
    - `U.dat`
    - `V.dat`

<br>

### 3일차 과제

#### eval_rmse

```python
# 평균 제곱근 편차(Root Mean Square Deviation) 구하기
def eval_rmse(self):
    # Valid 데이터에서 0이 아닌 평점의 x좌표, y좌표 리스트 구하기
    xs, ys = self.R_valid.nonzero()
    
    # U x V를 predicted 변수에 할당
    predicted = self.U.dot(self.V.T)
    
    error = 0
    count = 0
    for x, y in zip(xs, ys):
        error += pow(self.R_valid[x, y] - predicted[x, y], 2)
        count = count + 1
    return np.sqrt(error)/count
```

 <br>

#### sgd

```python
# U, V Matrix 업데이트
def sgd(self):
    for i, j, r in self.T:
        prediction = self.get_rating(i, j)
        e = (r - prediction)
        
        # 행렬 U의 i번째 행 전체를 복사
        U_i = self.U[i, :][:]
    	
        # Update 공식 대입
        self.U[i, :] += self.alpha * (2*e * self.V[j, :] - self.beta * self.U[i, :])
        self.V[j, :] += self.alpha * (2*e * U_i - self.beta * self.V[j, :])
```

<br>

#### get_rating

```python
# 유저 i의 영화 j에 대한 예상 평점 계산 후 리턴
def get_rating(self, i, j):
    prediction = self.U[i, :].dot(self.V[j, :].T)
    return prediction
```

<br>

#### train

```python
def train(self):
    # U, V Matrix 랜덤하게 Initialize
    self.U = np.random.normal(scale=1./self.K, size=(self.num_users, self.K))
    self.V = np.random.normal(scale=1./self.K, size=(self.num_movies, self.k))
    
    # 0이 아닌 값들의 x, y 좌표와 해당값 리스트 만들기
    self.T = []
    for i, j in zip(self.R_train.nonzero()[0], self.R_train.nonzero()[1]):
        self.T.append((i, j, self.R_train[i, j]))
    
    # 경사하강법(gradient descent)을 5번까지 시행
    endure_count = 5
    count = 0
    # 큰 숫자를 할당하여 rmse 초기화 - 가장 작은 최소값을 찾아야 하기 때문
    bset_rmse = 9e7
    training_process = []
    for i in range(self.num_iterations):
        # shuffle 하여 랜덤한 순서로 진행
        np.random.shuffle(self.T)
        
        self.sgd()
        rmse = self.eval_rmse()
        
        training_process.append((i, rmse))
        print("Iteration: %d ; error = %.4f" %(i+1, rmse))
        
        # best_rmse 값 변경하고, txt 파일 저장
        if rmse < best_rmse:
            np.savetxt(self.output_path + '/U.dat', self.U)
            np.savetxt(self.output_path + '/V.dat', self.V)
            best_rmse = rmse
            print("Best matrices are saved (err: {})".format(rmse))
        else:
            count += 1
            
        # 5번 시도하고 나면 break
        if count == endure_count:
            break
            
    return training_process
```

<br>

***

### 실제 프로젝트에서 사용할 Improving Matrix Factorization

#### 기존 MF 방법

- 평점 행렬 `R`에 대해서 `NxK` 행렬 `U`와 `KxM` 행렬 `V`의 행렬 곱 `UxV`를 했을 때, 평점을 가장 잘 맞추는 행렬 `U`와 `V`를 찾아냄

<br>

#### 향상된 MF 방법

- 단순히 영화 평점만을 기반으로 예측하는 것이 아닌, **다른 정보도 활용하여 평점을 예측**한다.
- 예를 들어, 영화의 줄거리 정보로부터 **PLSI** 모델과 **주제 확률분포**를 이용, 행렬 `U` 와 `V`를 찾아낼 수 있다.
- 텍스트 문서의 주제 확률분포를 알아내는 모델은 여러가지가 있음
  - PLSI
  - LDA

