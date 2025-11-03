#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n,k,c,a,b,d;

    cin>>n>>k>>c;
    vector<int> last_day(n+1,0);
    vector<int> need(n+1,0);
    vector<vector<vector<int>>> adj(k+1,vector<vector<int>>(n+1));
    for (int i=0;i<c;i++) {
        cin>>a>>b>>d;
        last_day[a] = max(last_day[a],d);
        last_day[b] = max(last_day[b],d);
        adj[d][a].push_back(b);
        adj[d][b].push_back(a);
    }

    for (int i=1;i<=n;i++) {
        if (last_day[i]>1) continue;
        vector<vector<int>> temp(k+1);
        vector<vector<bool>> visited(k+1,vector<bool>(n+1,0));

        visited[0][i]=1;
        temp[0].push_back(i);

        for (int t=0;t<k;t++) {
            d=t+1;
            for (int x: temp[t]) {
                for (int y: adj[d][x]) {
                    if (last_day[y]<=d+1&&!visited[d][y]) {
                        temp[d].push_back(y);
                        visited[d][y]=1;
                    }
                }
            }
        }
        for (int i=1;i<=n;i++) {
            if (visited[k][i]) need[i]=1;
        }
    }
    vector<int> ans;
    for (int i=1;i<=n;i++) {
        if (need[i]) ans.push_back(i);
    }
    cout<<ans.size();
    for (int i: ans) cout<<'\n'<<i;
}