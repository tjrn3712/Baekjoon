#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n;
    cin >> n;
    for (int i=0; i<9; i++){
        cout << n << " * " << i+1 << " = " << n*(i+1) << "\n";
    }
}