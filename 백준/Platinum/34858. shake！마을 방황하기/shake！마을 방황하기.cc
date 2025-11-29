#include <bits/stdc++.h>
using namespace std;
using ll =long long;

int n,m,q;
vector<pair<int,int>> adj[101010];
int p[20][101010];
int d[101010];
int plen[101010];

void dfs(int u, int v) {
    for (auto [x,y]:adj[u]) {
        if (x==v) continue;
        p[0][x]=u;
        d[x]=d[u]+1;
        plen[x]=y;
        dfs(x,u);
    }
}

int LCA(int u, int v) {
    if (d[u]<d[v]) swap(u,v);
    for (int i=0;i<20;i++) if ((1<<i)&(d[u]-d[v])) u=p[i][u];
    if (u==v) return u;
    for (int i=19;i>-1;i--) if (p[i][u]!=p[i][v]) u=p[i][u],v=p[i][v];
    return p[0][u];
}

int anc(int u, int k) {
    for (int i=0;i<20;i++) if ((1<<i)&k) u=p[i][u];
    return u;
}

pair<int,int> dlehd(int u, int v) {
    if (u!=LCA(u,v)) return {p[0][u],plen[u]};
    return {anc(v,d[v]-d[u]-1),plen[anc(v,d[v]-d[u]-1)]};
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin>>n>>m>>q;
    int a,b,c;
    for (int i=0;i<n-1;i++) {
        cin>>a>>b>>c;
        adj[a].push_back({b,c});
        adj[b].push_back({a,c});
    }

    p[0][1]=0;
    plen[1]=0;
    d[1]=0;
    dfs(1,0);

    for (int i=1;i<20;i++)
    for (int j=1;j<=n;j++)
    p[i][j]=p[i-1][p[i-1][j]];

    vector<pair<ll,ll>> move(q);
    for (int i=0;i<q;i++) {
        cin>>a>>b;
        move[i]={a,b};
    }

    ll ntime=0,nnode=1,to=-1234,remain=0,moving=0,gonode=-1234,gbtlr=0;
    for (int i=0;i<q;i++) {
        ll t=move[i].first;
        for (;ntime<t;) {
            if (moving) {
                if (ntime+remain<=t) {
                    ntime+=remain;
                    nnode=gonode;
                    moving=0;
                    remain=0;
                } else {
                    //도중에끝나면어캄
                    remain-=(t-ntime);
                    ntime=t;
                    break;
                }
            } else {
                if (to<0||nnode==to) {
                    gbtlr+=t-ntime;
                    ntime=t;
                    break;
                } else {
                    auto [ekdma, tlrks] = dlehd(nnode,to);
                    moving=1;
                    gonode=ekdma;
                    remain=tlrks;
                }
            }
        }
        to=move[i].second;
    }
    ll t=m;
    for (;ntime<t;) {
            if (moving) {
                if (ntime+remain<=t) {
                    ntime+=remain;
                    nnode=gonode;
                    moving=0;
                    remain=0;
                } else {
                    //도중에끝나면어캄
                    remain-=(t-ntime);
                    ntime=t;
                    break;
                }
            } else {
                if (to<0||nnode==to) {
                    gbtlr+=t-ntime;
                    ntime=t;
                    break;
                } else {
                    auto [ekdma, tlrks] = dlehd(nnode,to);
                    moving=1;
                    gonode=ekdma;
                    remain=tlrks;
                }
            }
        }

    cout<<gbtlr;
}
//엥터지네아댓다