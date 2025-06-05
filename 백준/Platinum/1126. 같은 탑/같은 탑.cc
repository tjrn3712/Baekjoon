#include <bits/stdc++.h>
using namespace std;

int dp[50][1000001];
int a[50];
void solve(){
    int n,ans=0;
    cin >> n;
    for (int i=0;i<n;i++) cin>>a[i];
    memset(dp, -1, sizeof(dp));
    dp[0][0] = 0;
    dp[0][a[0]] = 0;
/*
    for (int i=1;i<n;i++){
        for (int j=0;j<500001;j++){
            dp[i][j] = max(dp[i-1][j], max(dp[i-1][j+a[i]], dp[i-1][abs(j-a[i])]+min(a[i], j)));
        }
    }
*/
    for (int i=1;i<n;i++) {
        for (int j=0;j<=500000;j++) {
            if (dp[i-1][j]<0) continue;
            dp[i][j] = max(dp[i][j], dp[i-1][j]);
            if (j+a[i]<=500000) dp[i][j+a[i]] = max(dp[i][j+a[i]], dp[i-1][j]);
            if (j>=a[i]) dp[i][j-a[i]] = max(dp[i][j-a[i]], dp[i-1][j]+a[i]);
            else dp[i][a[i]-j] = max(dp[i][a[i]-j], dp[i-1][j]+j);
        }
    }
    ans = dp[n-1][0];
    cout<<(ans>0 ? ans:-1);
    return;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int t=1;
    //cin>>t;
    while(t--)solve();
}