
#include <bits/stdc++.h>
#include <string>
#include <map>

using namespace std;
bool checkConsistency(string _str){
	
	//not exist, wrong
	for(auto ch: "aeiou"){
		string _ch = to_string(ch);
		if(_str.find(_ch) == string::npos){
			return false;
		}
	}
	
	for(int i=0; i < _str.size()-1; i++){
		string _subStr = _str.substring(i, 2);
		if(_subStr[0] == _subStr[1]){ 
			if( !(_subStr == "oo" || 
			   _subStr == "ee") ) return false; 
		}
	}
	
	return true;
}

bool isInputPresent = true;


bool checkConsistency(string _str){
		
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	
	string tmpInput = "";
	
	while(true){
		cin >>	tmpInput;
		if(tmpInput == 	"end") break;
		
		if(checkConsistency(tmpInput)) cout << "<" << tmpInput << "> is acceptable" << "\n";
		else cout << "<" << tmpInput << "> is not acceptable" << "\n";
		
	}
	
	return 0;
	
}
