# 2-P

- [문제링크](https://www.acmicpc.net/problem/14502)

## 알면 좋은점

> 1. memset으로 visited 2d array bool값 초기화
> 2. = = = 1 등으로 한번에 여러개 변수 set 가능
> 3. typedef 사용 => 굳이 필요 없는 듯
> 4. visited가 방문 메모이제이션으로 쓰이고, \_map 데이터가 이동가능 영역 판별하는 것으로 쓰임

<br>

## 코드

- 해설

  ```c++
    #include <bits/stdc++.h>
    using namespace std;
    typedef long long lint;
    typedef pair<int, int> pi;
    int dx[4] = {1, 0, -1, 0};
    int dy[4] = {0, 1, 0, -1};

    int n, m, a[10][10];
    vector<pi> v;

    bool vis[10][10];

    void dfs(int x, int y){
        if(a[x][y] == 1 || vis[x][y]) return;
        vis[x][y] = 1;
        for(int i=0; i<4; i++){
            if(x + dx[i] < 0 || y + dy[i] < 0 || x + dx[i] >= n || y + dy[i] >= m){
                continue;
            }
            dfs(x + dx[i], y + dy[i]);
        }
    }

    int solve(){
        memset(vis, 0, sizeof(vis));
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(a[i][j] == 2) dfs(i, j);
            }
        }
        int ans = 0;
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(!vis[i][j] && a[i][j] == 0) ans++;
            }
        }
        return ans;
    }


    int main(){
        cin >> n >> m;
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                cin >> a[i][j];
                if(!a[i][j]) v.push_back(pi(i, j));
            }
        }
        assert(v.size() >= 3);
        int ans = 0;
        for(int i=0; i<v.size(); i++){
            for(int j=0; j<i; j++){
                for(int k=0; k<j; k++){
                    a[v[i].first][v[i].second] = a[v[j].first][v[j].second] = a[v[k].first][v[k].second] = 1; // 벽생성
                    ans = max(ans, solve());
                    a[v[i].first][v[i].second] = a[v[j].first][v[j].second] = a[v[k].first][v[k].second] = 0; // 벽해제
                }
            }
        }
        cout << ans;
    }


  ```

- 내코드

  ```c++

  ```
