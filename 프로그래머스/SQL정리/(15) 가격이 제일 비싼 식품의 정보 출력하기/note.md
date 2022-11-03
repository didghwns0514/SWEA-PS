# 해설

1. [해설]()

# 문제 링크

[링크](https://school.programmers.co.kr/learn/courses/30/lessons/131115)

## 배울점

> 1. 아마도 where 절로 비교되기 위해서는 같은 table 형식으로 비교가 되어야 하는듯...

## 내코드

```sql
-- 코드를 입력하세요
show table status;
select * from food_product;


select product_id, product_name, product_cd, category, price from food_product
    group by product_id
    having price = max(price);
```

## 정답코드

### 1 방법

```sql
-- 코드를 입력하세요
select *
from food_product
where price = (SELECT max(price) as price from food_product);

```

---
