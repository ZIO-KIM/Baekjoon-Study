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
### 문자열에서 특정 문자 제거하기  
> 만약 "google" 에서 "oo" 를 제거하고 싶다면  
```
str1 = 'google'
str1 = str1.replace("oo", "")
str1
``` 
```
>>> ggle
```
> 만약 "google" 에서 "oo" 를 "kk" 로 replace 하고 싶다면  
```
str1 = 'google'
str1 = str1.replace("oo", "kk")
str1
``` 
```
>>> gkkgle
```   
### 리스트 원형을 복사하고 싶을 때  
> 리스트1 = 리스트2를 하면, 리스트2가 변화할 때 리스트1도 같이 변화한다.   
> 따라서, 다음 copy function을 써야 함  
``` 
tmp_lst = lst.copy() 
```  
### 리스트 특정 위치에 원소를 삽입하고 싶을 때  
```
lst.insert(3, "c")  
```
### 리스트 내의 특정 문자 갯수를 세고 싶을 때  
```  
lst.count("c")  
```
### 리스트에서 중복되는 원소 제거  
> 순서는 유지할 수 없다  
``` 
lst = ['h', 'a', 'p', 'p', 'y']
lst2 = set(lst)
print(lst2) 
```
```
['a', 'h', 'p', 'y']
```
