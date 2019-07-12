#include <iostream>
#include <algorithm>
using namespace std;

int N;
long int Y;
int main(){
    cin >> N >> Y;
    bool flag = false;
    for (int x = 0; x <= N; x++){
        for (int y = 0; y <= N - x; y++){
            int z = N - x - y;
            if (10000 * x + 5000 * y + 1000 * z == Y){
                cout << x << " " << y << " " << z << endl;
                flag = true;
                break;
            }
        }
        if (flag){
            break;
        }
    }
    if (!flag){
        cout << -1  << " " << -1 << " " << -1 << endl;
    }
    return 0;
}