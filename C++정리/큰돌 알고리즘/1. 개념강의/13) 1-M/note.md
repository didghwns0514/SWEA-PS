# 1-B

- [문제링크](https://www.acmicpc.net/problem/3986)

## 알면 좋은점

> 1. Stack으로 핵결 -> memoization 처럼 해결하는 것!, 아파트 키재기 문재랑 비슷
>    - 다음을 include 할 것 : #include <stack>
> 2. Stack 설명된 블로그 : [링크](https://twpower.github.io/75-how-to-use-stack-in-cpp)

<br>

## 코드

- 해설

  ```c++
    #include<bits/stdc++.h>
    using namespace std;
    int n, ret;
    string s;
    int main() {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        cin >> n;
        for(int i = 0; i < n; i++){
            cin >> s;
            stack<char> stk;
            for(char a : s){
                if(stk.size() && stk.top() == a)stk.pop();
                else stk.push(a);
            }
            if(stk.size() == 0)ret++;
        }
        cout << ret << "\n";
    }
  ```

- 내코드

  ```c++

  ```
