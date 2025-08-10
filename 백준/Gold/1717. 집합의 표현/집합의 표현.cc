#include <bits/stdc++.h>
using namespace std;

int p[4444444]={};
int find (int x) {
    if (p[x]==-1) return x;
    p[x] = find(p[x]);
    return p[x];
}
bool uni (int x, int y) {
    x=find(x),y=find(y);
    if (x==y) return 0;
    p[x]=y; return 1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    memset(p,-1,sizeof(p));
    int m,n,a,b,q;
    cin>>n>>m;
    for (;m--;) {
        cin>>q>>a>>b;
        if (q) cout<<(find(a)==find(b)?"YES":"NO")<<'\n';
        else uni(a,b);
    }
}