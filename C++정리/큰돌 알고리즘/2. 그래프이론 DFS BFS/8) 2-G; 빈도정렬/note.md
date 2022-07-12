# 2-E

- [문제링크](https://www.acmicpc.net/problem/2910)

## 알면 좋은점

> 1. map 사용법 정리 블로그 [링크](https://life-with-coding.tistory.com/305)
>    - MAP 에 특정 값 판별, 다음이 true 이면 없는 것 :: \_when.find(tmpInput) == \_when.end()
>    - sort의 compare 함수 [링크](https://leeeegun.tistory.com/5) ; => array, vector …
>      - sort(\_vec.begin(), \_vec.end(), comp);
>    - `true 인게 앞으로 오게 만드는 형식`
>    - vector :: push_back
> 2. typedef long long ll;
> 3. const INF = 1e18;
> 4. pair :: first, second // tuple :: first, second, third
> 5. tuple access :: get<0>(\_tuple_name)
> 6. 여러줄 주석은 /\* \*/로 처리하여 컴파일 에러 피하기
> 7. 너무 많은 메모리 할당은 문제될 수 있음, 배열 10억자리 등

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

  ```c++
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

  ```

- 내코드

  ```c++

  #include <bits/stdc++.h>
  #include <algorithm>
  #include <vector>
  #include <utility>
  #include <iostream>
  #include <map>

  using namespace std;

  bool comp(tuple<int, int, int> p1, tuple<int, int, int> p2);
  void solution();
  void getInput();

  int N;
  int C;
  vector< tuple<int, int, int> > _vec;
  bool isInputPresent = true;
  map<int, int> _map, _when;

  // number 자체, 리스트에서 처음 인덱스, 개수
  bool comp(tuple<int, int, int> p1, tuple<int, int, int> p2){
  	if( get<2>(p1) != get<2>(p2)) return get<2>(p1) > get<2>(p2);
  	else{
  		// return p1.second > p2.second;
  		return get<1>(p1) < get<1>(p2);
  	}
  }

  void solution() {


  	for(auto k: _map){
  		// k.first : 숫자, k.second : 개수
  		if( k.first >= 1 && k.second >= 1){
  			// number 자체, 리스트에서 처음 인덱스, 개수
  			_vec.push_back({ k.first, _when[k.first], k.second});
  		}
  	}

  	/* for(auto k: _vec){
  	// 	int p1 = 0; int p2 = 0; int p3 = 0;
  	// 	tie(p1, p2, p3) = k;
  	// 	cout << "=========" << "\n";
  	// 	cout << "number 자체, 리스트에서 처음 인덱스, 개수" << "\n";
  	// 	cout << "p1 : " << p1 << " p2 : " << p2 << " p3 : " << p3 << "\n";
  	// }
  	*/

  	sort(_vec.begin(), _vec.end(), comp);

  	for(auto k: _vec){
  		int p1 = 0; int p2 = 0; int p3 = 0;
  		tie(p1, p2, p3) = k;

  		for(int i1=0; i1 < p3; i1++){
  			cout << p1 << " ";
  		}
  	}
  }

  void getInput(){

  	if(isInputPresent) freopen("input.txt", "r", stdin);
  	cin >> N >> C;

  	for(int k=0; k < N; k++) {

  		int tmpInput = 0; cin >> tmpInput;
  		_map[tmpInput] += 1;
  		if( _when.find(tmpInput) == _when.end() ) _when[tmpInput] = k;
  	}
  }

  int main(){
  	ios_base::sync_with_stdio(false);
  	cin.tie(NULL); cout.tie(NULL);

  	getInput();
  	solution();

  	return 0;


  }

  ```
