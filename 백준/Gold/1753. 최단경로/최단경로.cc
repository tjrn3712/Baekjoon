#include <bits/stdc++.h>
using namespace std;
using pii = pair<int,int>;
const int INF = 998244353;

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

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int v,e,k,u,vv,w;
    cin>>v>>e>>k;
    int d[v+1];
    vector<pii> graph[v+1];
    for (int i=0;i<e;i++){
        cin>>u>>vv>>w;
        graph[u].push_back({vv,w});
    }
    dijkstra(graph, k, d, v);
    for (int i=1;i<=v;i++){
        string ans = (d[i]==INF) ? "INF" : to_string(d[i]);
        cout<< ans<<"\n";
    }
}