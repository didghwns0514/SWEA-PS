#include <bits/stdc++.h>
#include <iostream>
#include <string>
#include <map>
// #include <pair>

using namespace std;

//
int N;
string _data[100];
map<string, string> _map;
bool isInputPresent = true;

int MIN_MAX = 47;
int SEC_MAX = 59;

int curr_min, curr_sec, team1, team2, score1, score2, data_index;

//
void getInput();
void solution();

void getInput(){

    if(isInputPresent) freopen("input.txt", "r", stdin);

    cin >> N;
    string tmpString = "";
    for(int i=0; i < N; i++){
        cout << "------------" << endl;

        // cin >> tmpString;
        string num,  restText = "";
        cin >> num >> restText;

        cout << "num : " << num << " restText : " << restText << endl;

        _data[i] = restText;
        _map[restText] = num;
    }
}

pair<int, int> converToInt(string stringTime){

    pair<int, int> _pair;
    int tmpIndex = 0;
    string _min = stringTime.substr(0, stringTime.find(":"));
    string _sec = stringTime.substr(stringTime.find(":")+1);
    
    
    if(_min[0] == '0') _min = _min.substr(1);
    cout << "   ##" << " _min : [" << _min << "] _sec : [" << _sec << "]" <<endl;

    _pair = {stoi(_min), stoi(_sec)};

    return _pair;
    
}

void solution(){

    cout << "start solution!" << endl;

    while( curr_min <= MIN_MAX && curr_sec <= SEC_MAX ) {
        // cout << "ITER!" << endl;


        if(data_index < N){

            int _min, _sec = 0;
            string tmpString = _data[data_index];
            tie(_min, _sec) = converToInt(tmpString);
            cout << "conversion done!" << endl;
            
            cout << "_min : " << _min << " _sec : " << _sec << endl;


            if(curr_min == _min && curr_sec == _sec){
                data_index += 1;

                if(_map.find(tmpString) != _map.end()){
                    string tmpTeam = _map[tmpString];
                    if(tmpTeam == "1") score1 += 1;
                    else if(tmpTeam == "2") score2 += 1;
                }

            }
        }

        if(score1 > score2) team1 += 1;
        else if(score1 < score2) team2 += 1;

        // next time
        if(curr_sec == 59) { curr_min +=1; curr_sec = 0;}
        else curr_sec += 1;

    }

    cout << "team1 : " << team1 << endl;
    cout << "team2 : " << team2 << endl;

    string m1 = to_string(team1/60).size() == 1 ? "0" + to_string(team1/60) : to_string(team1/60);
    string s1 = to_string(team1%60).size() == 1 ? "0" + to_string(team1%60) : to_string(team1%60);

    string m2 = to_string(team2/60).size() == 1 ? "0" + to_string(team2/60) : to_string(team2/60);
    string s2 = to_string(team2%60).size() == 1 ? "0" + to_string(team2%60) : to_string(team2%60);

    cout << m1 << ":" << s1 << "\n";
    cout << m2 << ":" << s2 << "\n";

}



int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    getInput();
    solution();

    return 0;
}