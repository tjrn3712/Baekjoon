#include <bits/stdc++.h>
using namespace std;
const int INF=99824435;

int bfs(int grid[], bool visited[], queue<int>& q){
    int temp=0;
    while (int s=q.size()){
        for (int i=0;i<s;i++){
            int now = q.front(); q.pop();
            if (now<=50000 and not visited[2*now]){
                if (grid[2*now]>=INF) return grid[now];
                q.push(2*now);
                grid[2*now]=grid[now];
                visited[2*now]=true;
            } 
            if (now>0 and not visited[now-1]){
                if (grid[now-1]>=INF) return grid[now]+1;
                q.push(now-1);
                grid[now-1]=grid[now]+1;
                visited[now-1]=true;
            }
            if (now<100000 and not visited[now+1]){
                if (grid[now+1]>=INF) return grid[now]+1;
                q.push(now+1);
                grid[now+1]=grid[now]+1;
                visited[now+1]=true;
            }

        }
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n,k;
    cin>>n>>k;
    if (n==k){
        cout<<0;
        exit(0);
    }
    int grid[100001]={0,};
    grid[n]=0;grid[k]=INF;
    bool visited[100001]={false,};
    visited[n]=true;
    queue<int> q;
    q.push(n);
    cout<<bfs(grid, visited, q);
}