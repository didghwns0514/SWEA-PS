#include <bits/stdc++.h>
#include <string>
#include <algorithm>
#include <iostream>

using namespace std;

//
bool isTextTrue = true;

string getInput() {

    if(isTextTrue) freopen("input.txt", "r", stdin);

    string str;

    //cin >> str;
    getline(cin, str);


    return str;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    string str = getInput();

    cout << "str is : " << str << "::::\n";

    for(int k=0; k<str.size(); k++){
        if( isalpha(str[k]) ) {
            // 대문자
            if(str[k] >= 65 && str[k] < 97){
                if(str[k] + 13 > 90) str[k] = str[k] + 13 - 26; 
                else str[k] = str[k] + 13;
            }
            // 소문자
            else if(str[k] >= 97 && str[k] <= 122){
                if(str[k] + 13 > 122) str[k] = str[k] + 13 - 26; 
                else str[k] = str[k] + 13;  
            }
        }
    }

    // for(int k=0; k<str.size(); k++){
    //     if( isalpha(str[k]) ) {
    //         if(str[k] >= 65 && str[k] < 97){
    //             if(str[k] + 13 > 90) str[k] = str[k] + 13 - 26; 
    //             else str[k] = str[k] + 13;  
    //         }else if(str[k] >= 97 && str[k] <= 122){
    //             if(str[k] + 13 > 122) str[k] = str[k] + 13 - 26; 
    //             else str[k] = str[k] + 13;  
    //         }
    //     }
    // }
    
    for(char c : str) cout << c;
    
    return 0;
    
    
}

