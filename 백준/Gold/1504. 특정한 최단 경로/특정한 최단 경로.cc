#include <bits/stdc++.h>
using namespace std;
using pii = pair<int,int>;
const int INF = 99824435;

void dijkstra (vector<pii> graph[], int s, int d[], int v){
    for (int i=1; i<=v; i++) d[i]=INF;
    priority_queue<pii, vector<pii>, greater<>> pq;
    pq.push({d[s]=0, s});
    while (pq.size()){
        auto [cdist, u] = pq.top(); pq.pop();
        if (d[u]!=cdist) continue;
        for (auto[v, cost]: graph[u]) {
            if (d[v]<=d[u]+cost) continue;
            pq.push ({d[v]=d[u]+cost, v});
            }
    }
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int v,e,u,vv,w,v1,v2;
    cin>>v>>e;
    int d1[v+1];
    int d2[v+1];
    vector<pii> graph[v+1];
    for (int i=0;i<e;i++){
        cin>>u>>vv>>w;
        graph[u].push_back({vv,w});
        graph[vv].push_back({u, w});
    }
    cin>>v1>>v2;
    dijkstra(graph, v1, d1, v);
    dijkstra(graph, v2, d2, v);
    int ans1 = d1[1]+d1[v2]+d2[v];
    int ans2 = d2[1]+d2[v1]+d1[v];
    if (min(ans1,ans2) < INF)cout << min(ans1, ans2);
    else cout << -1;
}