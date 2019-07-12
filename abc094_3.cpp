#include <iostream>
#include <algorithm>
using namespace std;
#define MAX_N 200001

void get_median(long int *X, int N, long int *left_value, long int *right_value){
    long int Y[MAX_N];
    for (int i = 0; i < N; i++){
        Y[i] = X[i];
    }
    sort(Y, Y + N);
    *left_value = Y[N/2 - 1];
    *right_value = Y[N/2];
}

int main(){
    int N;
    long int left_value, right_value;
    long int X[MAX_N];
    cin >> N;
    for (int i = 0; i < N; i++){
        cin >> X[i];
    }
    get_median(X, N, &left_value, &right_value);
    // cout << left_value << right_value << endl;
    for (int i = 0; i < N; i++){
        if (X[i] <= left_value){
            cout << right_value << endl;
        }else{
            cout << left_value << endl;
        }
    }
    return 0;
}