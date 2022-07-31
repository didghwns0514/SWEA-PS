# 2-R

- [문제링크](https://www.acmicpc.net/problem/1068)

## 알면 좋은점

> 1. vector를 dfs용 map 기록으로 쓰는건 좋은 생각! -> adj array 안에 가변 vector
> 2. 제거 값이 root인 경우가 반례, 이런 반례를 잘 생각하고 추가를 해주어야 test케이스 통과

<br>

## 코드

- 해설

  ```c++
    #include<bits/stdc++.h>
    using namespace std;
    int n, r, temp, root;
    vector<int> adj[54]; // adj

    int dfs(int here){
        int ret = 0;
        int child = 0;
        for(int there : adj[here]){
            if(there == r) continue;
            ret += dfs(there);
            child++;
        }
        if(child == 0) return 1;
        return ret;
    }

    int main(){
        ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
        cin >> n;
        for(int i = 0; i < n; i++){
            cin >> temp;
            if(temp == -1)root = i;
            else adj[temp].push_back(i);
        }
        cin >> r;
        if(r == root){
            cout << 0 << "\n";return 0;
        }
        cout << dfs(root) << "\n";
        return 0;
    }

  ```

- 내코드

  ```c++

  ```
