#include <iostream>
#include <algorithm>
using namespace std;

int N;
int X[101], Y[101];
long int H[101];
int Cx, Cy;
long int ans;

void check(){
    for (int i = 0; i <= 100; i++){
        for (int j = 0; j <= 100; j++){
            bool flag = true;
            int num = 0;
            for (int k = 0; k < N; k++){
                if (H[k] == 0){
                    continue;
                }else{
                    if ((num == 0) || (((ans == abs(X[k] - i) + abs(Y[k] - j) + H[k])) && (ans >= 1))){
                        ans = abs(X[k] - i) + abs(Y[k] - j) + H[k];
                        num += 1;
                    }else{
                        flag = false;
                        break;
                    }
                }
            }
            if (flag){
                Cx = i;
                Cy = j;
                return;
            }
        }
    }
    return;
}


int main(){
    cin >> N;
    for (int i = 0; i < N; i ++){
        cin >> X[i] >> Y[i] >> H[i];
    }
    check();
    cout << Cx << " " << Cy << " " << ans << endl;

    return 0;
}