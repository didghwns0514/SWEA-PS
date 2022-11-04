# 해설

1. [해설]()

# 문제 링크

[링크](https://school.programmers.co.kr/learn/courses/30/lessons/59409)

## 배울점

> 1.

## 내코드

```sql
-- 코드를 입력하세요
show table status;
select * from animal_ins;

select animal_id, name,
(
    case
    when sex_upon_intake like '%Neutered%' then 'O'
    when sex_upon_intake like '%Spayed%' then 'O'
    else 'X'
    end
) as 중성화
from animal_ins;
```

## 정답코드

### 1 방법

```sql
-- 코드를 입력하세요

```

---
