#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <queue> 
// #include <pair>

using namespace std;

// function
void getInput();
void solution();
auto makeCopyMap(auto _map);
void bfsSolution(auto _map);
void bfs(auto _map, int y, int x);

// variables
bool isInputPresent = true;
int N, M;
int originalMap[8][8];
int MAX_VALUE = 0;

auto makeCopyMap(auto _map){
    int tmpMap[8][8] = {0};
    for(int i=0; i < N; i ++){
        for(int j=0; j < M; j++){
            tmpMap[i][j] = _map[i][j];
        }
    }
    return tmpMap;
}

void getInput(){

    if(isInputPresent) freopen("input.txt", "r", stdin);

    cin >> N >> M;

    for(int n=0; n < N; n++){
        for(int m=0; m < M; m++){

            cin >> originalMap[n][m];
        }
    }
}

void solution(auto _map, int _cnt){
    if(_cnt == 3) bfsSolution(_map);
    else{
        for(int n=0; n < N; n++){
            for(int m=0; m < M; m++){
                int tmpMap[8][8] = makeCopyMap(_map);
                tmpMap[n][m] = 1;
                solution(tmpMap, _cnt + 1); 
            }
        }
    }

}

void bfsSolution(auto _map){
    for(int n=0; n < N; n++){
        for(int m=0; m < M; m++){

        }
    }
}

void bfs(auto _map, int y, int x){
    vector <pair<int, int> > visited;
    queue <pair<int, int>> _q;

    _q.push({y, x});

    while(_q.size()){
        int cy = 0; int cx = 0;
        tie(cy, cx) = _q.front();
        _q.pop();

        if(visited.find({cy, cx}) != visited.end()){
            break;
        }
    }

}

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    getInput();
    solution(originalMap, 0);

    return 0;
}