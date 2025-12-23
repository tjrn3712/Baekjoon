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

struct P{int a,i;};
void solve() {
    int n,a,b;
    cin>>n>>a>>b;
    a--;b--;
    vector<int> p(n);
    for (int i=0;i<n;i++) cin>>p[i];

    vector<P> mn(n);
    vector<P> mx(n);

    for (int i=0;i<n;i++) {
        mn[i].a=i-p[i];
        mn[i].i=i;
        mx[i].a=i+p[i];
        mx[i].i=i;
    }

    //SegmentTree<int> minseg(mn,[](int x, int y){return min(x,y);},998244353);
    //SegmentTree<int> maxseg(mx,[](int x, int y){return max(x,y);},-998244353);

    SegmentTree<P> minseg(mn,[](P x, P y){return x.a>y.a?P(y.a,y.i):P(x.a,x.i);},{998244353,0});
    SegmentTree<P> maxseg(mx,[](P x, P y){return x.a>y.a?P(x.a,x.i):P(y.a,y.i);},{-998244353,0});
    //p[i]반지름으로, 왼쪽은 max 오른쪽은 min가져가야댐

    queue<int> q;
    vector<int> dist(n,-1);
    dist[a]=0;
    for (q.push(a);!q.empty();) {
        int u=q.front();
        q.pop();
        for (int i=max(u-p[u],0);i<u;i++) {
            P x=maxseg.query(max(u-p[u],0),u-1);
            if (x.a<u) break;
            if (dist[x.i]==-1) {
            dist[x.i]=dist[u]+1;
            q.push(x.i);
            }
            maxseg.update_index(x.i,{-998244353,x.i});
        }
        for (int i=u+1;i<=min(u+p[u],n-1);i++) {
            P x=minseg.query(u+1,min(u+p[u],n-1));
            if (x.a>u) break;
            if (dist[x.i]==-1) {
            dist[x.i]=dist[u]+1;
            q.push(x.i);
            }
            minseg.update_index(x.i,{998244353,x.i});
        }
    }
    cout<<dist[b]<<'\n';
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
     
    int t=1;
    cin>>t;
    for (;t--;solve());
}