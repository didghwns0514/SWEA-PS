#include <bits/stdc++.h>
#include <string>
#include <regex>

using namespace std;

// function
void getInput();
void solution();

// global
bool isInputPresent = true;
int N;


void getInput(){

    if(isInputPresent) freopen("input.txt", "r", stdin);

    cin >> N;
}

void solution(){

    string tmpString = "";
    for(int i=0; i < N; i++){
        // cout << "----------" << endl;
        cin >> tmpString;
        // cout << "tmpString :: " << tmpString << endl;
        int sizeLimit = tmpString.size() / 2;
        
        for(int k=0; k < sizeLimit; k++){
            
            if(tmpString.find("()") != string::npos){
                int _index = tmpString.find("()");
                // cout << "-  _index :: " << _index << endl;
                // cout << "-  _index+2 :: " << _index+1 << endl;
                if(_index != 0){
                    tmpString.erase(_index, 2);
                    // cout << "-  tmpString :: " << tmpString << endl;
                }
                else{
                    tmpString.replace(_index, _index + 2, "");
                    // cout << "-  tmpString :: " << tmpString << endl;
                }

            }
        }

        if(tmpString == "") cout << "YES";
        else cout << "NO";
        cout << "\n";
    }



}

int main() {

    ios_base::sync_with_stdio(false);
    cout.tie(NULL); cin.tie(NULL);
    
    getInput();
    solution();

    return 0;

}
