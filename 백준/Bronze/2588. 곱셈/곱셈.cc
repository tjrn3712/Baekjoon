#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int a,b;
    cin>>a>>b;
    cout<<a*(b%10)<<'\n';
    cout<<a*(b%100-b%10)/10<<'\n';
    cout<<a*(b-b%100)/100<<'\n';
    cout<<a*b<<'\n';
}