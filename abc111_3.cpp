#include <iostream>
#include <algorithm>
using namespace std;

int n;
pair<int, int> A[100000], B[100000];
int num = 0;

void solve(){
    // secondを基準にして，A, Bを降順にsort
    sort(
        A,
        A + 100000);
    sort(
        B,
        B + 100000);

    int a = 0;
    int b = 0;
    if (A[a].second == B[b].second){
        num = min(A[a + 1].first + B[b].first, A[a].first + B[b + 1].first);
    }else{
        num = A[a].first + B[b].first;
    }
}

int main(){
    cin >> n;
    // A, Bの初期化
    for (int i = 0; i < 100000; i++){
        A[i].second = 0;
        A[i].first = 0;
        B[i].second = 0;
        B[i].first = 0;
    }
    for (int i = 0; i < n; i++){
        int element;
        cin >> element;
        if (i % 2 == 0){
            A[element].second = element;
            A[element].first -= 1;
        }
        else{
            B[element].second = element;
            B[element].first -= 1;
        }
    }
    solve();
    cout << n + num << endl;
    return 0;
}