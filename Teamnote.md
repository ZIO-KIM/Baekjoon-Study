### 리스트를 공백과 함께 한줄로 출력  
```
for i in range (N):
    print(lst[i], end=' ')
```  
### find() 함수 (문자열에서 특정 문자를 찾고 그 위치를 반환)  
```
s = 'abcdef'
print(s.find('a'))
```
```
>>> 0
```
### 리스트 인덱스를 값에 따라 정렬하는 방법 1 (numpy 사용x)  
> 리스트가 [2, 3, 1, 4, 5] 라면, 인덱스 리스트를 [2, 0, 1, 3, 4] 로 정렬하는 법  
```
s = [2, 3, 1, 4, 5, 3]
sorted(range(len(s)), key=lambda k: s[k])
>>> [2, 0, 1, 5, 3, 4]
```
### 방법 2 (numpy 사용 가능할때)  
```
import numpy
vals = numpy.array([2,3,1,4,5])
vals
>>> array([2, 3, 1, 4, 5])
sort_index = numpy.argsort(vals)
sort_index
>>> array([2, 0, 1, 3, 4])
```
