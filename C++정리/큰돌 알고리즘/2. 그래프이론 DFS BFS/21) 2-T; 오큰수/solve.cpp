#include <bits/stdc++.h>
#include <iostream>


using namespace std;

//
bool isInputPresent = true;
int _data[1000000];
int filtered[1000000];
int N;

int main() {

    ios_base::sync_with_stdio(false);
    cout.tie(NULL); cin.tie(NULL);

    if(isInputPresent) freopen("input.txt", "r", stdin);

    cin >> N;

    if( N == 1) cout << -1;
    else{

        for(int i=0; i < N; i++){
            cin >> _data[i];
        }

        //
        // for(int i=0; i < N; i++){
        //     cout << _data[i] << endl;
        // }
        // cout << "";

        int left_int = 0;
        int left_index = 0;
        for(int i=0; i < N; i++){
            
            // if( left_int > _data[i] && left_index > i) cout << left_int << " ";
            // else{

                for(int k=i+1; k < N; k++){
                    if(_data[k] > _data[i] && k > i){
                        // cout << "data[k] : " << _data[k] << " data[i] : " << _data[i] << endl;
                        left_int=_data[k]; 
                        left_index=k; 
                        break;
                    }
                }
                if(left_index > i && left_int > _data[i]) cout << left_int << " ";
                else cout << -1 << " ";
            // }
        }   
        
    }

    return 0;
}