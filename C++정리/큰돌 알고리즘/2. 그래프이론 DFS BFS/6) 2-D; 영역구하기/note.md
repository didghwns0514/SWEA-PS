# 2-D

- [문제링크](https://www.acmicpc.net/problem/2583)

## 알면 좋은점

> 1. cstdio ::
> 2. list, vector :: push_back -> list는 sort 메서드, 벡터는 array와 마찬가지로 sort 함수 사용

<br>

## 코드

- 해설

  ```c++
    #include <cstdio>
    #include <string>
    #include <iostream>
    #include <vector>
    #include <algorithm>
    #include <string>
    #include <stack>
    using namespace std;
    int _map[104][104], m, n, k, x1, x2, y1, y2;
    const int dy[4] = {-1, 0, 1, 0};
    const int dx[4] = {0, 1, 0, -1};
    vector<int> ret;
    int dfs(int y, int x){
        _map[y][x] = 1;
        int _ret = 1;
        for(int i = 0; i < 4; i++){
            int ny = y + dy[i];
            int nx = x + dx[i];
            if(ny < 0 || ny >= m || nx < 0 || nx >= n || _map[ny][nx] == 1) continue;
            _ret += dfs(ny, nx);
        }
        return _ret;
    }
    int main() {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        cout.tie(NULL);
        cin >> m >> n >> k;
        for(int i = 0; i < k; i++){
            cin >> x1 >> y1 >> x2 >> y2;
            for(int x = x1; x < x2; x++){
                for(int y = y1; y < y2; y++){
                    _map[y][x] = 1;
                }
            }
        }
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(_map[i][j] != 1) {
                    ret.push_back(dfs(i, j));
                }
            }
        }
        sort(ret.begin(), ret.end());
        cout << ret.size() << "\n";
        for(int _ret : ret) cout << _ret << "\n";
        return 0;
    }
  ```

- 내코드

  ```c++
    #include <bits/stdc++.h>
    #include <iostream>
    #include <queue>
    #include <set>
    #include <list>

    using namespace std; // 항상 최상단

    //
    bool isInputPresent = true;
    int N, M, K;
    int cy, cx, ny, nx;
    int _map[100][100], visited[100][100];
    int const dx[4] = {1, 0, -1, 0};
    int const dy[4] = {0, 1, 0, -1};
    int ans[10000];


    void getInput();
    int BFS(int y, int x);

    void getInput(){
        if(isInputPresent) freopen("input.txt", "r", stdin);

        cin >> M >> N >> K;

        for(int j=0; j < K; j++){
            int l_x = 0;
            int l_y = 0;
            int r_x = 0;
            int r_y = 0;
            cin >> l_x >> l_y >> r_x >> r_y;
            // cout << "l_x : " << l_x << " l_y : " << l_y << " r_x : " << r_x << " r_y : " << r_y << "\n";

            l_x = l_x;
            l_y = (M - l_y) - 1;
            r_x = r_x - 1;
            r_y = (M - r_y);

            // cout << "l_x : " << l_x << " l_y : " << l_y << " r_x : " << r_x << " r_y : " << r_y << "\n";
            for(int i1=r_y; i1 <= l_y; i1++ ){
                for(int i2=l_x; i2 <= r_x; i2++){

                    _map[i1][i2] = 1;
                }

            }
        }

        // for(int i1=0; i1 < M; i1 ++){
        //     for(int i2=0; i2 < N; i2 ++){
        //         cout << _map[i1][i2] << " ";
        //     }
        //     cout << "\n";
        // }

    }

    int BFS(int y, int x){
        queue< pair<int, int> > _q;
        int counts = 0;

        if( visited[y][x] != 0) return 0;
        if( _map[y][x] != 0 ) return 0;

        _q.push({y, x});

        while(_q.size()){
            tie(cy, cx) = _q.front();
            _q.pop();
            if(visited[cy][cx] ==0 && _map[cy][cx] == 0){counts += 1;}

            visited[cy][cx] = 1;

            for(int k=0; k < 4; k++){
                ny = cy + dy[k];
                nx = cx + dx[k];
                if(
                    0 <= ny && ny < M && 0 <= nx && nx < N &&
                    visited[ny][nx] == 0 && _map[ny][nx] == 0
                ){
                    _q.push({ny, nx});
                }
            }
        }

        return counts;

    }

    int main(){
        ios_base::sync_with_stdio(false);
        cin.tie(NULL); cout.tie(NULL);

        getInput();

        // cout << "Ph 1" << "\n";

        for(int i1=0; i1 < M; i1++){
            for(int i2=0; i2 < N; i2++){
                if(_map[i1][i2] == 0 && visited[i1][i2] == 0){
                    // cout << "For Loop !" <<  "\n";
                    int counts = BFS(i1, i2);
                    if(counts) {
                            // cout << "BFS ran" <<  "\n";
                            // _list.push_back(counts);
                            ans[counts] += 1;
                        }
                }

            }
        }

        // cout << "Ph 2" << "\n";


        int realCount = 0;
        for(auto k: ans){
            if( k > 0) realCount += 1;
        }

        cout << realCount << "\n";
        for(int k=1; k < 10000; k++){
            if(ans[k] > 0) cout << k << " ";
        }

        return 0;
    }
  ```
