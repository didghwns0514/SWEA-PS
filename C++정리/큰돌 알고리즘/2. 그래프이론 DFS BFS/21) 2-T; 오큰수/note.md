# 2-T

- [문제링크](https://www.acmicpc.net/problem/17298)

## 알면 좋은점

> 1. index pair 하면 stack 생각해보자 -> 나는 메모이제이션 써야할거같고, iter나올 때 stack 필이 옴
> 2. 괄호 문제 등등...
> 3. https://cocoon1787.tistory.com/347 참조!

<br>

## 코드

- 해설

  ```c++
  #include <bits/stdc++.h>
  using namespace std;
  int n, a[1000004], ret[1000004];
  stack<int> s;
  int main(){
    cin >> n;
    memset(ret, -1, sizeof(ret));
    for(int i = 0; i < n; i++){
      cin >> a[i];
      while(s.size() && a[s.top()] < a[i]){
        ret[s.top()] = a[i]; s.pop();
      }
      s.push(i);
    }
    for(int i = 0; i < n; i++) cout << ret[i] << " ";
  }

  ```

- 내코드

  ```c++

  ```
