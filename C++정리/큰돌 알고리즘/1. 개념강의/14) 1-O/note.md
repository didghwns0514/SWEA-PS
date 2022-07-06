# 1-B

- [문제링크](https://www.acmicpc.net/problem/4375)

## 알면 좋은점

>

<br>

## 코드

- 해설

  ```c++
  #include<bits/stdc++.h>
  using namespace std;
  typedef long long ll;
  int n;
  int main(){
    while(scanf("%d", &n) != EOF){
      int cnt = 1, ret = 1;
      while(true){
        if(cnt % n == 0){
          printf("%d\n", ret);
          break;
        }else{
          cnt = (cnt * 10) + 1;
          cnt %= n;
          ret++;
        }
      }
    }
    return 0;
  }
  ```

- 내코드

  ```c++

  ```
