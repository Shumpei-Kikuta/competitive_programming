#include <iostream>
#include <algorithm>
using namespace std;
#include <string>

int N;
string S;

int main(){
    cin >> N >> S;
    int left = 0;
    int right = 0;
    for (int i = 1; i < N; i++){
        if (S[i] == 'E'){
            right += 1;
        }
    }
    int num = right + left;
    for (int i = 0; i < N - 1; i++){
        if (S[i] == 'E'){
            left = left;
        }else{
            left += 1;
        }
        if (S[i + 1] == 'E'){
            right -= 1;
        }else{
            right = right;
        }
        num = min(num, right + left);
    }
    cout << num << endl;
    return 0;
}