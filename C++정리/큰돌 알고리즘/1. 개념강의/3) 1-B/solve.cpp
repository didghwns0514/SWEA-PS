
#include <bits/stdc++.h>
#include <iostream>
#include <algorithm>

int main() {

    using namespace std;

    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int littlePeople[9];
    int totalSum = 0;
    int currNum;
    for(int k=0; k < 9; k ++){
        cin >> currNum;
        littlePeople[k] = currNum;
        totalSum += currNum;
    }

    for(int i1=0; i1<9-2; i1++){

        for(int i2=i1+1; i2<9-1; i2++ ){

            for(int i3=i2+1; i3<9; i3++){
                int n1 = littlePeople[i1];
                int n2 = littlePeople[i2]; 
                int n3 = littlePeople[i3];
                if( totalSum - (n1 + n2 + n3) == 100 ){
                    
                    sort(littlePeople, littlePeople+9);

                    for(int k; k<9; k++){
                        if(
                              (littlePeople[k]==n1)
                           || (littlePeople[k]==n2)
                           || (littlePeople[k]==n3)
                        ){
                            continue; 
                        }
                        else {
                            cout << littlePeople[k] << '\n';
                        }
                    }


                }
            }
        }

    }

}