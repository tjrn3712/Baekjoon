#include <bits/stdc++.h>
using namespace std;
#define int long long

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int d,p,q,ans=9998244353,m,t;
    cin>>d>>p>>q;
    if (p<q) swap(p,q);
    m=d/p;
    for (int i=0;i<=min(m,q)+1;i++) ans=d>i*p?min(ans,i*p+(d-(i*p)+q-1)/q*q):min(ans,i*p);
    cout<<ans;
}