#include <bits/stdc++.h>
#include <string>
#include <map>
#include <vector>

using namespace std;

bool checkConsistency(string _str);
void getInput();
bool checkIsVowul(char ch);

bool isInputPresent = true;
vector< string > _vec;


void getInput(){
	if(isInputPresent) freopen("input.txt", "r", stdin);

	string tmpString = "";
	while(true){
		cin >> tmpString;
		if(tmpString == "end") break;
		_vec.push_back(tmpString);

	}


}

bool checkConsistency(string _str){
	// cout << "----" << "\n";
	// cout << " => _str : " << _str << "\n";
	// cout << " => 1" << "\n";
	bool isMoulFound = false;
	
	//not exist, wrong
	for(auto ch: "aeiou"){
		// cout << "  - ch : " << ch << "\n";

		// string _ch = to_string(ch);
		if(_str.find(ch) != string::npos){
			isMoulFound = true;
		}
	}
	if(!isMoulFound) return false;

	// cout << " => 2" << "\n";
	
	for(int i=0; i < _str.size()-1; i++){
		string _subStr = _str.substr(i, 2);
		if(_subStr[0] == _subStr[1]){ 
			if( !(_subStr == "oo" || 
			      _subStr == "ee") ) return false; 
		}
	}

    if(_str.size() >= 3){
	for(int i=0; i < _str.size()-2; i++){
		if(
			(
				checkIsVowul(_str[i]) == true && checkIsVowul(_str[i+1]) == true && checkIsVowul(_str[i+2]) == true
			) || 
			(
				checkIsVowul(_str[i]) == false && checkIsVowul(_str[i+1]) == false && checkIsVowul(_str[i+2]) == false
			)

		) return false;
	}
    }

	
	return true;
}

bool checkIsVowul(char ch){

	bool isVowul = false;
	for(auto _ch: "aeiou"){
		if(_ch == ch) {isVowul = true; break;}
	}

	return isVowul;

}


int main(){

	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	
	string _str = "";
	bool tmpBool = false;
	
	// cout << "1" << "\n";

	// getInput();

	// for(auto _str: _vec){
	while(true){
		
		cin >> _str;
		if(_str == "end") break;

		// cout << "############" << "\n";
		tmpBool = checkConsistency(_str);
		// cout << "tmp Bool : " << tmpBool << "\n";
		if(tmpBool) {
			cout << "<" << _str << "> is acceptable" << "\n";
		}
		else{ 
			cout << "<" << _str << "> is not acceptable" << "\n";
		}
	}

	return 0;
	
}


