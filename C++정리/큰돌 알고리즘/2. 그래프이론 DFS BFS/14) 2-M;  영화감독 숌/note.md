# 2-E

- [문제링크](https://www.acmicpc.net/problem/2828)

## 알면 좋은점

>

<br>

## 코드

- 해설

  ```c++
  #include<bits/stdc++.h>
  using namespace std;
  int n;
  int main() {
      cin >> n;
      int i = 666;
      for(;; i++){
          if(to_string(i).find("666") != string::npos)n--;
          if(n == 0)break;
      }
      cout << i << "\n";
  }
  ```

- 내코드

  ```c++

  ```
