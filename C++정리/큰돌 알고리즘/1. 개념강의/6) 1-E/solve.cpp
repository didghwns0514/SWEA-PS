#include <bits/stdc++.h>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

//
char i;
string returnResult;
string nameData[150];

prijestolonasljednikovi

int repeat;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    nameData[0] = "babic";

nameData[1] ="keksic";
nameData[2] ="boric";
nameData[3] ="bukic";
"sarmic";
"balic";
"kruzic";
"hrenovkic";
"beslic";
"boksic";
"krafnic";
""
klavirkovic
kukumaric
sunkic
kolacic
kovacic

    cin >> repeat;
    for(int j=0; j<repeat; j++){
        cin >> nameData[j];
    }
    
    do{
        int count = 0;
        for(string name : nameData){
            if(name[0] == i) {count += 1;}
        }
        if(count >= 5) {returnResult += i;}
        
        i += 1;
    } while( i != 'z' );
    
    if(returnResult == "") cout << "PREDAJA" << "\n";
    else cout << returnResult << "\n"; 
    
    return 0;
}