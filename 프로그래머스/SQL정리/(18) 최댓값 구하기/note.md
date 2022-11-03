# 해설

1. [해설]()

# 문제 링크

[링크](https://school.programmers.co.kr/learn/courses/30/lessons/59415)

## 배울점

> 1.

## 내코드

```sql
-- 코드를 입력하세요
-- 코드를 입력하세요
show table status;
select * from animal_ins;

select datetime from animal_ins
    order by datetime desc limit 1;
```

## 정답코드

### 1 방법

```sql
-- 코드를 입력하세요

-- 코드를 입력하세요
SELECT MAX(DATETIME) from ANIMAL_INS order by DATETIME;

```

---
