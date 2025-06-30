#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int x,y;
    cin>>x>>y;
    cout<<(x>0?y>0?1:4:y>0?2:3);
}