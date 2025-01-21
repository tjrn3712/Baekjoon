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
    int n,m,r,a,b,c,temp;
    cin>>n>>m>>r;
    vector<pii> graph[n+1];
    int d[n+1], item[n+1];
    for (int i=1;i<=n;i++) cin>>item[i];
    for (int i=0;i<r;i++) {
        cin>>a>>b>>c;
        graph[a].push_back({b,c});
        graph[b].push_back({a,c});
    }
    int ans=-1;
    for (int i=1;i<=n;i++) {
        temp=0;
        dijkstra(graph, i, d, n);
        for (int j=1;j<=n;j++) {
            if (d[j]<=m) temp+=item[j];

        }
        ans=max(ans,temp);
    }
    cout<<ans;
}