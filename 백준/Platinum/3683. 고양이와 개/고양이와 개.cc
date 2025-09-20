#include <bits/stdc++.h>
using namespace std;
using ll=long long;

// Edge Struct for Dinic
template <class T> struct FlowEdge {
    int v, u;
    T cap, flow = 0;
    
    FlowEdge(int v, int u, T cap): v(v), u(u), cap(cap) {}
};
// Dinic Structure
// Dinic<ll> d(N), d.add_edge(from, to, cap), d.flow(S, T)
// Code from cp-algorithms: https://cp-algorithms.com/graph/dinic.html
template <class T> struct Dinic {
    const long long flow_inf = 1e18;
    vector<FlowEdge<ll>> edges;
    vector<vector<ll>> adj;
    ll n, m=0;
    ll s, t;
    vector<ll> level, ptr;
    queue<ll> q;

    Dinic(ll n): n(n) {
        adj.resize(n);
        level.resize(n);
        ptr.resize(n);
    }

    void add_edge(ll v, ll u, long long cap = 1) {
        edges.emplace_back(v, u, cap);
        edges.emplace_back(u, v, 0);
        adj[v].push_back(m);
        adj[u].push_back(m+1);
        m+=2;
    }

    bool bfs(auto t) {
        while (!q.empty()) {
            ll v = q.front();
            q.pop();
            for (int id: adj[v]) {
                if (edges[id].cap == edges[id].flow) continue;
                if (level[edges[id].u] != -1) continue;
                level[edges[id].u] = level[v]+1;
                q.push(edges[id].u);
            }
        }
        return level[t]!=-1;
    }

    long long dfs(ll v, long long pushed, auto t) {
        if (pushed == 0) return 0;
        if (v == t) return pushed;

        for (ll& cid=ptr[v]; cid<(int)adj[v].size(); cid++) {
            ll id = adj[v][cid];
            ll u = edges[id].u;
            if (level[v]+1 != level[u]) continue;

            long long tr = dfs(u, min(pushed, edges[id].cap-edges[id].flow), t);
            if (tr == 0) continue;

            edges[id].flow += tr;
            edges[id^1].flow -= tr;
            return tr;
        }
        return 0;
    }

    long long flow(auto s, auto t) {
        long long f = 0;
        while (true) {
            fill(level.begin(), level.end(), -1);
            level[s] = 0;
            q.push(s);
            if (!bfs(t)) break;

            fill(ptr.begin(), ptr.end(), 0);
            while (long long pushed = dfs(s, flow_inf, t)) f += pushed;
        }
        return f;
    }
};

struct Vote {
    int c1=0,c2=0,d1=0,d2=0;
};
int cc,dd,v,l,r;
string a,b;
void solve(){
    cin>>cc>>dd>>v;
    vector<Vote> c, d;
    l=0,r=0;
    for (int i=0;i<v;i++) {
        cin>>a>>b;
        Vote t;
        (a[0]=='C'?t.c1:t.d1) = stoi(a.substr(1));
        (b[0]=='C'?t.c2:t.d2) = stoi(b.substr(1));
        (t.c1?c:d).push_back(t);
        (t.c1?l:r)++;
    }

    Dinic<ll> dn(1000);
    for (int i=0;i<l;i++) dn.add_edge(0, i+1, 1);
    for (int i=0;i<r;i++) dn.add_edge(l+i+1, 999, 1);
    for (int i=0;i<l;i++) for (int j=0;j<r;j++) if ((c[i].c1&&c[i].c1==d[j].c2)||(d[j].d1==c[i].d2&&c[i].d2)) dn.add_edge(i+1, l+j+1, 1);
    cout<<v-dn.flow(0, 999)<<'\n';
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t; cin>>t;
    for(;t--;solve());
}