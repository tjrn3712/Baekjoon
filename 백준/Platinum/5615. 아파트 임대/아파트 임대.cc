#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using lll = __int128_t;

ll ipow (ll x, ll p, ll mod) {
	ll ret=1,piv=x;
    x%=mod;
	for (;p;p>>=1) {
		if (p&1) ret=(lll)ret*piv%mod;
		piv=(lll)piv*piv%mod;
	}
	return ret;
}
bool isComposite (ll n, ll a, ll d, int s) {
    ll x = ipow(a, d, n);
    if (x==1||x==n-1) return false;
    for (int r=1;r<s;r++) {
        x = (lll)x*x%n;
        if (x==n-1) return false;
    }
    return true;
}
bool MillerRabin (ll n) {
    if (n<2) return false;
    int r=0;
    ll d=n-1;
    for (;~d&1;r++) d>>=1;
    for (int a: {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41}) {
        if (n==a) return true;
        if (isComposite(n, a, d, r)) return false;
    }
    return true;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int n,ans=0;
    ll a;
    for (cin>>n;n--;) {
        cin>>a;
        ans+=MillerRabin(2*a+1);
    }
    cout<<ans;
}