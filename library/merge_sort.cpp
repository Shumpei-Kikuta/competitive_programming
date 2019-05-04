// 分割統治法の有名問題

#include <iostream>
#include <algorithm>
using namespace std;
#define MAX_N 500001
#define INF 1000000000000

long int num = 0;
long int L[MAX_N];
long int R[MAX_N];

void merge(int N, long int *X, int left, int mid, int right){
    int n1 = mid - left + 1;
    int n2 = right - mid;
    for (int i = 0; i < n1; i++){L[i] = X[left + i];}
    for (int i = 0; i < n2; i++){R[i] = X[mid + 1 + i];}
    L[n1] = INF; R[n2] = INF;
    int l = 0;
    int r = 0;
    for (int i = 0; i < n1 + n2; i++){
        if (L[l] < R[r]){
            X[left + i] = L[l];
            l++;
        }else{
            X[left + i] = R[r];
            r ++;
        }
        num += 1;
    }
}

void merge_sort(int N, long int *X, int left, int right){
    if (left < right){
        int mid = (left + right)/2;
        merge_sort(N, X, left, mid);
        merge_sort(N, X, mid + 1, right);
        merge(N, X, left, mid, right);
    }
}

int main(){
    int N;
    long int X[MAX_N];
    cin >> N;
    for (int i = 0; i < N; i++){
        cin >> X[i];
    }
    merge_sort(N, X, 0, N-1);
    for (int i = 0; i < N; i++){
        cout << X[i];
        if (i != N - 1){
            cout << " ";
        }
    }
    cout << endl;
    cout << num << endl;
    return 0;
}