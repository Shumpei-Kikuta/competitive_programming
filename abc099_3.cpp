#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;
#include <vector>
#define MAX_N 100001
#define INF 100001

int main(){
    int N;
    int dp[12][MAX_N];
    vector <int> lists;
    int num = 0;
    cin >> N;
    for (int i = 1; i < 7; i++){
        lists.push_back(pow(6, i));
    }
    for (int i = 1; i < 6; i++){
        lists.push_back(pow(9, i));
    }
    lists.push_back(1);
    sort(lists.begin(), lists.end());

    for (int i = 0; i < 12; i++){
        for (int j = 0; j <= N; j++){
            if (j == 0){
                dp[i][j] = 0;
            }else{
                dp[i][j] = INF;
            }
        }
    }
    for (int i = 0; i < 12; i++){
        for (int j = 0; j <= N; j++){
            if (i == 0){
                dp[i][j] = j;
            }else{
                if (j - lists[i] < 0){
                    dp[i][j] = dp[i - 1][j];
                }else{
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - lists[i]] + 1);
                }
            }
        }
    }
    // for (int i = 0; i < 12; i++){
    //     for (int j = 0; j <= N; j++){
    //         cout << dp[i][j] << " ";
    //     }
    //     cout << endl;
    // }
    cout << dp[11][N] << endl;
    return 0;
}