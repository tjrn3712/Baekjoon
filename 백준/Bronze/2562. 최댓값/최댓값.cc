#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n=9,ans=-32456,temp,cnt;
    for (int i=1;i<=n;i++){
        cin>>temp;
        if (temp > ans){
            ans = temp;
            cnt = i;
        }
    }
    cout<<ans<<"\n";
    cout<<cnt<<"\n";
}