#include <bits/stdc++.h>
using namespace std;
using ll=long long;

struct d{ll e,c;};
d a[5050];
ll dp[5050][5050];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin>>n;
    for (int i=0;i<n;i++) cin>>a[i].e;
    for (int i=0;i<n;i++) cin>>a[i].c;

    sort(a,a+n,[](d a, d b){return a.c<b.c;});
    for (ll i=n;i>0;i--) {
        for (ll j=0;j<n+1;j++) {
            dp[i][j]=max(dp[i][j],dp[i+1][j]);
            if (j) dp[i][j]=max(dp[i][j],dp[i+1][j-1]+a[i-1].e-a[i-1].c*(j-1));
        }
    }
    ll ans = 0;
    for (int i=0;i<n+1;i++) ans = max(ans,dp[1][i]);
    cout<<ans;
}
