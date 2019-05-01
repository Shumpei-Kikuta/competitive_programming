#include <iostream>
#include <algorithm>
using namespace std;
#define MAX_N 100001

int N;
int K;
long int x[MAX_N];

int main(){
    cin >> N >> K;
    bool flag = true;
    for (int i = 0; i < N; i++){
        long int element;
        cin >> element;
        // if ((element > 0) && (flag)){
            // flag = false;
            // x[i] = 0;
            // i ++;
        // }
        x[i] = element;
    }
    // for (int i = 0; i <= N; i++){
    //     cout << x[i] << endl;
    // }
    int left = 0;
    int right = K - 1;
    long int distance = 10000000001;
    if (x[0] >= 0){
        distance = x[K - 1];
    }
    else if (x[N - 1] <= 0){
        distance = - x[N - K];
    }
    else{
        while (right < N){
            if ((x[right] >= 0) && (x[left] <= 0)){
                distance = min(min(2 * x[right] - x[left], x[right] - 2 * x[left]), distance);
            }
            left ++;
            right ++;
        }
    }
    cout << distance << endl;

    return 0;
}