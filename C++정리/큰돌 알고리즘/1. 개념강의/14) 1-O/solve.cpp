#include <bits/stdc++.h>
#include <string>
#include <iostream>
#include <stack>

using namespace std;
int n, ret;
string s;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    freopen("input.txt", "r", stdin);

    cin >> n;
    for(int i = 0; i < n; i++){
        // cout << "--------" << "\n";
        // cout << "int i : " << i << "\n";

        cin >> s;
        stack<char> stk;
        for(char a : s){
            // cout << " ##" << "\n";
            // cout << " value of  a : " << a << "\n";
            // cout << "stk.top() : " << stk.top() << "\n";
            if(stk.size() && stk.top() == a)stk.pop();
            else stk.push(a);
        }
        if(stk.size() == 0)ret++;
    }
    cout << ret << "\n";
}