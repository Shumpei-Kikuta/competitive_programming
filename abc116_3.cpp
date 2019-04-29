#include <iostream>
#include <algorithm>
using namespace std;
#define MAX 100

int N;
int h[MAX];
int num = 0;

int find_min_idx(int left, int right){
    // return the index of the minimum value in h
    int min_idx = left;
    for (int i = left; i <= right; i++){
        if (h[min_idx] > h[i]){
            min_idx = i;
        }
    }
    return min_idx;
}

void binary_calc(int left, int right){
    // minを見つける
    int min_idx = find_min_idx(left, right);
    num += h[min_idx];
    int each_num = h[min_idx];
    for (int i = left; i <= right; i++){
        h[i] -= each_num;
    }
    if (min_idx != right){
        binary_calc(min_idx+1, right);
    }
    if (min_idx != left){
        binary_calc(left, min_idx-1);
    }
}

int main(){
    cin >> N;
    for (int i = 0; i < N; i++){
        cin >> h[i];
    }
    binary_calc(0, N-1);
    cout << num << endl;

    return 0;
}

// 反省