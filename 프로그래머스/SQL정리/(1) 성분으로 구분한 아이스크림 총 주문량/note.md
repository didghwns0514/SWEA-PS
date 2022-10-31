# 해설
1. [해설](https://velog.io/@hrlrh/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%84%B1%EB%B6%84%EC%9C%BC%EB%A1%9C-%EA%B5%AC%EB%B6%84%ED%95%9C-%EC%95%84%EC%9D%B4%EC%8A%A4%ED%81%AC%EB%A6%BC-%EC%B4%9D-%EC%A3%BC%EB%AC%B8%EB%9F%89)

## 배울점

> 1. SHOW TABLE STATUS;
> 2. Join 에서 굳이 명시 안해주어도, select만 가지고도 되는 듯? join 없이
> 3. GROUP BY, ORDER  BY, SUM() 함수 확인

## 내코드

```sql

```

## 정답코드

```sql
-- 코드를 입력하세요
SHOW TABLE STATUS;

SELECT A.INGREDIENT_TYPE, SUM(B.TOTAL_ORDER) AS TOTAL_ORDER
    FROM 
        ICECREAM_INFO as A, 
        FIRST_HALF as B
    WHERE 
        A.FLAVOR = B.FLAVOR
     GROUP BY 
        A.INGREDIENT_TYPE
    ORDER BY 
        B.TOTAL_ORDER ASC
```
