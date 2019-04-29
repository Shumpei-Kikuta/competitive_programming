#include <iostream>
#include <algorithm>
using namespace std;
#define MAX 100001

int N, K;
long int h[MAX];

int main(){
    cin >> N >> K;
    for (int i = 0; i < N; i++){
        cin >> h[i];
    }
    // sort
    sort(h, h + N);
    // for (int i = 0; i < N; i++){
    //     cout << h[i];
    // }

    int left = 0;
    int right = K -1 ;
    long int distance = 10000000001;
    while(right < N){
        if (distance > h[right] - h[left]){
            distance = h[right] - h[left];
        }
        right ++;
        left ++;
    }
    cout << distance << endl;
    return 0;
}