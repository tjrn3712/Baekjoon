#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    string s;
    getline(cin, s);
    int cnt=1;
    if (s[0] == ' ') cnt--;
    if (s.back()==' ') cnt--;
    for (char i: s){
        if (i == ' ') cnt++;
    }
    cout<<cnt;
}