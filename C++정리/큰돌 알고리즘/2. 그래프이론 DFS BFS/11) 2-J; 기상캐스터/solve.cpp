#include <bits/stdc++.h>
#include <iostream>

using namespace std;

void getInput();
void solution();

//
int _map[100][100], cloud[100][100];
bool isInputPresent = true;
int H, W;

void getInput(){
    if(isInputPresent) freopen("input.txt", "r", stdin);

    char tmpCh;

    cin >> H >> W;

    for(int i1=0; i1 < H; i1++){
        for(int i2=0; i2 < W; i2++){
            cin >> tmpCh;
            if(tmpCh == 'c') _map[i1][i2] = 1;
        }
    }
    
    // for(int i1=0; i1 < H; i1++){
    //     for(int i2=0; i2 < W; i2++){
    //         cout << "_map[i1][i2] : " << _map[i1][i2] << "\n";
    //     }
    // }

    fill(&cloud[0][0], &cloud[99][99], -1);

    return;
}


void solution(){

    // W 만큼의 구름의 이동
    for(int _iniNum=0; _iniNum < W+1; _iniNum ++){
        
        // 구름 기록
        for(int i1=0; i1 < H; i1++){
            for(int i2=0; i2 < W; i2++){

                if(_map[i1][i2]==1 && cloud[i1][i2] == -1 ) cloud[i1][i2] = _iniNum;  

            }

        }

        //구름 이동
        for(int i1=0; i1 < H; i1++){
            for(int i2=W-1; i2 >= 0; i2--){
                if(i2 == 0) _map[i1][i2] = 0; // 구름 없어지는 부분
                else{
                    _map[i1][i2] = _map[i1][i2-1];
                }

            }
        }
    }

    // 구름 출력
    for(int i1=0; i1 < H; i1++){
        for(int i2=0; i2 < W; i2++){
            cout << cloud[i1][i2] << " ";
        }
        cout << "\n";

    }
}    

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    getInput();
    solution();

    return 0;
}