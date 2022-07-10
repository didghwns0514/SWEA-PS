# 2-C

- [문제링크](https://www.acmicpc.net/problem/2468)

## 알면 좋은점

> 1. 초기화 fill :: fill(&visited[0][0], &visited[99][99], 0);

<br>

## 코드

- 해설

  ```c++
    #include<bits/stdc++.h>
    using namespace std;
    int b[101][101], e[101][101], visited[101][101], n, temp, ret = 1;
    int dy[4] = {-1, 0, 1, 0};
    int dx[4] = {0, 1, 0, -1};
    void dfs(int y, int x){
        visited[y][x] = 1;
        for(int i = 0; i < 4; i++){
            int ny = y + dy[i];
            int nx = x + dx[i];
            if(ny < 0 || nx < 0 || ny >= n || nx >= n) continue;
            if(!visited[ny][nx] && e[ny][nx] == 0) dfs(ny, nx);
        }
        return;
    }
    int main(){
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        cout.tie(NULL);
        cin >> n;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                cin >> b[i][j];
            }
        }
        for(int d = 1; d < 101; d++){
            fill(&visited[0][0], &visited[0][0] + 101 * 101, 0);
            temp = 0;
            for(int i = 0; i < n; i++){
                for(int j = 0; j < n; j++){
                    if(e[i][j] == 1) continue;
                    if(b[i][j] <= d) e[i][j] = 1;
                }
            }
            for(int i = 0; i < n; i++){
                for(int j = 0; j < n; j++){
                    if(e[i][j] == 0 && !visited[i][j]) {
                        dfs(i, j);
                        temp++;
                    }
                }
            }
            ret = max(ret, temp);
        }
        cout << ret << '\n';
        return 0;
    }


  ```

- 내코드

  ```c++
    #include <bits/stdc++.h>
    #include <queue>
    #include <iostream>
    #include <utility>

    // global variables
    int N, cy, cx, ny, nx;
    int ans;
    int _count;
    int const dx[4] = {1, 0, -1, 0};
    int const dy[4] = {0, 1, 0, -1};
    int _map[100][100], visited[100][100];
    bool isInputPresent = true;

    using namespace std;
    void getInput();
    void BFS(int y, int x, int height);
    void initData();

    void BFS(int y, int x, int height){

        queue< pair<int, int >> _q;
        _q.push({y, x});

        if( _map[y][x] <= height || visited[y][x]) return;

        while(_q.size()){
            tie(cy, cx) = _q.front();
            _q.pop();

            if(visited[cy][cx]) continue;
            visited[cy][cx] = 1;

            for(int k=0; k < 4; k++){
                ny = cy + dy[k];
                nx = cx + dx[k];
                if(
                    0<= ny && ny < N && 0 <= nx && nx < N && _map[ny][nx] > height && visited[ny][nx] == 0
                ){
                    _q.push({ny, nx});
                }
            }

        }

        _count += 1;
    }

    void getInput(){

        if(isInputPresent) {
            freopen("input.txt", "r", stdin);
        }

        cin >> N;
        for(int i1=0; i1 < N; i1++){
            for(int i2=0; i2 < N; i2++){
                cin >> _map[i1][i2];
            }
        }


    }

    void initData(){
        _count = 0;
        fill(&visited[0][0], &visited[99][99], 0);
    }

    int main(){

        ios_base::sync_with_stdio(false);
        cout.tie(NULL); cin.tie(NULL);

        getInput();

        for(int tryNum = 0; tryNum <= 100; tryNum ++){
            initData();
            for(int i1=0; i1 < N; i1++){
                for(int i2=0; i2 < N; i2++){
                    BFS(i1, i2, tryNum);

                }
            }

            if(_count >= ans) ans = _count;
        }

        cout << ans << "\n";

        return 0;
    }

  ```
