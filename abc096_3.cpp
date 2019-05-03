#include <iostream>
#include <algorithm>
using namespace std;
#define sharp 1
#define dot 0

int H;
int W;
int matrix[52][52] = {};
int main(){
    cin >> H >> W;
    for (int i = 0; i <= H; i++){
        for (int j = 0; j <= W; j++){
            if ((i == 0) || (j == 0)){
                matrix[i][j] = 0;
            }else{
                cin >> matrix[i][j];
            }
        }
    }
    for (int i = 0; i <= H; i++){
        for (int j = 0; j <= W; j++){
            cout << matrix[i][j]<< " ";
        }
        cout << endl;
    }
    return 0;
}