#include <bits/stdc++.h>
using namespace std;

int main(){ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);long long n,m,k,f,b,c;cin>>n>>m>>k;long long r,a[n],s[n<<1]={0,};for(int i=0;i<n;i++)cin>>a[i];for(int i=0;i<n;i++)s[n+i]=a[i];for(int i=n-1;i>0;i--)s[i]=s[i<<1]+s[i<<1|1];for(int i=0;i<m+k;i++){cin>>f;if(--f){cin>>b>>c;r=0;for(b+=n-1,c+=n;b<c;b>>=1,c>>=1){if(b&1)r=r+s[b++];if(c&1) r=r+s[--c];}cout<<r<<'\n';}else{cin>>b>>c;for(s[b=--b+n]=c;b>1;b>>=1)s[b>>1]=s[b]+s[b^1];}}}