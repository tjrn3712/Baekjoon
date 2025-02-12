#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n,t,ans=0; cin>>n;
    priority_queue<int> pq;
    for(int i=0;i<n;i++) {
        cin>>t;
        pq.push(-t);
    }
    for(int i=0;i<n-1;i++){
        t=ans;
        ans-=pq.top();pq.pop();
        ans-=pq.top();pq.pop();
        pq.push(-(ans-t));
    }
    cout<<ans;
}