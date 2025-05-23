#include <bits/stdc++.h>
using namespace std;

template <class T> class SegmentTree {
    public:
        int N;
        vector<T> tree;
        T identity;
        function<T(const T&, const T&)> merge;
    
        SegmentTree(const vector<T>& arr, function<T(const T&, const T&)> merge, T identity)
            : identity(identity), merge(merge){
            N = arr.size();
            tree.resize(N<<1,identity);
            for (int i=0;i<N;i++) tree[N+i] = arr[i];
            for (int i=N-1;i>0;i--) tree[i] = merge(tree[i<<1], tree[i<<1|1]);
        }
    
        void update_index(int i, T v) {
            for (tree[i+N]=v;i>1;i>>=1) tree[i>>1] = merge(tree[i], tree[i^1]);
        }

        long long query(int l, int r, int now){
            long long ret = 0;
            for (l+=N,r+=N+1;l<r;l>>=1,r>>=1){
                if (l&1) {
                    ret += lower_bound(tree[l].begin(), tree[l].end(), now) - tree[l].begin();
                    l++;
                }
                if (r&1) {
                    r--;
                    ret += lower_bound(tree[r].begin(), tree[r].end(), now) - tree[r].begin();
                }
            }
            return ret;
        }
    };

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int n,now,l,r,m;cin>>n;
    long long res = 0;
    vector<vector<int>> a;
    a.resize(n);for (int i=0;i<n;i++) a[i].resize(1);
    for (int i=0;i<n;i++) cin>>a[i][0];
    SegmentTree<vector<int>> seg(a, [](vector<int> x, vector<int> y){vector<int> ret;ret.resize((int)x.size()+(int)y.size());merge(x.begin(), x.end(), y.begin(), y.end(), ret.begin());return ret;}, (vector<int>){});

    for (int i=0;i<n;i++) {
        res += seg.query(i, n-1, a[i][0]);
    }

    cout<<res;
}