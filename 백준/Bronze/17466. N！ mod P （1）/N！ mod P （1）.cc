#include <bits/stdc++.h>
using namespace std;
using ll=long long;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    ll n,p;
    cin>>n>>p;
    ll ans=1;
    for (int i=2;i<=n;i++) {
        ans*=i;
        ans%=p;
    }
    cout<<ans;
}