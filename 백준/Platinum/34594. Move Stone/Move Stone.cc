#include <bits/stdc++.h>
using namespace std;
using ll=long long;

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

Dinic<int> dn(999999);int visited[555555]={};
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n; cin >> n;
    int a[501][501] = {};
    for (int i=0;i<n;i++) {
        for (int j=0;j<n;j++) {
            cin>>a[i][j];
        }
    }

    int s = 999997;
    int e = 999998;
    int cnt = 0;
    vector<int> row(501,0);
    vector<int> col(501,0);
    for (int i=0;i<n;i++) {
        for (int j=0;j<n;j++) {
            if (a[i][j]==0) {
                row[i]++;
                col[j]++;
            } 
        }
    }
    vector<pair<int,int>> z;
    vector<vector<int>> zr(501),zc(501);
    int r[501]={},c[501]={};
    for (int i=0;i<n;i++) {
        for (int j=0;j<n;j++) {
            if (a[i][j]==0) {
                cnt++;
                z.push_back({i,j});
                zr[i].push_back((int)z.size()-1);
                zc[j].push_back((int)z.size()-1);
            }
            if (a[i][j]>1) {
                dn.add_edge(s,i*500+j,a[i][j]-1);

                if (row[i]) {dn.add_edge(i*500+j,260000+i,row[i]);}
                if (col[j]) {dn.add_edge(i*500+j,270000+j,col[j]);}
            }
        }
    }

    for (int i=0;i<501;i++) {
        for(int a:zr[i]) {dn.add_edge(260000+i,300000+a,1);}
        for(int a:zc[i]) {dn.add_edge(270000+i,300000+a,1);}
    }
    for (int i=0;i<z.size();i++) {
        dn.add_edge(300000+i,e,1);
    }
    int ans = 0;
    int f = dn.flow(s,e);

    ans = f + 2 * (cnt - f);
    cout << ans;
}