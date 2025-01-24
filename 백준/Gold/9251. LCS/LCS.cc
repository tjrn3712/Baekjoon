#include <bits/stdc++.h>
using namespace std;

int dp[1234][1234];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    string a,b;

    cin>>a>>b;
    for (int i=0;i<=(int)a.size();i++) dp[i][0]=0;
    for (int i=0;i<=(int)b.size();i++) dp[0][i]=0;
    for (int i=1;i<=(int)a.size();i++) for (int j=1;j<=(int)b.size();j++) (a[i-1]==b[j-1]) ? dp[i][j]=dp[i-1][j-1]+1 : dp[i][j]=max(dp[i][j-1], dp[i-1][j]);
    cout<<dp[(int)a.size()][(int)b.size()]; 
}