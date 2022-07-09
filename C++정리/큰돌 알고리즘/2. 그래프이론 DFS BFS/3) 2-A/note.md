# 1-B

- [문제링크](https://www.acmicpc.net/problem/2178)

## 알면 좋은점

> 1. scanf("%1d", &a[i][j]); :: 하나씩 정수 입력받을 때 매우 유용
> 2. scanf("%d %d", &n, &m); :: 각각 정수 입력받기
>    참조 : [링크](https://yoonwould.tistory.com/18)
> 3. pair, tuple 등으로 2, 3자리 값을 묶을 수 있음

<br>

## 코드

- 해설

  ```c++
  #include<bits/stdc++.h>
  using namespace std;
  const int max_n = 104;
  int dy[4] = {-1, 0, 1, 0};
  int dx[4] = {0, 1, 0, -1};
  int n, m, a[max_n][max_n], visited[max_n][max_n], y, x;
  int main(){
      scanf("%d %d", &n, &m);
      for(int i = 0; i < n; i++){
          for(int j = 0; j < m; j++){
              scanf("%1d", &a[i][j]);
          }
      }
      queue<pair<int, int>> q;
      visited[0][0] = 1;
      q.push({0, 0});
      while(q.size()){
          tie(y, x) = q.front(); q.pop();
          for(int i = 0; i < 4; i++){
              int ny = y + dy[i];
              int nx = x + dx[i];
              if(ny < 0 || ny >= n || nx < 0 || nx >= m || a[ny][nx] == 0) continue;
              if(visited[ny][nx]) continue;
              visited[ny][nx] = visited[y][x] + 1;
              q.push({ny, nx});
          }
      }
      printf("%d", visited[n - 1][m - 1]);
      return 0;
  }


  ```

- 내코드

  ```c++
  #include <bits/stdc++.h>
  #include <queue>
  #include <string>
  #include <utility>
  #include <tuple>
  #include <iostream>

  //
  bool isInputPresent = true;
  int _map[100][100];
  int visited[100][100];
  int N, M, cy, cx, cc, ny, nx;
  int const dx[4] = {1, 0, -1, 0};
  int const dy[4] = {0, 1, 0, -1};


  using namespace std;
  void BFS(int y, int x);
  void buildMap();

  void buildMap(){
      for(int i = 0; i < N; i++){
          for(int j = 0; j < M; j++){
              scanf("%1d", &_map[i][j]);
          }
      }
  }


  void BFS(int y, int x){

      queue< tuple< int, int, int > > _q;
      _q.push({y, x, 1});

      while(_q.size()){
          cout << "=========" << "\n";

          tie(cy, cx, cc) = _q.front();
          cout << "cy : " << cy << " cx : " << cx << " cc : " << cc << "\n";

          _q.pop();

          if(visited[cy][cx] == 1) continue;
          visited[cy][cx] = 1;

          if(cy == N-1 && cx == M-1) {
              cout << cc; return;
          }

          for(int k=0; k < 4; k++){
              ny = cy + dy[k];
              nx = cx + dx[k];
              cout << "ny : " << ny << " nx : " << nx << "\n";
              if (
                  (0 <= ny) && (ny < N) && (0 <= nx) && (nx < M) && (visited[ny][nx] == 0) && _map[ny][nx] == 1
              ){
                  _q.push({ny, nx, cc + 1});
              }
          }
      }

      cout << "BFS ended" << "\n";


  }

  int main() {

      ios_base::sync_with_stdio(false);
      cin.tie(NULL); cout.tie(NULL);

      if(isInputPresent) freopen("input.txt", "r", stdin);

      cin >> N >> M;

      cout << "N : " << N << " M : " << M << "\n";
      buildMap();
      BFS(0, 0);


      return 0;
  }

  ```
