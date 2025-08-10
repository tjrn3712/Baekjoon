#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int m,q,n,x;
    cin>>m;
    vector<int> f(m);
    for (int i=0;i<m;i++) cin>>f[i];
    int st[31][m];
    for (int j=0;j<m;j++) st[0][j]=j+1;
    for (int j=0;j<m;j++) st[1][j]=f[j];
    for (int i=2;i<31;i++) for (int j=0;j<m;j++) st[i][j]=st[i-1][st[i-1][j]-1];
    
    cin>>q;
    for (;q--;) {
        cin>>n>>x;
        for (int i=0;i<31;i++) if (n&(1<<i)) x=st[i+1][x-1];
        cout<<x<<'\n';
    }
}