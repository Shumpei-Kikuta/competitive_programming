#include <iostream>
#include <algorithm>
using namespace std;
#define MAX_N 100001

struct structure{
    char signal;
    int value;
};

int N;
structure A[MAX_N];

// int partition(int left, int right){
//     int l = 0;
//     int r = 0;
//     int norm = A[right].value;
//     structure tmp;
//     while (l + r < right - left){
//         if (A[left + l + r].value <= norm){
//             l++;
//         }else{
//             tmp = A[left + l + r];
//             A[left + l + r] = A[right - 1 - r];
//             A[right - 1 - r] = tmp;
//             r ++;
//         }
//     }
//     // swap(A[right], A[right - r]);
//     tmp = A[right];
//     A[right] = A[right - r];
//     A[right - r]  = tmp;
//     return right - r;
// }



int partition(int p, int r){
    // rA[r]より大きいものと，小さいものを分けるアルゴリズム
    structure x = A[r];
    int i = p - 1;
    for (int j = p; j < r; j++){
        if (A[j].value <= x.value){
            i++;
            structure tmp = A[i];
            A[i] = A[j];
            A[j] = tmp;
        }
    } 
    structure tmp = A[i + 1];
    A[i + 1] = A[r];
    A[r] = tmp;
    return i + 1;
}

void quick_sort(int left, int right){
    if (left < right){
        int q = partition(left, right);
        quick_sort(left, q - 1);
        // if (q + 1 <= right){
        quick_sort(q + 1, right);
        // }
    }
}

int main(){
    cin >> N;
    for (int i = 0; i < N; i++){
        cin >> A[i].signal >> A[i].value;
    }
    quick_sort(0, N - 1);
    cout << "Not stable" << endl;
    for (int i = 0; i < N; i++){
        cout << A[i].signal << " " << A[i].value << endl;
    }
    return 0;
}