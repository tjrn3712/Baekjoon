#include <bits/stdc++.h>
using namespace std;
using ll = long long;


ll n,A,B,l,r,i,j,aa,sz,q,rm,qq,rr,mn;
void solve() {
    cin>>n>>A>>B;

    vector<ll> a(n+1);
    for (int i=1;i<=n;++i) cin>>a[i];
    sort(a.begin()+1,a.end(),greater<ll>());

    if (B==n) {
        cout<<a[1]+A<<"\n";
        return;
    }

    vector<ll> dp((n-1)/B+1,0);
    vector<ll> ps(n+1,0);
    for (int i=1;i<=n;i++) ps[i]=ps[i-1]+a[i];

    l=1;
    for (r=1;r<=n;r+=B) {
        for (;a[l]*1ll*(r-l+1)-(ps[r]-ps[l-1])>A*1ll*(((l-1)/B)+1);l++);
        if (l==r) dp[0]=max(dp[0], a[r]+A*1ll*(((r-1)/B)+1));
        else {
            i = (r-1)/B-(((l-1)/B)+1);
            if (i>=0&&i<=(n-1)/B) {
                sz=r-l+1;
                q=(A*((l-1)/B+1)+ps[r]-ps[l-1])/sz;
                rm=(A*((l-1)/B+1)+ps[r]-ps[l-1])%sz;
                dp[i]=max(dp[i],q*(sz-((B-l%B)%B+1))+max(rm-((B-l%B)%B+1),0ll)+A);
            }
        }
    }

    a[0] = a[1]+A+1;
    aa = A;
    vector<ll> ps2(n+1,0);
    i=n;
    for (;i>0;i--) {
        mn=min(a[i-1]-a[i],aa/(n-i+1));
        a[i]+=mn;
        ps2[i]=mn;
        aa-=mn*(n-i+1);

        if (a[i-1]>a[i]) {
            j=i;
            for (;aa;aa--,j++) a[j]++;
            i++;
            for (;i<=n;i++) {
                a[i]+=ps2[i-1];
                ps2[i]+=ps2[i-1];
            }
            break;
        }
    }

    for (i=1;i<=n-B;i++) a[i]=a[i+B];
    for (i=n-B+1;i<=n;i++)a[i]=0;

    fill(ps.begin(), ps.end(), 0);
    for (i=1;i<=n;i++) ps[i]=ps[i-1]+a[i];
    l=1;
    for (r=1;r<=n;r+=B) {
        for (;a[l]*1ll*(r-l+1)-(ps[r]-ps[l-1])>A*1ll*(((l-1)/B)+1);l++);
        if (l==r) dp[0]=max(dp[0],a[r]+A*1ll*(((r-1)/B)+1));
        else {
            i=(r-1)/B-(((l-1)/B)+1);
            if (i>=0&&i<=(n-1)/B) {
                sz=r-l+1;
                q=(A*((l-1)/B+1)+ps[r]-ps[l-1])/sz;
                rm=(A*((l-1)/B+1)+ps[r]-ps[l-1])%sz;
                dp[i]=max(dp[i],q*(sz-((B-l%B)%B+1))+max(rm-((B-l%B)%B+1),0ll)+A);
            }
        }
    }

    for (i=(n-1)/B;i>0;i--) {
        dp[i]=max(dp[i],(A-1)/B*1ll*min(n-B,i*B+1)+A);
        qq=dp[i]/(1ll*i*B+1);
        rr=dp[i]%(1ll*i*B+1);
        dp[i-1]=max(dp[i-1],qq*(1ll*(i-1)*B+1)+max(0ll,rr-B)+A);
    }

    cout<<dp[0]<<"\n";
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t=1;
    for (cin>>t;t--;) solve();
}