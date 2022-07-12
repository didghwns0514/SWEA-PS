#include <bits/stdc++.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <utilities>

using namespace std;
void getInput();

// variables
bool isInputPresent = true;
int N;
int currNum, currInt;
int currIntString;


void getInput(){
    if(isInputPresent) freopen("input.txt.", "r", stdin);
    cin >> N;        
}

int main()  {
    
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    while(currNum != N) {
        
        currIntString = to_string(currInt);
        
        
        currInt += 1;
        
    }
    
    return 0;
}