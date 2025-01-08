#include "hat.h"
#include <vector>
using namespace std;

#include <bits/stdc++.h>
int n;
void init(int N){
    n = N;
}
int call(vector<int> F, vector<int> B, int num){
    if (num == n-1) {
        int temp = 0;
        for (int i=0;i<n;i++) temp^=F[i];
        return temp;
    }
    int temp = 0;
    for (int i=0;i<num;i++) temp^=F[i];
    for (int i=num+1;i<n;i++) temp^=B[i];
    return temp;
}
