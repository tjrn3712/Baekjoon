#include <bits/stdc++.h>
using namespace std;

long long convert(const string &s, int base) {
    long long num = 0;
    for (char c : s)
        num = num * base + (c - '0');
    return num;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    string b, t;
    cin >> b >> t;
    
    unordered_set<long long> nums;
    for (int i = 0; i < b.size(); i++){
        string temp = b;
        temp[i] = (b[i] == '0' ? '1' : '0');
        nums.insert(convert(temp, 2));
    }
    
    for (int i = 0; i < t.size(); i++){
        for (char c = '0'; c <= '2'; c++){
            if (t[i] == c) continue;
            string temp = t;
            temp[i] = c;
            long long val = convert(temp, 3);
            if (nums.find(val) != nums.end()){
                cout << val << "\n";
                return 0;
            }
        }
    }
    
    return 0;
}
