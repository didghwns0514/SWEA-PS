# 2-H

- [문제링크]()

## 알면 좋은점

> 1. const int INF = 987654321; :: [참조](https://wizii.tistory.com/15)
> 2. string의 erase 메서드 :: [참조](https://modoocode.com/240)
>    - string.erase([시작index], <끝index>)
> 3. string의 clear 메서드 :: 모든 string 값 다 지움

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
  int n;
  vector<string> v;
  string s, ret;

  void go(){
    if(ret.size()){
      while(true){
        if(ret.size() && ret.front() == '0')ret.erase(ret.begin());
        else break;
      }
      if(ret.size() == 0) ret = "0";
      v.push_back(ret);
      ret = "";
    }
  }

  // 비내림차순 -> 오름차순
  bool cmp(string a, string b){
    if(a.size() == b.size()) return a < b; // string값으로 순서  보장
    return a.size() < b.size(); // 같은 사이즈 아닌 경우, 사이즈로 순서 보장
  }

  int main () {
    cin >> n;
    for(int i = 0; i < n; i++){
      cin >> s;
      ret = "";
      for(int j = 0; j < s.size(); j++){
        if(s[j] < 58)ret += s[j]; // 숫자 string인 경우 추가
        else{
          go(); // 아닌경우 지금까지 찾은 숫자 출력, 보관
        }
      }
      go();
    }
    sort(v.begin(), v.end(), cmp);
    for(string i : v)cout << i << "\n";
    return 0;
  }
  ```

- 내코드

  ```c++

  ```
