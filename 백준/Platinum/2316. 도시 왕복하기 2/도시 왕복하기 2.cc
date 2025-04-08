#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

template <class T> struct FlowEdge {
    int v, u;
    T cap, flow = 0;
    FlowEdge(int v, int u, T cap): v(v), u(u), cap(cap) {}
};
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

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n,p,a,b; cin>>n>>p;
    Dinic<int> d(1002);
    for (int i=3;i<=n;i++) d.add_edge(i*2,i*2+1,1);
    d.add_edge(1*2,1*2+1,998244);
    d.add_edge(2*2,2*2+1,998244);
    for (int i=0;i<p;i++) {
        cin>>a>>b;
        d.add_edge(a*2+1,b*2,1);
        d.add_edge(b*2+1,a*2,1);
    }
    d.add_edge(2*2+1,1*2,998244);
    d.add_edge(0,1*2,998244);
    d.add_edge(2*2+1,1001,998244);

    cout<<d.flow(0,1001);
}

