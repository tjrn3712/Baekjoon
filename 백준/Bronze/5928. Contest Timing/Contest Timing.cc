#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int d,h,m;cin>>d>>h>>m;
    if ((d<11) or (d==11 and h<11) or (d==11 and h==11 and m<11)) {
        cout<<-1;
        exit(0);
    };
    d-=11;h-=11;m-=11;
    cout<<d*1440+h*60+m;
}