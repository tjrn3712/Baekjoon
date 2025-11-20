#include <bits/stdc++.h>
using namespace std;

int dx[8]={2,1,-1,-2,-2,-1,1,2};
int dy[8]={1,2,2,1,-1,-2,-2,-1};

struct pos{int x,y;};
int n,x,y,best,now,tx,ty,nx,ny,m;
int possibleMove (vector<vector<bool>> &visited, int x, int y) {
    int cnt=0,nx,ny;
    for (int i=0;i<8;i++) {
        nx=x+dx[i],ny=y+dy[i];
        if (nx>0&&nx<=n&&ny>0&&ny<=n&&!visited[nx][ny]) cnt++;
    }
    return cnt;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    bool ok=1;

    cin>>n>>x>>y;
    int ox=x,oy=y;
    vector<vector<bool>> visited(n+1,vector<bool>(n+1,0));
    vector<pos> ans;

    visited[x][y]=1;
    ans.push_back({x,y});
    for (int i=0;i<n*n-1;i++) {
        best=9,tx=-1,ty=-1;
        vector<pos> c;
        for (int j=0;j<8;j++) {
            nx=x+dx[j],ny=y+dy[j];
            if (!(nx>0&&nx<=n&&ny>0&&ny<=n)||visited[nx][ny]) continue;
            m=possibleMove(visited,nx,ny);
            if (m<best) best=m,tx=nx,ty=ny;
        }
        for (int j=0;j<8;j++) {
            nx=x+dx[j],ny=y+dy[j];
            if (!(nx>0&&nx<=n&&ny>0&&ny<=n)||visited[nx][ny]) continue;
            m=possibleMove(visited,nx,ny);
            if (m==best) c.push_back({nx,ny});
        }
        if (tx==-1) {
            ok=0;
            break;
        }

        best=998244353;
        for (pos p:c) {
            now=min(abs(1-p.x),abs(n-p.x))+min(abs(1-p.y),abs(n-p.y));
            if (now<best) best=now,tx=p.x,ty=p.y;
        }
        x=tx,y=ty;
        visited[x][y]=1;
        ans.push_back({x,y});
    }
    if (!ok) {
        ok=1;
        x=ox,y=oy;
        vector<vector<bool>> visited(n+1,vector<bool>(n+1,0));
        ans.clear();

        visited[x][y]=1;
        ans.push_back({x,y});

        for (int i=0;i<n*n-1;i++) {
            best=9,tx=-1,ty=-1;
            vector<pos> c;
            for (int j=0;j<8;j++) {
                nx=x+dx[j],ny=y+dy[j];
                if (!(nx>0&&nx<=n&&ny>0&&ny<=n)||visited[nx][ny]) continue;
                m=possibleMove(visited,nx,ny);
                if (m<best) best=m,tx=nx,ty=ny;
            }
            for (int j=0;j<8;j++) {
                nx=x+dx[j],ny=y+dy[j];
                if (!(nx>0&&nx<=n&&ny>0&&ny<=n)||visited[nx][ny]) continue;
                m=possibleMove(visited,nx,ny);
                if (m==best) c.push_back({nx,ny});
            }
            if (tx==-1) {
                ok=0;
                break;
            }

            best=998244353;
            for (pos p:c) {
                now=min(min(abs(1-p.x),abs(n-p.x)),min(abs(1-p.y),abs(n-p.y)));
                if (now<best) best=now,tx=p.x,ty=p.y;
            }
            x=tx,y=ty;
            visited[x][y]=1;
            ans.push_back({x,y});
        }
    }
    if (!ok) {
            if (!ok) {
        ok=1;
        x=ox,y=oy;
        vector<vector<bool>> visited(n+1,vector<bool>(n+1,0));
        ans.clear();

        visited[x][y]=1;
        ans.push_back({x,y});

        for (int i=0;i<n*n-1;i++) {
            best=9,tx=-1,ty=-1;
            vector<pos> c;
            for (int j=0;j<8;j++) {
                nx=x+dx[j],ny=y+dy[j];
                if (!(nx>0&&nx<=n&&ny>0&&ny<=n)||visited[nx][ny]) continue;
                m=possibleMove(visited,nx,ny);
                if (m<best) best=m,tx=nx,ty=ny;
            }
            for (int j=0;j<8;j++) {
                nx=x+dx[j],ny=y+dy[j];
                if (!(nx>0&&nx<=n&&ny>0&&ny<=n)||visited[nx][ny]) continue;
                m=possibleMove(visited,nx,ny);
                if (m==best) c.push_back({nx,ny});
            }
            if (tx==-1) {
                ok=0;
                break;
            }

            best=-1;
            for (pos p:c) {
                now=abs(n/2-p.x)+abs(n/2-p.y);
                if (now<best) best=now,tx=p.x,ty=p.y;
            }
            x=tx,y=ty;
            visited[x][y]=1;
            ans.push_back({x,y});
        }
    }
    }
    if (!ok) {
        cout<<"-1 -1";
        return 0;
    }
    for (pos i:ans) cout<<i.x<<' '<<i.y<<'\n';
}
