/*   /\_/\
*   (# ._.)
*   / >  \>
*/
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;

template <typename T>
class SegmentTree {
public:
    int N;
    vector<T> tree;
    T identity;
    function<T(const T&, const T&)> merge;

    SegmentTree(const vector<T>& arr, function<T(const T&, const T&)> merge, T identity)
        : identity(identity), merge(merge) {
        N = arr.size();
        tree.resize(N<<1, identity);
        for (int j=0;j<N;j++) tree[N+j] = arr[j];
        for (int j=N-1;j>0;j--) tree[j] = merge(tree[j<<1], tree[j<<1|1]);
    }

    void update_index(int index, T value) {
        index += N;
        tree[index] = value;
        while (index>1) {
            tree[index>>1] = merge(tree[index], tree[index^1]);
            index >>= 1;
        }
    }
    
    T query(int left, int right) {
        left += N;
        right += N+1;
        T res_left = identity;
        T res_right = identity;
        while (left<right) {
            if (left&1) res_left = merge(res_left, tree[left++]);
            if (right&1) res_right = merge(tree[--right], res_right);
            left>>=1;right>>=1;
        }
        return merge(res_left, res_right);
    }
};

bool bipartate_matching(vector<vector<ll>> adj, vector<ll> A, vector<ll> B, ll a, vector<ll> visited) {
    visited[a] = true;
    for (auto &b: adj[a]) {
        if (B[b] == -1 or !visited[B[b]] and bipartate_matching(adj, A, B, B[b], visited)) {
            A[a] = b; B[b] = a;
            return true;
        }
    }
    return false;
}

ll ccw(auto a, auto b, auto c) {
    ll cp = (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]);
    if (cp>0) return -1;
    else if (cp<0) return 1;
    else return 0;
}

bool line_seg_intersection(auto a, auto b, auto c, auto d) {
    ll ab = ccw(a,b,c)*ccw(a,b,d);
    ll cd = ccw(c,d,a)*ccw(c,d,b);
    if (!ab and !cd) {
        if (a > b) swap(a, b);
        if (c > d) swap(c, d);
        return !(b<c and d<a);
    }
    return ab<=0 and cd<=0;
}

ld shoelace_area(auto vertices) {
    ll n = (ll)vertices.size();
    ld area = 0;
    for (int i=0; i<n; i++) {
        ll x_i = vertices[i].first, y_i = vertices[i].second;
        ll x_next = vertices[(i+1)%n].first, y_next = vertices[(i+1%n)].second;
        area += (ld)(x_i*y_next) - (ld)(x_next*y_i);
    }
    return abs(area)/2.0;
}

void solve(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll a,b;
    cin>>a>>b;
    cout<<lcm(a,b)<<'\n';
    return;
}

int main(){
    ll t=1;
    cin>>t;
    while(t--)solve();
}