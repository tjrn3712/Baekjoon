#include <bits/stdc++.h>
using namespace std;

void solve() {
    long double w,h,r;
    cin>>w>>h>>r;

    long double pi=3.141592653589793238;
    cout.precision(20);
    cout<<w*h-pi*r*r/4;

}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t=1;
    //cin>>t;
    for (;t--;) solve();
}