#include <iostream>
#include <algorithm>
using namespace std;
#define sharp 1
#define dot 0

int H;
int W;
int matrix[52][52] = {};

bool dfs(int now_y, int now_x){
    // 隣がいればfalse, いなければtrue
    for (int i = -1; i <= 1; i++){
        for (int j = -1; j <= 1; j++){
            if ((i + j) % 2 != 0){
                if (matrix[now_y + i][now_x + j] == sharp){
                    return false;
                }
            }
        }
    }
    return true;
}

bool is_solve(){
    for (int i = 1; i <= H; i++){
        for (int j = 1; j <= W; j++){
            if (matrix[i][j] == sharp){
                if (dfs(i, j)){
                    // 隣がいなかったとき
                    return false;
                }
            }
        }
    }
    return true;
}

int main(){
    cin >> H >> W;
    for (int i = 0; i <= H; i++){
        for (int j = 0; j <= W; j++){
            if ((i == 0) || (j == 0)){
                matrix[i][j] = 0;
            }else{
                char str;
                cin >> str;
                if (str == '#'){
                    matrix[i][j] = sharp;
                }else{
                    matrix[i][j] = dot;
                }
            }
        }
    }
    if (is_solve()){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }
    
    return 0;
}