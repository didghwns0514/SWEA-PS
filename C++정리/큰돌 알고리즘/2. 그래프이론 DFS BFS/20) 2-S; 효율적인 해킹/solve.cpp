#include <bits/stdc++.h>
#include <iostream>
#include <vector>

using namespace std;

//

//
bool isInputPresent = true;
int N, M;
vector<int> _data[10000];

int main(){

    ios_base::sync_with_stdin(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N >> M;

    int i1 = 0; int i2 = 0;
    for(int i=0; i < M; i++){
        
        cin >> i1 >> i2;
        _data[i1].push_back(i2);
    }

    return 0;
}