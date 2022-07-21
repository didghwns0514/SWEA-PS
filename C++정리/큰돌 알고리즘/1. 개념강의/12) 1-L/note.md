# 1-B

- [문제링크](https://www.acmicpc.net/problem/1940)

## 알면 좋은점

> 1. Sizeof 함수로 array 사이즈 구할 수 있음

<br>

## 코드

- 해설

  ```c++
    #include<bits/stdc++.h>
    using namespace std;
    int n, m, a[150001], cnt;
    int main() {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        cin >> n >> m;
        for(int i = 0; i < n; i++) cin >> a[i];
        sort(a, a + n);
        if(m > 200000) cout << 0 << "\n";
        else{
            for(int i = 0; i < n; i++){
                for(int j = i + 1; j < n; j++){
                    if(a[i] + a[j] == m)cnt++;
                }
            }
            cout << cnt << "\n";
        }
    }
  ```

- 내코드

  ```c++
    #include <bits/stdc++.h>
    #include <string>
    #include <algorithm>

    using namespace std;

    //
    bool isInputPresent = true;
    int N;
    int M;
    int answer;
    int _data[15001];

    int getInput(){

        if(isInputPresent) freopen("input.txt", "r", stdin);

        cin >> N;
        cin >> M;

        for(int j=1; j <= N; j++) cin >> _data[j];

        return 0;
    }

    int main() {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL); cout.tie(NULL);

        // input
        getInput();
        int totSize = sizeof(_data);

        sort(_data, _data + 15001);


        bool isIterationNeeded = true;
        for(int i=1; i < 15001-1; i++){
            for(int j=i+1; j < 15001; j++){
                if(_data[i] > M/2) {
                    break;
                    isIterationNeeded = false;
                }
                if(_data[i] + _data[j] == M) {
                    // cout << "_data[i] : " << _data[i] << "\n";
                    // cout << "_data[j] : " << _data[j] << "\n";
                    answer += 1;}

            }

            if(!isIterationNeeded) break;
        }

        cout << answer << "\n";

        return 0;
    }
  ```
