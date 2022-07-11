#include <bits/stdc++.h>
#include <vector>

using namespace std;

//
int totalMoves;
int isInputPresent = true;
int N, M, J,  r;
int l = 1;
vector<int> _vec;

void getInput();
void solve();

void getInput() {

    if(isInputPresent) freopen("input.txt", "r", stdin);

    cin >> N >> M; 
    cin >> J;

    for(int j=0; j < J; j++){
        int tmp = 0; cin >> tmp;
        _vec.push_back(tmp);
    }
}

void solve(){
    for(auto i : _vec){
        // cout << "---------" << "\n";
        // cout << " i : " << i << "\n";
        r = l + M - 1;
        if(l <= i && i <= r) {
            
            // cout << "Not move!" << "\n";
            continue;
            }
        else{
            int diff = 0;
            if(r < i){
                diff = i - (r);
                l += diff;
                totalMoves += diff;
            }
            else if(l > i) {
                diff = l - i;
                l = i;
                totalMoves += diff;
            }
            // cout << "Diff : " << diff << "\n";
            // cout << "currNode : " << currNode << "\n";
            // cout << "totalMoves : " << totalMoves << "\n";
        }

    }
}

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    getInput();

    solve();

    cout << totalMoves;

    return 0;

}