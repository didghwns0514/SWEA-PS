# 2-T

- [문제링크](https://www.acmicpc.net/problem/17298)

## 알면 좋은점

> 1. index pair 하면 stack 생각해보자 -> 나는 메모이제이션 써야할거같고, iter나올 때 stack 필이 옴
> 2. 괄호 문제 등등...
> 3. https://cocoon1787.tistory.com/347 참조!

<br>

## 코드

- 해설

  ```c++
  #include <bits/stdc++.h>
  using namespace std;
  int n, a[1000004], ret[1000004];
  stack<int> s;
  int main(){
    cin >> n;
    memset(ret, -1, sizeof(ret));
    for(int i = 0; i < n; i++){
      cin >> a[i];
      while(s.size() && a[s.top()] < a[i]){
        ret[s.top()] = a[i]; s.pop();
      }
      s.push(i);
    }
    for(int i = 0; i < n; i++) cout << ret[i] << " ";
  }

  ```

- 내코드

  ```c++
  #include <bits/stdc++.h>
  #include <iostream>


  using namespace std;

  //
  bool isInputPresent = true;
  int _data[1000000];
  int filtered[1000000];
  int N;

  int main() {

      ios_base::sync_with_stdio(false);
      cout.tie(NULL); cin.tie(NULL);

      if(isInputPresent) freopen("input.txt", "r", stdin);

      cin >> N;

      if( N == 1) cout << -1;
      else{

          for(int i=0; i < N; i++){
              cin >> _data[i];
          }

          //
          // for(int i=0; i < N; i++){
          //     cout << _data[i] << endl;
          // }
          // cout << "";

          int left_int = 0;
          int left_index = 0;
          for(int i=0; i < N; i++){

              // if( left_int > _data[i] && left_index > i) cout << left_int << " ";
              // else{

                  for(int k=i+1; k < N; k++){
                      if(_data[k] > _data[i] && k > i){
                          // cout << "data[k] : " << _data[k] << " data[i] : " << _data[i] << endl;
                          left_int=_data[k];
                          left_index=k;
                          break;
                      }
                  }
                  if(left_index > i && left_int > _data[i]) cout << left_int << " ";
                  else cout << -1 << " ";
              // }
          }

      }

      return 0;
  }
  ```
