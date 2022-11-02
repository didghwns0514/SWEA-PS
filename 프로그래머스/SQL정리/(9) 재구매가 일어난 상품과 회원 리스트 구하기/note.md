# 해설

1. [해설]()

# 문제 링크

[링크](https://school.programmers.co.kr/learn/courses/30/lessons/131536)

## 배울점

> 1. WHERE 조건절과 구분되는 -> 테이블 생성 이후 Having 조건절
>    [챀고 링크](https://wakestand.tistory.com/522)

> 2. GROUP BY?
>    [참고 링크](https://extbrain.tistory.com/56)
> 그룹 by를 두개 다 해야될 수도 있음....

> 3. SELECT distinct
> 중복값 제거하게 됨!

```sql
-- 코드를 입력하세요
show table status;
select * from online_sale;

select distinct user_id, product_id from online_sale
    group by product_id having count(user_id) >= 2
    order by user_id asc, product_id desc;
```

## 정답코드

### 1 방법

```sql
-- 코드를 입력하세요
show table status;
select * from online_sale;

select distinct user_id, product_id from online_sale
    group by user_id, product_id having count(user_id) >= 2
    order by user_id asc, product_id desc;
```
> 동일한 group by를 두 컬럼 모두에 적용... why?
> 

---
