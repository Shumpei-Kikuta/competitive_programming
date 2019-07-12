#include <iostream>
#include <algorithm>
using namespace std;

long int X, Y;
int main(){
    cin >> X >> Y;
    long int cnt = 1;
    long int prev = X;
    while(true){
        long int next = 2 * prev;
        if (next > Y){
            break;
        }
        cnt ++;
        prev = next;
    }
    cout << cnt << endl;
    return 0;
}