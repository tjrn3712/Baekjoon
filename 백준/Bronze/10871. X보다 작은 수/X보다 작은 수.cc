#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n, x;
    cin>>n>>x;
    for (int i; i<n; i++){
        int temp;
        cin >> temp;
        if (temp<x) cout << temp << " ";
    }   
}