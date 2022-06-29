# 1-B

- [문제링크](https://www.acmicpc.net/problem/1213)

## 알면 좋은점

> 1. 반례가 있는지 체크
>
> - 홀수개가 2개 이상이면 팰런드롬 못만든다; 홀수 1개 혹은 0개

<br>

## 코드

- 해설

  ```c++
  #include<bits/stdc++.h>
  using namespace std;
  string s, ret;
  int cnt[200], flag;
  char mid;
  int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> s;
    for(char a : s)cnt[a]++;
    for(int i = 'Z'; i >= 'A'; i--){
      if(cnt[i]){
        if(cnt[i] & 1){
          mid = char(i);flag++;
          cnt[i]--;
        }
        if(flag == 2)break;
        for(int j = 0; j < cnt[i]; j += 2){
          ret = char(i) + ret;
          ret += char(i);
        }
      }
    }
    if(mid)ret.insert(ret.begin() + ret.size() / 2, mid);
    if(flag == 2)cout << "I'm Sorry Hansoo\n";
    else cout << ret << "\n";
  }
  ```

- 내코드

  ```c++
  #include <bits/stdc++.h>
  #include <map>
  #include <string>
  #include <algorithm>

  using namespace std;

  //
  bool isTextPresent = true;
  string str;
  map<char, int> _map;


  void getInput() {
      if(isTextPresent) freopen("input.txt", "r", stdin);

      cin >> str;
      cout << "str : " << str << "\n";

  }

  int main(){

      ios_base::sync_with_stdio(false);
      cin.tie(NULL); cout.tie(NULL);

      //
      getInput();


      for(char ch: str){
          _map[ch]++;
      }

      bool answerIsNotPossible = false;
      int oddCnt = 0;
      string oddChar = "";
      for(auto key: _map){
          cout << "key.first : " << key.first << " / " << "key.second : " << key.second << "\n";

          if(key.second % 2 == 1 ) {oddCnt += 1; oddChar = key.first;}
      }

      cout << oddCnt << "\n";

      if(oddCnt >= 2) {cout << "I'm Sorry Hansoo"; return 0;}


      if(oddCnt == 0){
          string temp = "";
          int cnt = 0;
          for( auto key: _map){
              for(int j=0; j < key.second / 2; j++){
                  temp += key.first;
              }

              // cout << "Temp : " << temp << " cnt : " << cnt << "\n";
          }

          string rev = temp;
          reverse(rev.begin(), rev.end());
          temp = temp + rev;

          cout << "temp : " << temp << "\n";
          cout << "H1";
      }

      else {
          string temp = "";
          int cnt = 0;
          for( auto key: _map){
              if(key.second % 2 == 0){
                  for(int j=0; j < key.second / 2; j++){
                      temp += key.first;
                  }
              } else if (key.second == 1){
                  oddChar = key.first;
              } else {
                  for(int j=0; j < (key.second-1) / 2; j++){
                      oddChar = key.first;
                      temp += key.first;
                  }
              }

              // cout << "Temp : " << temp << " cnt : " << cnt << "\n";
          }

          string rev = temp;
          reverse(rev.begin(), rev.end());
          temp = temp + oddChar + rev;

          cout << "temp : " << temp << "\n";
          cout << "H2";

      }

      return 0;

  }

  ```
