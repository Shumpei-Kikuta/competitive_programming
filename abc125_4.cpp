#include <iostream>
#include <algorithm>
using namespace std;
#define MAX_N 100001

int N;
long int A[MAX_N];
long int num = 0;
int main(){
    cin >> N;
    for (int i = 0; i < N; i++){
        cin >> A[i];
    }
    long int min_value = 10000000000;
    int cnt = 0;
    for (int i = 0; i < N; i++){
        if (A[i] < 0){
            cnt += 1;
        }
        num += abs(A[i]);
        min_value = min(abs(A[i]), min_value);
    }
    if (cnt % 2 == 0){
        
    }else{
        num -= 2 * min_value;
    }
    cout << num << endl;
    return 0;
}