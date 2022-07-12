# 2-E

- [문제링크](https://www.acmicpc.net/problem/2910)

## 알면 좋은점

> 1. map 사용법 정리 블로그 [링크](https://life-with-coding.tistory.com/305)
> 2. typedef long long ll
> 3. const INF = 1e18;
> 4. pair :: first, second // tuple :: first, second, third


<br>

## 코드

- 해설

  ```c++	
	#include <bits/stdc++.h>
	using namespace std;  
	typedef long long ll;
	
	const ll INF = 1e18;   
	int n, c, a[1004];
	
	vector<pair<int, int>> v; 
	map<int, int> mp, mp_first; 

	bool cmp(pair<int,int> a, pair<int, int> b){
		if(a.first == b.first){
			return mp_first[a.second] < mp_first[b.second];
		}
		return a.first > b.first;
	}

	int main(){
		ios_base::sync_with_stdio(false);
		cin.tie(NULL); cout.tie(NULL);
		cin >> n >> c; 
		
		for(int i = 0; i < n; i++){
			cin >> a[i];mp[a[i]]++;
			if(mp_first[a[i]] == 0) mp_first[a[i]] = i + 1; 
		} 
		for(auto it : mp){
			v.push_back({it.second, it.first});
		}
		sort(v.begin(), v.end(), cmp);
		for(auto i : v){
			for(int j = 0; j < i.first; j++){
				cout << i.second << “ “;
			}
		} 
		 
		return 0;
	}

  ```

- 해설2
	~~~c++
	#include <iostream>
	#include <map>
	#include <vector>
	#include <algorithms>
	using namespace std;

	int n, c;
	map<int, int> firstindex;
	map<int,int > countarr;

	bool cmp(int x,int y){
		if (x == y)	return false;
		if (countarr[x] > countarr[y])	return true;
		else if (countarr[x] == countarr[y]) {
			if (firstindex[x] >= firstindex[y])	return false;
			else return true;
		}
		else return false;
	}
	
	int main() {
		ios::sync_with_stdio(false);
		cin.tie(NULL);
		cout.tie(NULL);

		vector<int> input;
		cin >> n >> c;

		input.resize(n);
		for (int i = 0; i < n; i++) {
			cin >> input[i];
			countarr[input[i]]++;
			if (firstindex.find(input[i]) == firstindex.end()) {
				firstindex[input[i]]= i;
			}
		}

		sort(input.begin(), input.end(), cmp);
		
		for (int i = 0; i < n; i++) {
			cout << input[i] << “ “;
		}
		cout << “\n”;
		return 0;
	}
	~~~ 

- 내코드

  ```c++
  #include <bits/stdc++.h>
  #include <vector>

  using namespace std;

  //
  int totalMoves;
  int isInputPresent = true;
  int N, M, J,  r;
  int l = 1;
  vector<int> _vec;

  void getInput();
  void solve();

  void getInput() {

      if(isInputPresent) freopen("input.txt", "r", stdin);

      cin >> N >> M;
      cin >> J;

      for(int j=0; j < J; j++){
          int tmp = 0; cin >> tmp;
          _vec.push_back(tmp);
      }
  }

  void solve(){
      for(auto i : _vec){
          // cout << "---------" << "\n";
          // cout << " i : " << i << "\n";
          r = l + M - 1;
          if(l <= i && i <= r) {

              // cout << "Not move!" << "\n";
              continue;
              }
          else{
              int diff = 0;
              if(r < i){
                  diff = i - (r);
                  l += diff;
                  totalMoves += diff;
              }
              else if(l > i) {
                  diff = l - i;
                  l = i;
                  totalMoves += diff;
              }
              // cout << "Diff : " << diff << "\n";
              // cout << "currNode : " << currNode << "\n";
              // cout << "totalMoves : " << totalMoves << "\n";
          }

      }
  }

  int main(){

      ios_base::sync_with_stdio(false);
      cin.tie(NULL); cout.tie(NULL);

      getInput();

      solve();

      cout << totalMoves;

      return 0;

  }
  ```
