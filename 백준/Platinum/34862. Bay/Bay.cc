#include <bits/stdc++.h>
using namespace std;
using ll=long long;

int n,S,N,u,v,r,c,ans=0,ansu=0,ansv=0;
pair<int,int> rc(int x) {
    return {(x-1)/n,(x-1)%n};
}

ll weight(int u, int v, vector<int>& col, vector<int>& height) {
    int dx=col[v]-col[u];
    return (dx?1ll*height[u]*dx:0);
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>n>>S;
    N=n*n;

    vector<pair<int,int>> edges;
    for (int i=0;i<N-1;i++) {
        cin>>u>>v;
        edges.push_back({u,v});
    }

    vector<vector<int>> graph(N+1);
    for (auto [x,y]:edges) {
        graph[x].push_back(y);
        graph[y].push_back(x);
    }

    vector<vector<bool>> ro(n, vector<bool>(n-1,0));
    vector<vector<bool>> co(n-1, vector<bool>(n,0));
    for (auto [x,y]:edges) {
        auto [r1,c1]=rc(x);
        auto [r2,c2]=rc(y);

        if (r1==r2) {
            r=r1;
            c=min(c1,c2);
            ro[r][c]=1;
        } else {
            c=c1;
            r=min(r1,r2);
            co[r][c]=1;
        }
    }

    vector<int> row(N+1);
    vector<int> col(N+1);
    vector<int> height(N+1);

    for (int i=1;i<=N;i++) {
        r=rc(i).first,c=rc(i).second;
        row[i]=r;
        col[i]=c;
        height[i]=(n-1)-r;
    }

    vector<ll> h(N+1,0);
    vector<bool> visited(N+1,0);

    stack<int> st;
    h[1]=0;
    visited[1]=1;

    for (st.push(1);!st.empty();) {
        int x = st.top();
        st.pop();
        for (int i:graph[x]) {
            if (visited[i]) continue;
            visited[i]=1;
            h[i]=h[x]+weight(x,i,col,height);
            st.push(i);
        }
    }

    bool ok=false;
    for (r=0;r<n;r++) {
        for (c=0;c<n;c++) {
            u=r*n+c+1;
            if (c<n-1) {
                v=u+1;
                if (!ro[r][c]) {
                    if (llabs(h[v]-h[u]+weight(v,u,col,height))==S) {
                        ans++;
                        if (!ok||u<ansu||(u==ansu&&v<ansv)) {
                            ok=1;
                            ansu=u;
                            ansv=v;
                        }
                    }
                }
            }

            if (r<n-1) {
                v=u+n;
                if (!co[r][c]) {
                    if (llabs(h[v]-h[u]+weight(v,u,col,height))==S) {
                        ans++;
                        if (!ok||u<ansu||(u==ansu&&v<ansv)) {
                            ok=1;
                            ansu=u;
                            ansv=v;
                        }
                    }
                }
            }
        }
    }
    cout<<ans<<'\n';
    cout<<ansu<<' '<<ansv;
}