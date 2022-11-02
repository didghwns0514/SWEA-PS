# 해설

1. [해설]()

# 문제 링크

[링크](https://school.programmers.co.kr/learn/courses/30/lessons/131529)

## 배울점

> 1. string_split 함수! => 프로그래머스에서는 안써짐....
>    [참조 링크](https://tragramming.tistory.com/91)

> 2. LEFT / RIGHT 함수 : 엑셀이랑 동일하네... z  
>    [참조 링크](https://velog.io/@hrlrh/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC-%EB%B3%84-%EC%83%81%ED%92%88-%EA%B0%9C%EC%88%98-%EA%B5%AC%ED%95%98%EA%B8%B0)

## 내코드

```sql
-- 코드를 입력하세요
show table status;
select * from product;

select left(product_code, 2) as category,
       count(product_id) as products from product

       group by category
       order by category asc;
```

## 정답코드

### 1 방법

```sql
-- 코드를 입력하세요


```

---
