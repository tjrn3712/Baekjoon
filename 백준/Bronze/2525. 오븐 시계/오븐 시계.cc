#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int a,b,c;
    cin>>a>>b>>c;
    cout<<(a+(b+c)/60)%24<<' '<<(b+c)%60;
}