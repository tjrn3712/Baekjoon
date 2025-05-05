#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n,w,i,ans=2147483647;
    cin>>n>>w;
    int a[n][2];
    for (i=0;i<n;i++) cin>>a[i][0];
    for (i=0;i<n;i++) cin>>a[i][1];

    int dp[n+1][3];
    dp[0][0]=0;
    dp[0][1]=1;
    dp[0][2]=1;
    for (i=0;i<n;i++) {
        dp[i+1][0]=(i>0&&a[i-1][0]+a[i][0]<=w&&a[i-1][1]+a[i][1]<=w?a[i][0]+a[i][1]<=w?min({dp[i][1]+1,dp[i][2]+1,dp[i][0]+1,dp[i-1][0]+2}):min({dp[i][1]+1,dp[i][2]+1,dp[i-1][0]+2}):a[i][0]+a[i][1]<=w?min({dp[i][1]+1,dp[i][2]+1,dp[i][0]+1}):min(dp[i][1]+1,dp[i][2]+1));
        dp[i+1][1]=(a[i][0]+a[i+1][0]<=w?min(dp[i+1][0]+1,dp[i][2]+1):dp[i+1][0]+1);
        dp[i+1][2]=(a[i][1]+a[i+1][1]<=w?min(dp[i+1][0]+1,dp[i][1]+1):dp[i+1][0]+1);
    }
    ans=dp[n][0];
    if (n==1) {cout<<ans<<'\n';return;}
    if (a[0][1]+a[n-1][1]<=w) {
        dp[1][0]=1,dp[1][1]=a[0][0]+a[1][0]<=w?1:2,dp[1][2]=2;
        for (i=1;i<n;i++) {
            dp[i+1][0]=(i>0&&a[i-1][0]+a[i][0]<=w&&a[i-1][1]+a[i][1]<=w?a[i][0]+a[i][1]<=w?min({dp[i][1]+1,dp[i][2]+1,dp[i][0]+1,dp[i-1][0]+2}):min({dp[i][1]+1,dp[i][2]+1,dp[i-1][0]+2}):a[i][0]+a[i][1]<=w?min({dp[i][1]+1,dp[i][2]+1,dp[i][0]+1}):min(dp[i][1]+1,dp[i][2]+1));
            dp[i+1][1]=(a[i][0]+a[i+1][0]<=w?min(dp[i+1][0]+1,dp[i][2]+1):dp[i+1][0]+1);
            dp[i+1][2]=(a[i][1]+a[i+1][1]<=w?min(dp[i+1][0]+1,dp[i][1]+1):dp[i+1][0]+1);
        }
        ans=min(ans,dp[n-1][1]+1);
    }
    if (a[0][0]+a[n-1][0]<=w) {
        dp[1][0]=1,dp[1][2]=a[0][1]+a[1][1]<=w?1:2,dp[1][1]=2;
        for (i=1;i<n;i++) {
            dp[i+1][0]=(i>0&&a[i-1][0]+a[i][0]<=w&&a[i-1][1]+a[i][1]<=w?a[i][0]+a[i][1]<=w?min({dp[i][1]+1,dp[i][2]+1,dp[i][0]+1,dp[i-1][0]+2}):min({dp[i][1]+1,dp[i][2]+1,dp[i-1][0]+2}):a[i][0]+a[i][1]<=w?min({dp[i][1]+1,dp[i][2]+1,dp[i][0]+1}):min(dp[i][1]+1,dp[i][2]+1));
            dp[i+1][1]=(a[i][0]+a[i+1][0]<=w?min(dp[i+1][0]+1,dp[i][2]+1):dp[i+1][0]+1);
            dp[i+1][2]=(a[i][1]+a[i+1][1]<=w?min(dp[i+1][0]+1,dp[i][1]+1):dp[i+1][0]+1);
        }
        ans=min(ans,dp[n-1][2]+1);
        if (a[0][1]+a[n-1][1]<=w) {
            dp[1][0]=0,dp[1][1]=dp[1][2]=1;
            for (i=1;i<n;i++) {
                dp[i+1][0]=(i>0&&a[i-1][0]+a[i][0]<=w&&a[i-1][1]+a[i][1]<=w?a[i][0]+a[i][1]<=w?min({dp[i][1]+1,dp[i][2]+1,dp[i][0]+1,dp[i-1][0]+2}):min({dp[i][1]+1,dp[i][2]+1,dp[i-1][0]+2}):a[i][0]+a[i][1]<=w?min({dp[i][1]+1,dp[i][2]+1,dp[i][0]+1}):min(dp[i][1]+1,dp[i][2]+1));
                dp[i+1][1]=(a[i][0]+a[i+1][0]<=w?min(dp[i+1][0]+1,dp[i][2]+1):dp[i+1][0]+1);
                dp[i+1][2]=(a[i][1]+a[i+1][1]<=w?min(dp[i+1][0]+1,dp[i][1]+1):dp[i+1][0]+1);
            }
            ans=min(ans,dp[n-1][0]+2);
        }
    }
    cout<<ans<<'\n';
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int t=1;
    cin>>t;
    for(;t--;)solve();
}