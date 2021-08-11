# 배열(Array)
- 데이터를 나열하고, 각 데이터를 인덱스에 대응하도록 구성한 데이터 구조
- 파이썬에서는 리스트 타입이 배열 기능을 제공하고 있음

## 배열이 왜 필요할까?
- 같은 종류의 데이터를 효율적으로 관리하기 위해 사용
- 같은 종류의 데이터를 순차적으로 저장

## 배열의 장점과 단점
- 장점 : 빠른 접근 가능
- 단점 : 추가 / 삭제가 십지 않음, 미리 최대 길이를 지정해야 함

## 파이썬과 C언어의 배열 예제
```C
#include <stdio.h>

int main(int argc, char *argv[]) 
{
    char country[3] = "US";
    printf("%c%c\n", country[0], country[1]);
    printf("%s\n", country);
    return 0;
}
```
```python
country = 'US'
print(country)

country = country + 'A'
print(country)
```

## 파이썬과 배열
- 파이썬 리스트 활용
```python
# 1차원 배열 : 리스트로 구현시
data = [1, 2, 3, 4, 5]
```

```python
# 2차원 배열 : 리스트로 구현시
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

## 연습
### 연습1. 위 2차원 배열에서 9,8,7 순서로 출력해보기
### 연습2. dataset에서 전체 이름 안에 m이 몇 번 나왔는 지 빈도수 출력하기
