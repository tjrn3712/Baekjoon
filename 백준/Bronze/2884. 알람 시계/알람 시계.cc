#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int a,b;
    cin>>a>>b;
    cout<<(b>44?a:a?a-1:23)<<' '<<(b+15)%60;
}