#include <iostream>
#include <algorithm>
using namespace std;
#define MAX_N 100001

int N;
long int X;
long int x[MAX_N];

// bool is_multiple(long int D){
//     // 隣町までの距離がD以上であるかどうか
//     for (int i = 0; i < N; i++){
//         if ((x[i + 1] - x[i]) < D){
//             return false;
//         }
//     }
//     return true;
// }
// long int binary_search(long int left, long int right){
//     if (left == right){
//         return left;
//     }
//     cout <<left <<" " << right << endl;
//     long int D = (left + right) / 2;
//     if (D == left){
//         D = right;
//     }else if (D == right){
//         D = left;
//     }
//     if (is_multiple(D)){
//         // 隣町までがD以上→D以上が答え
//         return binary_search(D, right);
//     }else{
//         // Dより小さい
//         return binary_search(left, D - 1);
//     }
// }

long int D;

long int gcd(long int a, long int b) {
  if(a < b) return gcd(b, a);
  long int r;
  while ((r=a%b)) {
    a = b;
    b = r;
  }
  return b;
}

int main(){
    cin >> N >> X;
    for (int i = 0; i < N; i++){
        cin >> x[i];
    }
    // Xも含めて昇順にする
    x[N] = X;
    sort(x, x + N + 1);
    // cout <<left <<" " << right << endl;
    // D = binary_search(1,x[N] - x[0]);
    long int dis[MAX_N];
    for (int i = 0; i < N; i++){
        dis[i] = x[i + 1] - x[i];
    }
    D = dis[0];
    for (int i  = 1; i < N; i++){
        D = gcd(D, dis[i]);
    }
    cout << D << endl;
    return 0;
}