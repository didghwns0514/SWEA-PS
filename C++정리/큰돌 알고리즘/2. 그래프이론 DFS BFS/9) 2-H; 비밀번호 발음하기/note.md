# 2-H

- [문제링크](https://www.acmicpc.net/problem/4659)

## 알면 좋은점

> 1. find if sub-string(or Char) exists inside a larger string
>    - [참조할 링크](https://stackoverflow.com/questions/2340281/check-if-a-string-contains-a-string-in-c)
>    - 사용법 :: str.find(str2) != string::npos)

- [문자열 총정리 참조)(https://blockdmask.tistory.com/338)

> 2. to_string
> 3. get substring from string
>
> - [참조](https://modoocode.com/235)
>
> 4. split string
> 5. get string size

<br>

## 코드

- 해설

  ```c++
  #include <bits/stdc++.h>
  using namespace std;
  #define sz(x) ((int)(x).size())
  #define f first
  #define s second
  typedef unsigned long long ll;
  const int INF = 987654321;
  string s;
  int cnt[30], lcnt, vcnt;
  bool isVowel(int idx){
    return (idx == 0 || idx == 4 || idx == 8 || idx == 14 || idx == 20);
  }
  int main () {
    while(true){
      cin >> s;
      if(s == "end")break;
      memset(cnt, 0, sizeof(cnt));
      lcnt = vcnt = 0;
      bool flag = 0;
      int prev = -1;
      for(int i = 0; i < s.size(); i++){
        int idx = s[i] - 'a';
        cnt[idx]++;
        if(isVowel(idx))lcnt++, vcnt = 0;
        else vcnt++, lcnt = 0;
        if(vcnt == 3 || lcnt == 3) flag = 1;
        if(i >= 1 && (s[i - 1] == s[i]) && (idx != 4 && idx != 14)){
          flag  = 1;
        }
      }
      if(!cnt[0] && !cnt[4] && !cnt[8] && !cnt[14] && !cnt[20])flag = 1;
      if(flag) cout << "<" << s << ">" << " is not acceptable.\n";
      else cout << "<" << s << ">" << " is acceptable.\n";
    }
    return 0;
  }
  ```

- 내코드

  ```c++
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



  ```
