# 1-B

- 알파벳 개수
- [문제링크](http://boj.kr/4e97e76bb0dd438fba134d0aada1c531)

## 알면 좋은점

- 해설

  ```c++
  #include <bits/stdc++.h>
  using namespace std;
  int A, B, C, a, b, cnt[104], ret;
  int main(){
    cin >> A >> B >> C;
    for(int i = 0; i < 3; i++){
      cin >> a >> b;
      for(int j = a; j < b; j++)cnt[j]++;
    }
    for(int j = 1; j < 100; j++){
      if(cnt[j]){
        if(cnt[j] == 1) ret += A;
        else if(cnt[j] == 2)ret += B * 2;
        else if(cnt[j] == 3)ret += C * 3;
      }
    }
    cout << ret << "\n";
      return 0;
  }

  ```

- 내코드

  ```c++
  #include <bits/stdc++.h>
  #include <iostream>
  #include <algorithm>

  using namespace std;

  int A, B, C, sTime, eTime, timeCount[101];
  int fee = 0;

  int main(){
      ios_base::sync_with_stdio(false);
      cin.tie(NULL); cout.tie(NULL);

      cin >> A >> B >> C;

      for(int j=0; j<101; j++){
          timeCount[j]=0;
      }

      for(int k=0; k<3; k++){
          cin >> sTime >> eTime;
          for(int j=sTime; j<eTime; j++){
              timeCount[j] += 1;
          }
      }

      for(int q=0; q< 101; q++){
          if(timeCount[q]==1) fee += A;
          else if(timeCount[q]==2) fee += (B * 2);
          else if(timeCount[q]==3) fee += (C * 3);
      }

      cout << fee;
      return 0;

  }
  ```
