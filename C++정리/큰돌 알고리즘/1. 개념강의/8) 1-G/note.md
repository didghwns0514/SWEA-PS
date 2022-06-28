# 1-B

- [문제링크](https://www.acmicpc.net/problem/11655)

## 알면 좋은점

> 1. string 값 짜르기 : result = split(str, ',');
> 2. substring and find : String 객체에 대해서 수행
>
> - substring(index1, index2) : index1 ~ index2 - 1 까지
> - substring(index3) : index3 ~ last index

```c++
  #include <string>
  #include <vector>
  #include <iostream>
  #include <map>
  #include <sstream>
  #include <typeinfo>
  using namespace std;

  int main(){
      string tmp = "welcome to splitWorld!!! ";
      int prev = 0; //이전 위치
      int cur; //현재위치
      cur = tmp.find(' ');
      while (cur != string::npos)
      {
          string substring = tmp.substr(prev, cur - prev); //첫인자에서부터 두번째 인자의 크기만큼까지를 반환하는 함수이다. => substr
          cout << substring << " ";
          prev = cur + 1;
          cur = tmp.find(' ',prev); //prev지점부터 탐색을 시작한다.
      }
      //남아있는 문자열 출력
      cout << tmp.substr(prev, cur - prev);
      return 0;

  }
```

<br>

## 코드

- 해설

  ```c++
  #include<bits/stdc++.h>
  using namespace std;
  int n;
  string s, ori_s, pre, suf;
  int main(){
      cin >> n;
      cin >> ori_s;
      int pos = ori_s.find('*');
      pre = ori_s.substr(0, pos);
      suf = ori_s.substr(pos + 1);
      for(int i = 0; i < n; i++){
          cin >> s;
          if(pre.size() + suf.size() > s.size()){
              cout << "NE\n";
          }else{
              if(pre == s.substr(0, pre.size()) && suf == s.substr(s.size() - suf.size())) cout << "DA\n";
              else cout <<"NE\n";
          }
      }
      return 0;
  }

  ```

- 내코드

  ```c++


  ```
