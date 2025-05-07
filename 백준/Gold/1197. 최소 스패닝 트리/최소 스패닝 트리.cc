#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

struct UnionFindAmortized {
    ll p[10001]={};
    int find (int x) {
        if (!p[x]) return x;
        p[x] = find(p[x]);
        return p[x];
    }
    bool uni (int x, int y) {
        x=find(x),y=find(y);
        if (x==y) return 0;
        p[x]=y; return 1;
    }
};

void solve(){
    int v,e,a,b,c,ans=0;
    cin>>v>>e;
    vector<tuple<int,int,int>> edge;
    for (int i=0;i<e;i++) {
        cin>>a>>b>>c;
        edge.push_back({c,a,b});
    }

    sort(edge.begin(), edge.end(),[](tuple<int,int,int> x, tuple<int,int,int> y)->bool{return get<0>(x)<get<0>(y);});
    UnionFindAmortized UF;
    for (int i=0;i<e;i++) {
        if (UF.uni(get<1>(edge[i]),get<2>(edge[i]))) {
            ans+=get<0>(edge[i]);
        }
    }
    cout<<ans;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    ll t=1;
    //cin>>t;
    while(t--)solve();
}