# 대표적인 데이터 구조 : 큐(Queue)
## 1. 큐 구조
- 줄을 서는 행위와 유사
- 가장 먼저 넣은 데이터를 가장 먼저 꺼낼 수 있는 구조
    - 음식점에서 가장 먼저 줄을 선 사람이 제일 먼저 음식점에 입장하는 것과 동일
    - FIFO(First In First Out) 또는 LILO(Last-In, Last-Out) 방식으로 스택과 꺼내는 순서가 반대

## 2. 알아둘 용어
- enqueue
    - 큐에 데이터를 넣는 기능
- dequeue
    - 큐에서 데이터를 꺼내는 기능
    
## 3. 파이썬 queue 라이브러리 활용해서 큐 자료구조 사용하기
- queue 라이브러리에는 다양한 큐 구조로 Queue(), LifoQueue(), PriorityQueue() 제공
- 프로그램을 작성할 때 프로그램에 따라 적합한 자료구조를 사용
    - Queue() : 가장 일반적인 큐 자료구조
    - LifoQueue() : 나중에 입력된 데이터가 먼저 출력되는 구조(스택 구조라고 보면 됨)
    - PriorityQueue() : 데이터마다 우선순위를 넣어서, 우선순위가 높은 순으로 데이터 출력
> 일반적인 큐 외에 다양한 정책이 적용된 큐들이 있음

### 3.1 Queue() 로 큐 만들기 (가장 일반적인 큐, FIFO(First-In First-out))
### 3.2 LifoQueue() 로 큐 만들기 (LILO(Last-In Last-out))
### 3.3 PriorityQueue() 로 큐 만들기

## 참고 : 어디에 큐가 많이 쓰일까?
- 멀티 태스킹을 위한 프로세스 스케쥴링 방식을 구현하기 위해 많이 사용됨
> 큐의 경우에는 장단점 보다는 (특별히 언급되는 장단점이 없음), 큐의 활용 예로 프로세스 스케쥴링 방식을 함께 이해해두는 것이 좋음
