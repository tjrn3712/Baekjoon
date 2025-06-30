#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int a;
    cin>>a;
    cout<<(a>89?"A":a>79?"B":a>69?"C":a>59?"D":"F");
}