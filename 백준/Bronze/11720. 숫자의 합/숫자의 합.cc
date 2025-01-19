#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n,a=0;
    char b;
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>b;
        a+=int(b);
        a-=48;
    }
    cout<<a;
}