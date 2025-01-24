#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n,dp[1000]={1,},a[1000],t=1;
    cin>>n;
    for (int i=0;i<n;i++) cin>>a[i];
    for (int i=1;i<n;i++) {
        t=1;
        for (int j=0;j<i;j++) (a[i]>a[j]) ? t=max(t,dp[j]+1) : t=t;
        dp[i]=t;
    }
    t=0;
    for (int i=0;i<n;i++) t=max(t,dp[i]);
    cout<<t;
}