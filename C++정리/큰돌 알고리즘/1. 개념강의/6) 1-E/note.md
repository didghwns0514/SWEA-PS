# 1-B

- [문제링크](https://www.acmicpc.net/problem/1159)

## 알면 좋은점

<br>

## 코드

- 해설

  ```c++
  #include<bits/stdc++.h>
  using namespace std;
  string s, temp;
  int main(){
      cin >> s;
      temp = s;
      reverse(temp.begin(), temp.end());
      if(temp == s) cout << 1 << "\n";
      else cout << 0 << "\n";

      return 0;
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
  string originalString;
  string reverseString;

  int main(){

      ios_base::sync_with_stdio(false);
      cin.tie(NULL); cout.tie(NULL);

      cin >> originalString;

      reverseString = originalString;
      reverse(reverseString.begin(), reverseString.end());

      if (originalString == reverseString) cout << "1";
      else if (originalString != reverseString) cout << "0";

      return 0;
  }
  ```
