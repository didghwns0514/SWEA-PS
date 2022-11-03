# 해설

1. [해설]()

# 문제 링크

[링크](https://school.programmers.co.kr/learn/courses/30/lessons/131114)

## 배울점

> 1. 아마도 where 절로 비교되기 위해서는 같은 table 형식으로 비교가 되어야 하는듯...

## 내코드

```sql
-- 코드를 입력하세요
show table status;
select * from food_warehouse;

select warehouse_id, warehouse_name, address,
(
    case
    when freezer_yn is null then 'N'
    else freezer_yn
    end
) as freezer_yn
from food_warehouse
    where right(left(warehouse_name, 5),2) = '경기'

    order by warehouse_id asc;
```

## 정답코드

### 1 방법

```sql
-- 코드를 입력하세요
-- IFNULL 함수 사용
SELECT
    WAREHOUSE_ID,
    WAREHOUSE_NAME,
    ADDRESS,
    IFNULL(FREEZER_YN, "N") AS FREEZER_YN
FROM FOOD_WAREHOUSE
WHERE ADDRESS LIKE "경기도%"
ORDER BY WAREHOUSE_ID ASC;

-- IF 함수 사용
SELECT
    WAREHOUSE_ID,
    WAREHOUSE_NAME,
    ADDRESS,
    IF(FREEZER_YN IS NULL, "N", FREEZER_YN) AS FREEZER_YN
FROM FOOD_WAREHOUSE
WHERE ADDRESS LIKE "경기도%"
ORDER BY WAREHOUSE_ID ASC;

-- CASE 사용
SELECT
    WAREHOUSE_ID,
    WAREHOUSE_NAME,
    ADDRESS,
    CASE
        WHEN FREEZER_YN IS NULL THEN "N"
        ELSE FREEZER_YN
    END AS FREEZER_YN
FROM FOOD_WAREHOUSE
WHERE ADDRESS LIKE "경기도%"
ORDER BY WAREHOUSE_ID ASC;

```

---
