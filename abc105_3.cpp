#include <iostream>
#include <algorithm>
using namespace std;
#include <math.h>
#include <string>
#include <vector>

long int N;
vector<int> ans;
int main(){
    cin >> N;
    while(true){
        int amari = N % (-2);
        N = N / (-2);
        if (amari == -1){
            amari += 2;
            N += 1;
        }
        ans.push_back(amari);
        if (N == 0){
            break;
        }
    }
    for (int i = ans.size() - 1; i >= 0; i--){
        cout << ans[i];
    }
    cout << endl;
    return 0;
}