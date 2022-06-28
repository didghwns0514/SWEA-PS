# 1-B

- [문제링크](https://www.acmicpc.net/problem/2559)

## 알면 좋은점

> 1. 부분합 문제 : 어느 시점에 특정 합을 물어본다면, 매번 더하게되면 최소 n^2 시간복잡도
>    전체 값 + 1 만큼 인덱스 설정하여, 헷갈리지 않고 수월하게 풀어보도록 하자!
> 2. n회 순회로 문제를 풀도록 해보자!

<br>

## 코드

- 해설

  ```c++
    #include<bits/stdc++.h>
    using namespace std;
    typedef long long ll;
    int n, k, temp, psum[100001], ret = -1000000;
    int main(){
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);cout.tie(NULL);
        cin >> n >> k;
        for(int i = 1; i <= n; i++){
            cin >> temp; psum[i] = psum[i - 1] + temp;
        }
        for(int i = k; i <= n; i++){
            ret = max(ret, psum[i] - psum[i - k]);
        }
        cout << ret << "\n";
        return 0;
    }

  ```

- 내코드

  ```c++


  ```
