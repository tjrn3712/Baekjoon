#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int n, m;
    cin >> n >> m;
    
    vector<int> temp(n);
    for(auto &x : temp) cin >> x;
    
    vector<pair<int, int>> arr(n);
    for(int i = 0; i < n; i++) {
        arr[i] = {temp[i], i};
    }
    
    sort(arr.begin(), arr.end());
    
    while(m--){
        int i, j, k;
        cin >> i >> j >> k;
        i--; j--;
        
        int cnt = 0;
        for(int ind = 0; ind < n; ind++){
            if(arr[ind].second >= i && arr[ind].second <= j){
                cnt++;
                if(cnt == k){
                    cout << arr[ind].first << "\n";
                    break;
                }
            }
        }
    }
    
    return 0;
}
