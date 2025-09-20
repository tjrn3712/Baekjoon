#include <bits/stdc++.h>
using namespace std;
using ll=long long;

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

    // 비가환모노이드는 이거
    void update_index2(int i, T v) {
        for (tree[i+=N]=v;i>1;i>>=1) tree[i>>1] = i&1 ? merge(tree[i^1], tree[i]) : merge(tree[i], tree[i^1]);
    }

    // 가환모노이드는 이거
    void update_index(int i, T v) {
        for (tree[i+=N]=v;i>1;i>>=1) tree[i>>1] = merge(tree[i], tree[i^1]);
    }

    // 비가환모노이드는 이거
    T query2(int l, int r) {
        T res_l = identity;
        T res_r = identity;
        for (l+=N,r+=N+1;l<r;l>>=1,r>>=1){
            if (l&1) res_l = merge(res_l, tree[l++]);
            if (r&1) res_r = merge(tree[--r], res_r);
        }
        return merge(res_l, res_r);
    }

    // 가환모노이드는 이거
    T query(int l, int r){
        T ret=identity;
        for (l+=N,r+=N+1;l<r;l>>=1,r>>=1){
            if (l&1) ret = merge(ret, tree[l++]);
            if (r&1) ret = merge(ret, tree[--r]);
        }
        return ret;
    }
};


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    
    ll n,t,mod=1000000007;
    cin>>n;

    vector<SegmentTree<ll>> seg;
    for (int i=0;i<11;i++) seg.push_back(SegmentTree<ll>(vector<ll>(n+1, 0), [](ll a, ll b){return (a+b)%1000000007;}, 0));
    for (int i=0;i<n;i++) {
        cin>>t;
        seg[0].update_index(t, (seg[0].query(t,t)+1)%mod);
        for (int j=1;j<11;j++) {
            seg[j].update_index(t, (seg[j].query(t,t)+seg[j-1].query(1, t-1))%mod);
        }
    }

    cout<<seg[10].query(1, n)%mod;
}