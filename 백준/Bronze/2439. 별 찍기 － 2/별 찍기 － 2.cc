#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n;
    cin >> n;
    for (int i=0;i<n;i++) {
        for (int j=0;j<n-1-i;j++) cout << " ";
        for (int j=0;j<i+1;j++) cout << "*";
        cout << "\n";
    }
}