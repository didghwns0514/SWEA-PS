# 해설

1. [해설]()

# 문제 링크

[링크](https://school.programmers.co.kr/learn/courses/30/lessons/59408)

## 배울점

> 1.

## 내코드

```sql
-- 코드를 입력하세요
show table status;
select * from animal_ins;

select count(name) as 'count' from (
    select name from animal_ins
    where name is not null
    group by name
) as F;

```

## 정답코드

### 1 방법

```sql
-- 코드를 입력하세요
SELECT COUNT(DISTINCT NAME) FROM ANIMAL_INS
```

### 2 방법

```sql
-- 코드를 입력하세요
select count(distinct name)
from animal_ins
where name is not null
```

---
