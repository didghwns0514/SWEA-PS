# 1-B

- [문제링크](http://boj.kr/a7e74bfb990641249d917c73a9246796)

## 알면 좋은점
> 1) 알파벳 [0] 등올 해서 access 하면 됨
> 2) 'a'에 숫자연산 하면 char 값
> 3) 'z'에 +1 하면 다시 'a' 처리
> 4) string 변수에 .size()로 null 체크 가능


<br>

## 코드

- 해설

  ```c++
  #include<bits/stdc++.h>
  using namespace std;
  int n, cnt[26];
  string s, ret;
  int main(){
      cin >> n;
      for(int i = 0; i < n; i++){
          cin >> s;
          cnt[s[0] - 'a']++;
      }
      for(int i = 0; i < 26; i++)if(cnt[i] >= 5) ret+=  i + 'a';
      if(ret.size()) cout << ret << "\n";
      else cout << "PREDAJA" << "\n";
  }
  ```

- 내코드

  ```c++
  #include <bits/stdc++.h>
  #include <iostream>
  #include <algorithm>
  #include <string>

  using namespace std;

  //
  bool isInputText = false;
  char i = 'a';
  string returnResult;
  string nameData[150];

  int inputText() {
      int inputIteration;
      string tempString;


      if(isInputText) freopen("input.txt", "r", stdin);
      cin >> inputIteration;

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
          cout << "PREDAJA" << "\n";
      }
      else{
          cout << returnResult << "\n";
      };

      return 0;
  }



  ```
