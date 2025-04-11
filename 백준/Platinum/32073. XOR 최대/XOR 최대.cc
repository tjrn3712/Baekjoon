#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    string s;
    cin>>n>>s;

    int idx=n;
    int zeros=0,ones=1;
    for(int i=0;i<n;i++) {
        if (s[i]=='1') {
            idx = i;
            break;
        }
    }

    int ans_len = n-idx;
    if (!ans_len) {
        cout<<0<<'\n';
        return;
    }

    vector<int> ans={1};
    int temp=-1;
    for(int i=idx+1;i<n;i++) {
        if (s[i]=='1') {
            ones++;
            ans.push_back(1);
        }
        if (s[i]=='0'){
            for(;ones>zeros;){
                if (i==n) break;
                if (s[i]=='1') break;
                ans.push_back(1);
                zeros++;
                i++;
            }
            temp = i;
            break;
        }
    }
    //cout<<zeros<<'\n'<<'\n';
    if (temp==-1) {
        for (int i=0;i<(idx?ans_len:(ans_len-1));i++) cout<<1;
        if(!idx)cout<<0;
        cout<<'\n';
        return;
    }
    for (int i=temp-zeros;i<n-zeros;i++) {
        ans.push_back((s[i]-'0')^(s[i+zeros]-'0'));
    }

    for (int i: ans) cout<<i;
    cout<<'\n';
    return;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t=1;
    cin>>t;
    for(;t--;) solve();
}