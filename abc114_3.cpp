#include <iostream>
#include <algorithm>
using namespace std;
#include <string>

long int N;
int num = 0;

bool in_string(string s, string digit){
    for (int i = 0; i < s.length(); i++){
        if (s[i] == digit[0]){
            return true;
        }
    }
    return false;
}

void dfs(string s){
    if (in_string(s, "3") && in_string(s, "5") && in_string(s, "7")){
        if (stol(s) <= N){
            num += 1;
        }
    }
    if (s.length() < 9){
        dfs(s + "3");
        dfs(s + "5");
        dfs(s + "7");
    }
}

int main(){
    cin >> N;
    dfs("");
    cout << num << endl;

    return 0;
}