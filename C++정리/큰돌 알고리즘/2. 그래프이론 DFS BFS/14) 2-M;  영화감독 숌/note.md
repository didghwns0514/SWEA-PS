# 2-E

- [문제링크](https://www.acmicpc.net/problem/2828)

## 알면 좋은점

>

<br>

## 코드

- 해설

  ```c++
  #include<bits/stdc++.h>
  using namespace std;
  int n;
  int main() {
      cin >> n;
      int i = 666;
      for(;; i++){
          if(to_string(i).find("666") != string::npos)n--;
          if(n == 0)break;
      }
      cout << i << "\n";
  }
  ```

- 내코드

  ```c++
  #include <bits/stdc++.h>
  #include <string>

  using namespace std;

  //
  bool counter6(int _int);


  //
  int integer = 666;
  int target;
  int _count;
  bool isInputPresent = true;

  bool counter6(int _int){

      int returnbool = 0;
      string _strCounter = to_string(_int);

      for(int i=0; i < _strCounter.size() - 2; i++){

          if(
              (_strCounter[i] == '6') &&
              (_strCounter[i+1] == '6') &&
              (_strCounter[i+2] == '6')
          ) return true;

      }

      return false;
  }

  int main(){

      ios_base::sync_with_stdio(false);
      cin.tie(NULL); cout.tie(NULL);

      if(isInputPresent) freopen("input.txt", "r", stdin);
      cin >> target;

      while( _count != target ){

          if(counter6(integer)){
              _count += 1;
          }

          integer += 1;


      }

      cout << integer - 1;


      return 0;
  }
  ```
