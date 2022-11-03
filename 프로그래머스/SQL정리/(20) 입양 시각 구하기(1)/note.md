# 해설

1. [해설]()

# 문제 링크

[링크](https://school.programmers.co.kr/learn/courses/30/lessons/59412)

## 배울점

> 1. 정수 변환!!!! CAST() 함수 사용!  
>    cast( A as signed integer); 와 같이 사용

> 2. Datetime의 time 부분
>    %T 사용시 XX : XX 로 출력
>    between AA and BB 로 시간 제한 가능

## 내코드

```sql
-- 코드를 입력하세요
show table status;
select * from animal_outs;

select date_format(datetime, '%H') as hour,
count(animal_id) from animal_outs

    where cast(date_format(datetime, '%H') as signed integer) >= 9 and
     cast(date_format(datetime, '%H') as signed integer) <= 19

     group by hour
     order by hour asc;
```

## 정답코드

### 1 방법

```sql
-- 코드를 입력하세요
SELECT HOUR(DATETIME) as HOUR, count(*) as COUNT
from ANIMAL_OUTS
where date_format(DATETIME,'%T') between '09:00' and '19:59'
group by HOUR
order by HOUR ;
```

---
