# 7월 26일

## 🚩 기능개발

[![image-20210726202513934](README.assets/image-20210726202513934.png)](https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3)



#### ✍ 풀이

- `progresses` 변수에 작업을 완료할 수 있는 날짜를 다시 담아 둔다.
- `_max`를 설정해서 그것보다 크다면 배포하는 날을 다음 날로 바꿔준다.

```python
def solution(progresses, speeds):
    answer = []
    
    for i in range(len(progresses)):
        
        n = 100 - progresses[i] # 남은 일 %
        
        if n % speeds[i]: # 나머지가 있으면 하루 추가
            progresses[i] = n // speeds[i] + 1
        else:
            progresses[i] = n // speeds[i]
            
    _max = progresses[0] # 최댓값 설정
    cnt = 0
    
    
    for i in range(len(progresses)):
        
        if _max >= progresses[i]: # 최댓값보다 작으면 cnt 추가 (앞에 일이 끝나야 배포할 수 있음)
            cnt += 1
                
        else:
            answer.append(cnt)
            cnt = 1
            _max = progresses[i]
            
    answer.append(cnt)
    
    return answer
```



## 🚩 위장

[![image-20210726215218944](README.assets/image-20210726215218944.png)](https://programmers.co.kr/learn/courses/30/lessons/42578)



#### ✍ 풀이

- 딕셔너리로 해당 의상의 개수를 담아 준다.

- 의상 종류에 따라 조합을 이용해서 해결 하고자 했다.



```python
def solution(clothes):
    answer = 0
    
    spy = {}

    
    for res in clothes:
        
        if res[1] not in spy.keys():
            spy[res[1]] = 1
        else:
            spy[res[1]] += 1 

    oodt = list(spy.values())
    
    
    for i in range(1, 1 << len(oodt)):
        cnt = 1
        for j in range(len(oodt)):
            if i & (1 << j):
                cnt *= oodt[j]
                
        answer += cnt

        
    return answer

```

