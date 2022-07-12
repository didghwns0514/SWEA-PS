
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
