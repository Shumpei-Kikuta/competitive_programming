#include <iostream>
#include <algorithm>
using namespace std;
#include <string>

string S;
long int K;

int main(){
    cin >> S >> K;
    int i = 0;
    while(true){
        if (S[i] != '1'){
            break;
        }
        if (i == K -1){
            break;
        }
        i++;
    }
    cout << S[i] << endl;
    return 0;
}