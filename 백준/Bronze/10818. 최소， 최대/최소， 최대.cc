#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n,m=998244353,M=-998244353,num;
    cin>>n;
    while (n--){
        cin>>num;
        m=min(num,m);
        M=max(num,M);
    }
    cout<<m<<" "<<M;
}