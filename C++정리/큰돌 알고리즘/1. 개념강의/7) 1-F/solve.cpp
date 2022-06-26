#include <bits/stdc++.h>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

//
bool isInputText = true;
char i = 'a';
string returnResult;
string nameData[150];

int inputText() {
    int inputIteration;
    string tempString;

    
    if(isInputText) freopen("input.txt", "r", stdin);
    cin >> inputIteration;

    cout << "inputIteration : " << inputIteration << "\n";

    for(int k =0; k < inputIteration; k ++){
        cin >> tempString;
        nameData[k] = tempString; 
    }

    return 0;


}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    int count = 0;

    inputText();

    cout << "###########" << "\n";
    for(string name : nameData){
        if(name == "") continue;
        cout << name << "\n";
    }
    cout << "###########" << "\n";
    
    do{
        count = 0;
        for(string name : nameData){
            if (name == "") continue;
            if(name[0] == i) {count += 1;}
        }
        if(count >= 5) {returnResult += i;}
        
        i += 1;
    } while( i != 'a' );
    
    if(returnResult == "") {
        cout << "return Result! 1" << "\n";
        cout << "PREDAJA" << "\n";
    }
    else{ 
        cout << "return Result! 2" << "\n";
        cout << returnResult << "\n";
    }; 
    
    return 0;
}

