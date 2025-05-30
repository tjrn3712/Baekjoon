#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef __int128 lll;

ll g (ll x, ll y, ll mod) {return (lll)x*y%mod;}
ll llgcd(ll a, ll b) {
    if (a<b) swap(a,b);
    ll r;
    for (;b;) {
        r = a%b;
        a=b;
        b=r;
    }
    return a;
}
ll ipow (ll x, ll p, ll mod) {
	lll ret=1,piv=x%mod;
    x%=mod;
	for (;p;p>>=1) {
		if (p&1) ret=g(ret,piv,mod);
		piv=g(piv,piv,mod);
	}
	return (ll)ret;
}
bool MillerRabin (ll n, ll a) {
    if(n%a==0) return 0;
	ll d = n-1;
	for (;;d>>=1) {
		ll tmp = ipow(a, d, n);
		if(d&1) return (tmp!=1&& tmp!=n-1);
		else if(tmp==n-1) return 0;
	}
}
bool isPrime (ll n) {
    for (ll i:{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37}) {
		if (n==i) return 1;
		if (n>40&&MillerRabin(n,i)) return 0;
	}
	if (n<=40) return 0;
	return 1;
}
ll f (ll x, ll n, ll c) {
    return ((lll)x*x%n+c)%n;
}
mt19937_64 rng(time(NULL));
uniform_int_distribution<ll> r{};
void PollardRho (ll n, vector<ll> &v) {
    if (n==1) return;
    if (~n&1) {v.push_back(2);PollardRho(n/2,v);return;}
    if (isPrime(n)) {v.push_back(n);return;}
    ll x,y,c;
    for (;;) {
        x = r(rng)%(n-2)+2;
        y = x;
        c = r(rng)%(n-1)+1;
        do {
            x = f(x,n,c);
            y = f(f(y,n,c),n,c);
        } while (llgcd(llabs(x-y),n)==1);
        if (x!=y) break;
    }
    ll a = llgcd(llabs(x-y),n);
    PollardRho(a,v);
    PollardRho(n/a,v);
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    ll n;
    cin>>n;
    vector<ll> ans;
    PollardRho(n, ans);
    sort(ans.begin(),ans.end());
    for (ll a: ans) {
        cout<<a<<'\n';
    }
}