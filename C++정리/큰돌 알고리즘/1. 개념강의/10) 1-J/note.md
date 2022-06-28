# 1-B

- [문제링크](https://www.acmicpc.net/problem/9375)

## 알면 좋은점

> 1. map : map<string, int> \_map 등으로 선언하여 사용!

```c++
  //map 사용방법
  if (m.find(2) == m.end() )
  {
      // key 2 doesn't exist
  }
```

> 2. 대단히 수학적인 풀이; 전체 곱하고 -1 등을 좀 생각해야 떠올릴 수 있음
> 3. next_permutation, next_combination 등은 실제 조합, 순열을 돌려줌

<br>

## 코드

- 해설

  ```c++
  #include <bits/stdc++.h>
  using namespace std;
  int t, n;
  string a, b;
  int main(){
      cin >> t;
      while(t--){
          map<string, int> _map;
          cin >> n;
          for(int i = 0; i < n; i++){
              cin >> a >> b;
              _map[b]++;
          }
          long long ret = 1;
          for(auto c : _map){
              ret *= ((long long)c.second + 1);
          }
          ret--;
          cout << ret << "\n";
      }
      return 0;
  }



  ```

- 내코드

  ```c++


  ```
