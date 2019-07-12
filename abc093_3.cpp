#include <iostream>
#include <algorithm>
using namespace std;

int A, B, C;
int lists[3];

int main(){
    cin >> A >> B >> C;
    lists[0] = A; lists[1]  = B; lists[2] = C;
    sort(lists, lists + 3);
    int max_value = lists[2];
    int middle_value = lists[1];
    int min_value = lists[0];
    int D = middle_value - min_value;
    int E = max_value - min_value;
    if (D % 2 == 0){
        cout << E - D + D / 2 << endl;
    }else{
        cout << E - D + D / 2 + 2 << endl;
    }
    return 0;
}