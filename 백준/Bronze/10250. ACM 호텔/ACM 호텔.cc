#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t,H,W,N;
    cin>>t;
    while(t--){
        cin>>H>>W>>N;
        if(N%H) cout<<(N%H)*100+N/H+1<<"\n";
        else cout<<H*100+N/H<<"\n";
    }
}