#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n,m,psum[100001]={0,},a,b;
    cin>>n>>m;
    for (int i=1;i<=n;i++) {
        cin>>a;
        psum[i] = psum[i-1]+a;
    }
    for (int i=0;i<m;i++){
        cin>>a>>b;
        cout<<psum[b]-psum[a-1]<<"\n";
    }
}