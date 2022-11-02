# 해설

1. [해설]()

# 문제 링크

[링크](https://school.programmers.co.kr/learn/courses/30/lessons/131530)

## 배울점

> 1. 같은 column 값 inner join 하려면 mysql 에서는 where절로 같은 것 골라야 함

```sql
-- 코드를 입력하세요
show table status;

select a.product_code, sum(b.sales_amount * a.price) as sales
from product as a, offline_sale as b
    where a.product_id = b.product_id # join 하려면 이렇게...
    group by product_code
    order by sales desc, product_code asc;
```

## 정답코드

### 1 방법

```sql
-- 코드를 입력하세요

```

---
