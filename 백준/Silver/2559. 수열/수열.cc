#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n,k;
    cin>>n>>k;
    int a[n];
    for (int i=0;i<n;i++) cin>>a[i];
    int t=0,ans;
    for (int i=0;i<k;i++) t+=a[i];
    ans=t;
    for (int i=k;i<n;i++) {
        t-=a[i-k];
        t+=a[i];
        ans=max(ans,t);
    }
    cout<<ans;
}