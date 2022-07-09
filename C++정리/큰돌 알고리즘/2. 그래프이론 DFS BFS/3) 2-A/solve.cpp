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


