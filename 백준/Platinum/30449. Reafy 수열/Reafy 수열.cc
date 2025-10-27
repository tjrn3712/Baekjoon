#include <bits/stdc++.h>
using namespace std;

struct v{double a;int b,c;};
int gcdnot1[5001][5001];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n,k;
    cin>>n>>k;
    vector<v> r;
    r.push_back({0,0,1});
    r.push_back({1,1,1});

    for (int i=2;i<=n;i++) {
        r.push_back({1/double(i),1,i});
        for (int j=2;j<i;j++) {
            if (gcdnot1[i][j]) continue;
            if (i%j) {
                r.push_back({j/(double)i,j,i});
                continue;
            }
            for (int k=j;k<i;k+=j) gcdnot1[i][k]=1;
        }
    }
    nth_element(r.begin(),r.begin()+k-1,r.end(),[](v a, v b){return a.a<b.a;});
    cout<<r[k-1].b<<' '<<r[k-1].c;
}