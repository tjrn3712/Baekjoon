#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int a,b,c;
    cin>>a>>b>>c;
    string s = to_string(a*b*c);
    for (char i:"0123456789") {
        if (i =='\0') break;
        cout<<count(s.begin(), s.end(), i)<<"\n";
    }
}