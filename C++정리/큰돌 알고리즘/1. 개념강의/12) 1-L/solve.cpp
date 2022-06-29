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
            if(_data[i] > M/2) {break; isIterationNeeded = false;}
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