# 1-B

- [문제링크](https://www.acmicpc.net/problem/11655)

## 알면 좋은점

> 1. 대문자 65 ~ 66, 소문자 97 ~ 122 (diff는 26)
> 2. text 들여오기 : freopen("text.txt", "r", stdin)

<br>

## 코드

- 해설

  ```c++
    #include<bits/stdc++.h>
    using namespace std;
    string s;
    int main(){
        getline(cin, s);
        for(int i = 0; i < s.size(); i++){
            // 대문자인경우
            if(s[i] >= 65 && s[i] < 97){
                if(s[i] + 13 > 90) s[i] = s[i] + 13 - 26;
                else s[i] = s[i] + 13;
            }else if(s[i] >= 97 && s[i] <= 122){
                if(s[i] + 13 > 122)s[i] = s[i] + 13 - 26;
                else s[i] = s[i] + 13;
            }
            cout << s[i];
        }
        return 0;
    }


  ```

- 내코드

  ```c++
    #include <bits/stdc++.h>
    #include <string>
    #include <algorithm>
    #include <iostream>

    using namespace std;

    //
    bool isTextTrue = true;

    string getInput() {

        if(isTextTrue) freopen("input.txt", "r", stdin);

        string str;

        //cin >> str;
        getline(cin, str);


        return str;
    }

    int main(){
        ios_base::sync_with_stdio(false);
        cin.tie(NULL); cout.tie(NULL);

        string str = getInput();

        cout << "str is : " << str << "::::\n";

        for(int k=0; k<str.size(); k++){
            if( isalpha(str[k]) ) {
                if(str[k] >= 65 && str[k] < 97){
                    if(str[k] + 13 > 90) str[k] = str[k] + 13 - 26;
                    else str[k] = str[k] + 13;
                }else if(str[k] >= 97 && str[k] <= 122){
                    if(str[k] + 13 > 122) str[k] = str[k] + 13 - 26;
                    else str[k] = str[k] + 13;
                }
            }
        }

        for(char c : str) cout << c;

        return 0;


    }


  ```
