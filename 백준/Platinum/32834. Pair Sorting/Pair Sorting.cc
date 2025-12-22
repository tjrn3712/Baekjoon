#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin>>n;
    vector<int> a(n+1);
    vector<int> b(n+1);
    int j=1;
    for (int i=n;i>0;i--) {
        a[i]=j;
        b[i]=j;
        j++;
    }
    vector<vector<int>>ans;

    for (int i=n;i>0;i--) {
        for (;(a[i]==i)+(b[i]==i)<2;) {
            int have=(a[i]==i)+(b[i]==i),p=-1,s=-1;
            for (int k=i;k>=1;k--){
                if (a[k]==i&&!(have==1&&k==i&&a[i]==i)) {p=k;s=0;break;}
                if (b[k]==i&&!(have==1&&k==i&&b[i]==i)) {p=k;s=1;break;}
            }
            for (int j=p;j<i;j++) {
                int t=(a[j+1]<b[j+1]?0:1);
                if (j+1==i&&have==1) {
                    if (a[i]==i) t=1;
                    else t=0;
                }

                int l=(s?b[j]:a[j]);
                int r=(t?b[j+1]:a[j+1]);
                ans.push_back({j,l,r});

                if (s) {
                    if (t) swap(b[j],b[j+1]);
                    else swap(b[j],a[j+1]);
                } else {
                    if (t) swap(a[j],b[j+1]);
                    else swap(a[j],a[j+1]);
                }
                s=t;
            }
        }
    }
    cout<<ans.size()<<'\n';
    for (auto i:ans)cout<<i[0]<<' '<<i[1]<<' '<<i[2]<<'\n';
}