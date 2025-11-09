#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n,u,v,k;
    cin>>n;
    vector<vector<pair<int,int>>> graph(n+1,vector<pair<int,int>>(0));
    for (int i=0;i<n-1;i++) {
        cin>>u>>v>>k;
        graph[u].push_back({v,k});
        graph[v].push_back({u,k});
    }
    vector<bool> visited(n+1,0);
    function<pair<int,int>(int, int)> dfs = [&](int x, int d) -> pair<int,int> {
        pair<int,int> ret = {x,d};
        if (!visited[x]) {
            visited[x]=1;
            for (auto a:graph[x]) {
                if (!visited[a.first]) {
                    pair<int,int> v = dfs(a.first, a.second+d);
                    if (ret.second<v.second) ret=v;
                }
            }   
        }
        return ret;
    };
    
    pair<int,int> p = dfs(1,0);
    visited.assign(n+1,0);
    cout<<dfs(p.first,0).second;
}