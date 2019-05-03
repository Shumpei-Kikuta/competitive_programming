#include <iostream>
#include <algorithm>
using namespace std;

int A, B, C;
int X, Y;
long int cost = 0;
int main(){
    cin >> A >> B >> C >> X >> Y;
    if ((A + B) <= 2 * C){
        cost = A * X + B * Y;
    }
    else{
        int min_num = min(X, Y);
        X -= min_num;
        Y -= min_num;
        cost += 2 * min_num * C;
        if (X == 0){
            cost += min(2 * C * Y, B * Y);
        }
        else{
            cost += min(2 * C * X, A * X);
        }
    }
    cout << cost << endl;
    return 0;
}