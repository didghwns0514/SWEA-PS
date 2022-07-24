# 2-N

- [문제링크](https://www.acmicpc.net/problem/9012)

## 알면 좋은점

> 1. index로 찾아서 replace는 뭔가 안됨 -> 0번 index에서도 에러... => erase 사용하기!!
> 2. 키재기, 짝맞추기 등등 메모이제이션 쓰면 됨

<br>

## 코드

- 해설

  ```c++
    #include <bits/stdc++.h>
    using namespace std;
    int n;
    string s;
    bool check(string s){
        stack<char> stk;
        for(char c : s){
            if(c == '(')stk.push(c);
            else{
                if(!stk.empty()) stk.pop();
                else return false;
            }
        }
        return stk.empty();
    }
    int main() {
        cin >> n;
        for(int i = 0; i < n; i++){
            cin >> s;
            if(check(s)) cout << "YES\n";
            else cout << "NO\n";
        }
        return 0;
    }
  ```

- 내코드

  ```c++
    #include <bits/stdc++.h>
    #include <string>
    #include <regex>

    using namespace std;

    // function
    void getInput();
    void solution();

    // global
    bool isInputPresent = true;
    int N;


    void getInput(){

        if(isInputPresent) freopen("input.txt", "r", stdin);

        cin >> N;
    }

    void solution(){

        string tmpString = "";
        for(int i=0; i < N; i++){
            // cout << "----------" << endl;
            cin >> tmpString;
            // cout << "tmpString :: " << tmpString << endl;
            int sizeLimit = tmpString.size() / 2;

            for(int k=0; k < sizeLimit; k++){

                if(tmpString.find("()") != string::npos){
                    int _index = tmpString.find("()");
                    // cout << "-  _index :: " << _index << endl;
                    // cout << "-  _index+2 :: " << _index+1 << endl;
                    if(_index != 0){
                        tmpString.erase(_index, 2);
                        // cout << "-  tmpString :: " << tmpString << endl;
                    }
                    else{
                        tmpString.replace(_index, _index + 2, "");
                        // cout << "-  tmpString :: " << tmpString << endl;
                    }

                }
            }

            if(tmpString == "") cout << "YES";
            else cout << "NO";
            cout << "\n";
        }



    }

    int main() {

        ios_base::sync_with_stdio(false);
        cout.tie(NULL); cin.tie(NULL);

        getInput();
        solution();

        return 0;

    }

  ```
