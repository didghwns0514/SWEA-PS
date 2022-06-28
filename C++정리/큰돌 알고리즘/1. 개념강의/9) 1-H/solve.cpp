#include <bits/stdc++.h>
#include <string>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <vector>

using namespace std;

//
bool isTextPresent = true;
int numData;
string pattern;
string beginString = "";
string endString = "";

int getInput() {
    if(isTextPresent){
        freopen("input.txt", "r", stdin);
    }
    cin >> numData;
    cin >> pattern;

    cout << "numData : " << numData << "\n";
    cout << "pattern : " << pattern << "\n";
    
    return 0;
    
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    getInput();
    

    bool isBeginFound = false;
    
    for(char ch : pattern){
        if(ch == '*' && !isBeginFound){
            isBeginFound = true;
            continue;
        }
        else if(!isBeginFound) beginString += ch;
        else endString += ch;
    }
    

    cout << "beginString String : " << beginString << "\n";
    cout << "endString String : " << endString << "\n";
    
    for(int k=0; k<numData; k++){
        string str;
        cin >> str;
        int sIndex = str.find(beginString);
        int eIndex = str.rfind(endString);


        

        cout << "str : " << str << "\n";
        cout << "sIndex : " << sIndex << " // " << "eIndex : " << eIndex << "\n";

        if (sIndex >= 0 && eIndex >= 0){

            string sString = str.substr(0, sIndex);
            string eString = str.substr(eIndex, str.size());

            if(
                sString == beginString && eString == endString
            ){
                cout << "DA" << "\n";
            }
            else cout << "NE" << "\n";
        }
        else cout << "NE" << "\n";

    }
    
}