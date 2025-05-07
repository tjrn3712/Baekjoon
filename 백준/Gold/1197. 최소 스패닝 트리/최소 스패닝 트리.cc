/*   /\_/\
*   (# ._.)
*   / >  \>
*   CF: a_cedia
*   BOJ: tjrn3712
*/
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
const int INF = 1000000000;
const int mod = 998244353;

// Berlekamp-Massey
ll ipow(ll x, ll p, ll mod){
	ll ret = 1, piv = x;
	while(p){
		if(p & 1) ret = ret * piv % mod;
		piv = piv * piv % mod;
		p >>= 1;
	}
	return ret;
}
vector<int> berlekamp_massey(vector<int> x){
	vector<int> ls, cur;
	int lf, ld;
	for(int i=0; i<x.size(); i++){
		ll t = 0;
		for(int j=0; j<cur.size(); j++){
			t = (t + 1ll * x[i-j-1] * cur[j]) % mod;
		}
		if((t - x[i]) % mod == 0) continue;
		if(cur.empty()){
			cur.resize(i+1);
			lf = i;
			ld = (t - x[i]) % mod;
			continue;
		}
		ll k = -(x[i] - t) * ipow(ld, mod - 2, mod) % mod;
		vector<int> c(i-lf-1);
		c.push_back(k);
		for(auto &j : ls) c.push_back(-j * k % mod);
		if(c.size() < cur.size()) c.resize(cur.size());
		for(int j=0; j<cur.size(); j++){
			c[j] = (c[j] + cur[j]) % mod;
		}
		if(i-lf+(int)ls.size()>=(int)cur.size()){
			tie(ls, lf, ld) = make_tuple(cur, i, (t - x[i]) % mod);
		}
		cur = c;
	}
	for(auto &i : cur) i = (i % mod + mod) % mod;
	return cur;
}
int get_nth(vector<int> rec, vector<int> dp, ll n){
	int m = rec.size();
	vector<int> s(m), t(m);
	s[0] = 1;
	if(m != 1) t[1] = 1;
	else t[0] = rec[0];
	auto mul = [&rec](vector<int> v, vector<int> w){
		int m = v.size();
		vector<int> t(2 * m);
		for(int j=0; j<m; j++){
			for(int k=0; k<m; k++){
				t[j+k] += 1ll * v[j] * w[k] % mod;
				if(t[j+k] >= mod) t[j+k] -= mod;
			}
		}
		for(int j=2*m-1; j>=m; j--){
			for(int k=1; k<=m; k++){
				t[j-k] += 1ll * t[j] * rec[k-1] % mod;
				if(t[j-k] >= mod) t[j-k] -= mod;
			}
		}
		t.resize(m);
		return t;
	};
	while(n){
		if(n & 1) s = mul(s, t);
		t = mul(t, t);
		n >>= 1;
	}
	ll ret = 0;
	for(int i=0; i<m; i++) ret += 1ll * s[i] * dp[i] % mod;
	return ret % mod;
}
int guess_nth_term(vector<int> x, ll n){
	if(n < x.size()) return x[n];
	vector<int> v = berlekamp_massey(x);
	if(v.empty()) return 0;
	return get_nth(v, x, n);
}
struct elem{int x, y, v;}; // A_(x, y) <- v, 0-based. no duplicate please..
vector<int> get_min_poly(int n, vector<elem> M){
	// smallest poly P such that A^i = sum_{j < i} {A^j \times P_j}
	vector<int> rnd1, rnd2;
	mt19937 rng(0x14004);
	auto randint = [&rng](int lb, int ub){
		return uniform_int_distribution<int>(lb, ub)(rng);
	};
	for(int i=0; i<n; i++){
		rnd1.push_back(randint(1, mod - 1));
		rnd2.push_back(randint(1, mod - 1));
	}
	vector<int> gobs;
	for(int i=0; i<2*n+2; i++){
		int tmp = 0;
		for(int j=0; j<n; j++){
			tmp += 1ll * rnd2[j] * rnd1[j] % mod;
			if(tmp >= mod) tmp -= mod;
		}
		gobs.push_back(tmp);
		vector<int> nxt(n);
		for(auto &i : M){
			nxt[i.x] += 1ll * i.v * rnd1[i.y] % mod;
			if(nxt[i.x] >= mod) nxt[i.x] -= mod;
		}
		rnd1 = nxt;
	}
	auto sol = berlekamp_massey(gobs);
	reverse(sol.begin(), sol.end());
	return sol;
}
ll det(int n, vector<elem> M){
	vector<int> rnd;
	mt19937 rng(0x14004);
	auto randint = [&rng](int lb, int ub){
		return uniform_int_distribution<int>(lb, ub)(rng);
	};
	for(int i=0; i<n; i++) rnd.push_back(randint(1, mod - 1));
	for(auto &i : M){
		i.v = 1ll * i.v * rnd[i.y] % mod;
	}
	auto sol = get_min_poly(n, M)[0];
	if(n % 2 == 0) sol = mod - sol;
	for(auto &i : rnd) sol = 1ll * sol * ipow(i, mod - 2, mod) % mod;
	return sol;
}

// 구조체 세그
// SegmentTree<ll>, SegmentTree<vector<ll, ll>>같은 느낌으로 사용
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
        for (tree[i+N]=v;i>1;i>>=1) tree[i>>1] = i&1 ? merge(tree[i^1], tree[i]) : merge(tree[i], tree[i^1]);
    }

    // 가환모노이드는 이거
    void update_index(int i, T v) {
        for (tree[i+N]=v;i>1;i>>=1) tree[i>>1] = merge(tree[i], tree[i^1]);
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

// Not COmplete Code
template <class T> class LazySegmentTree {
    public:
    int N;
    vector<T> tree;
    vector<T> segLen;
    vector<T> lazy;
    vector<bool> isLazy;
    T identity;
    T Uidentity;
    function<T(const T&, const T&)> merge;
    function<T(const T&, const T&)> Umerge;

    LazySegmentTree(const vector<T>& arr, function<T(const T&, const T&)> merge, function<T(const T&, const T&)> Umerge, T identity, T Uidentity)
    : identity(identity), merge(merge), Umerge(Umerge), Uidentity(Uidentity){
        N = arr.size();
        tree.resize(N<<1, identity);
        segLen.resize(N<<1, 1);
        lazy.resize(N<<1, Uidentity);
        isLazy.resize(N, false);
        for (int i=0;i<N;i++) tree[N+i] = arr[i];
        for (int i=N-1;i>0;i--) {
            tree[i] = merge(tree[i<<1], tree[i<<1|1]);
            segLen[i] = segLen[i<<1]+segLen[i<<1|1];
        }
    }

    void update(int l, int r, T v){
        for (l+=N,r+=N;l<r;l>>=1,r>>=1){
            if (l&1) {
                tree[l++] = Umerge(tree[l], v);
                for (int i=l<<1;i>1;i<<=1){
                    if (!isLazy[i]){
                        isLazy[i] = true;
                        lazy[i] = Umerge(lazy[i], v);
                    }
                }
            }
            if (~r&1) {
                tree[r--] = Umerge(tree[r], v);
                for (int i=r<<1;i>1;i<<=1){
                    if (!isLazy[i]){
                        isLazy[i] = true;
                        lazy[i] = Umerge(lazy[i], v);
                    }
                }
            }
        }
    }

    T query(int l, int r){
        int L=l,R=r;
        T res_l = identity;
        T res_r = identity;
        for (l+=N,r+=N;l<r;l>>=1,r>>=1){
            if (l&1) {
                if (isLazy[l]) {
                    tree[l]=Umerge(tree[l], lazy[r]);
                    lazy[l] = Uidentity;
                    isLazy[l] = false;
                }
                res_l = merge(res_l, tree[l++]);
            }
            if (~r&1) {
                if (isLazy[r]) {
                    tree[r]=Umerge(tree[l], lazy[r]);
                    lazy[r] = Uidentity;
                    isLazy[r] = false;
                }
                res_r = merge(tree[r--], res_r);
            }
        }
        
        return merge(res_l, res_r);
    }
};

// pushrelabel에서 쓰는 간선 구조체
template <class T> struct Edge {
    int from, to, index;
    T cap, flow;

    Edge(int from, int to, T cap, T flow, int index): from(from), to(to), cap(cap), flow(flow), index(index) {}
};
// 구조체 push-relabel
// PushRelabel<ll> p(N), p.add_edge(from, to, cap), p.flow(S, T)
template <class T> struct PushRelabel {
    int n;
    vector <vector <Edge <T>>> adj;
    vector <T> excess;
    vector <int> dist, count;
    vector <bool> active;
    vector <vector <int>> B;
    int b;
    queue <int> Q;

    PushRelabel (int n): n(n), adj(n) {}

    void add_edge (int from, int to, int cap) {
        adj[from].push_back(Edge <T>(from, to, cap, 0, adj[to].size()));
        if (from == to) adj[from].back().index++;
        adj[to].push_back(Edge <T>(to, from, 0, 0, adj[from].size()-1));

    }

    void Enqueue (int v) {
        if (!active[v] && excess[v] > 0 && dist[v] < n) {
            active[v] = true;
            B[dist[v]].push_back(v);
            b = max(b, dist[v]);
        }
    }

    void Push (Edge <T> &e) {
        T amt = min(excess[e.from], e.cap - e.flow);
        if (dist[e.from] == dist[e.to] + 1 && amt > T(0)) {
            e.flow += amt;
            adj[e.to][e.index].flow -= amt;
            excess[e.to] += amt;    
            excess[e.from] -= amt;
            Enqueue(e.to);
        }
    }

    void Gap (int k) {
        for (int v = 0; v < n; v++) if (dist[v] >= k) {
            count[dist[v]]--;
            dist[v] = max(dist[v], n);
            count[dist[v]]++;
            Enqueue(v);
        }
    }

    void Relabel (int v) {
        count[dist[v]]--;
        dist[v] = n;
        for (auto e: adj[v]) if (e.cap - e.flow > 0) dist[v] = min(dist[v], dist[e.to] + 1);
        count[dist[v]]++;
        Enqueue(v);
    }

    void Discharge(int v) {
        for (auto &e: adj[v]) {
            if (excess[v] > 0) Push(e);
            else break;
        }

        if (excess[v] > 0) {
            if (count[dist[v]] == 1) Gap(dist[v]); 
            else Relabel(v);
        }
    }

    T flow (int s, int t) {
        dist = vector <int>(n, 0), excess = vector<T>(n, 0), count = vector <int>(n + 1, 0), active = vector <bool>(n, false), B = vector <vector <int>>(n), b = 0;
        
        for (auto &e: adj[s]) excess[s] += e.cap;

        count[0] = n;
        Enqueue(s);
        active[t] = true;
        
        while (b >= 0) {
            if (!B[b].empty()) {
                int v = B[b].back();
                B[b].pop_back();
                active[v] = false;
                Discharge(v);
            } else b--;
        }
        return excess[t];
    }

    T GetMinCut (int s, int t, vector <int> &cut);
};

// 디닉에서 쓰는 간선 구조체
template <class T> struct FlowEdge {
    int v, u;
    T cap, flow = 0;
    FlowEdge(int v, int u, T cap): v(v), u(u), cap(cap) {}
};
// 구조체 디닉
// Dinic<ll> d(N), d.add_edge(from, to, cap), d.flow(S, T)
template <class T> struct Dinic {
    const long long flow_inf = 1e18;
    vector<FlowEdge<ll>> edges;
    vector<vector<ll>> adj;
    ll n, m=0;
    ll s, t;
    vector<ll> level, ptr;
    queue<ll> q;

    Dinic(ll n): n(n) {
        adj.resize(n);
        level.resize(n);
        ptr.resize(n);
    }

    void add_edge(ll v, ll u, long long cap = 1) {
        edges.emplace_back(v, u, cap);
        edges.emplace_back(u, v, 0);
        adj[v].push_back(m);
        adj[u].push_back(m+1);
        m+=2;
    }

    bool bfs(auto t) {
        while (!q.empty()) {
            ll v = q.front();
            q.pop();
            for (int id: adj[v]) {
                if (edges[id].cap == edges[id].flow) continue;
                if (level[edges[id].u] != -1) continue;
                level[edges[id].u] = level[v]+1;
                q.push(edges[id].u);
            }
        }
        return level[t]!=-1;
    }

    long long dfs(ll v, long long pushed, auto t) {
        if (pushed == 0) return 0;
        if (v == t) return pushed;

        for (ll& cid=ptr[v]; cid<(int)adj[v].size(); cid++) {
            ll id = adj[v][cid];
            ll u = edges[id].u;
            if (level[v]+1 != level[u]) continue;

            long long tr = dfs(u, min(pushed, edges[id].cap-edges[id].flow), t);
            if (tr == 0) continue;

            edges[id].flow += tr;
            edges[id^1].flow -= tr;
            return tr;
        }
        return 0;
    }

    long long flow(auto s, auto t) {
        long long f = 0;
        while (true) {
            fill(level.begin(), level.end(), -1);
            level[s] = 0;
            q.push(s);
            if (!bfs(t)) break;

            fill(ptr.begin(), ptr.end(), 0);
            while (long long pushed = dfs(s, flow_inf, t)) f += pushed;
        }
        return f;
    }
};

// 이분매칭
// bipartate_matching(간선벡터, 노드벡터 A, 노트벡터 B, 1 (현재 노드번호 a in A), 방문벡터)
bool bipartate_matching(auto adj, auto A, auto B, auto a, auto visited) {
    visited[a] = true;
    for (auto &b: adj[a]) {
        if (B[b] == -1 or !visited[B[b]] and bipartate_matching(adj, A, B, B[b], visited)) {
            A[a] = b; B[b] = a;
            return true;
        }
    }
    return false;
}

// ccw
// a -> b -> c의 방향성을 알려줌
ll ccw(auto a, auto b, auto c) {
    ll cp = (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]);
    if (cp>0) return -1;
    else if (cp<0) return 1;
    else return 0;
}

// 선분교차판정
// ab와 cd가 교차하는가?
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

// 다각형넓이
// 정점집합 vertices
ld shoelace_area(auto vertices) {
    ll n = (ll)vertices.size();
    ld area = 0;
    for (int i=0; i<n; i++) {
        ll x_i = vertices[i].first, y_i = vertices[i].second;
        ll x_next = vertices[(i+1)%n].first, y_next = vertices[(i+1%n)].second;
        area += (ld)(x_i*y_next) - (ld)(x_next*y_i);
    }
    return abs(area)/(ld)2.0;
}

// Splay Tree, LCT
struct SplayTree {
    struct Node {
        Node *l,*r,*p,*pp;
        int key=0;
        int cnt=1;
        ll sum=0, value=0, lazy=0, min=LLONG_MAX, max=LLONG_MIN;
        bool inv=false;
    };
    int size=0;
    Node *tree = NULL;
    Node *ptr[101010];

    void Rotate (Node *x) {
        Node* p = x->p;
        Node* b = NULL;

        Lazy(p);
        Lazy(x);
        
        if (!p) return;
        if (x==p->l) {
            p->l = b = x->r;
            x->r = p;
        } else {
            p->r = b = x->l;
            x->l = p;
        }

        x->p = p->p;
        p->p = x;

        if (b) b->p = p;
        (x->p?p==x->p->l?x->p->l:x->p->r:tree) = x;

        Update(p);
        Update(x);

        if (p->pp) {
            x->pp=p->pp;
            p->pp=NULL;
        }
    }
    void Splay (Node* x) {
        Lazy(x);
        for (;x->p;) {
            Node* p = x->p;
            Node* g = p->p;

            if (g) {
                if ((x==p->l) == (p==g->l)) Rotate(p);
                else Rotate(x);
            }
            Rotate(x);
        }
    }
    
    void Insert (int key) {
        size++;
        Node* p = tree;
        Node** pp;
        if (!p) {
            Node* x = new Node;
            tree = x;
            x->l=x->r=x->p=NULL;
            x->key = key;
            return;
        }
        for (;1;) {
            if (p->key == key) return;
            if (p->key > key) {
                if (!p->l) {
                    pp = &p->l;
                    break;
                }
                p = p->l;
            } else {
                if (!p->r) {
                    pp = &p->r;
                    break;
                }
                p = p->r;
            }
        }
        Node* x = new Node;
        *pp = x;
        x->l=x->r=NULL;
        x->p = p;
        x->key = key;

        Splay(x);
    }
    bool Find (int key) {
        Node* p = tree;
        if (!p) return false;
        for (;p;) {
            if (p->key==key) break;
            if (p->key > key) {
                if (!p->l) break;
                p = p->l;
            } else {
                if (!p->r) break;
                p = p->r;
            }
        }
        Splay(p);
        return key==p->key;
    }
    void Delete (int key) {
        if (!Find(key)) return;
        size--;
        Node* p = tree;
        if (p->l&&p->r) {
            tree = p->l;
            tree->p = NULL;

            Node* x = tree;
            for (;x->r;) x = x->r;
            x->r = p->r;
            p->r->p = x;
            delete p;
            return;
        }

        if (p->l) {
            tree = p->l;
            tree->p = NULL;
            delete p;
            return;
        }

        if (p->r) {
            tree = p->r;
            tree->p = NULL;
            delete p;
            return;
        }

        delete p;
        tree = NULL;
    }

    void Update (Node *x) {
        x->cnt = 1;
        x->sum = x->value;
        x->min = x->value;
        x->max = x->value;
        if (x->l) {
            Lazy(x->l);
            x->sum += x->l->sum;
            x->cnt += x->l->cnt;
            x->min = min(x->min, x->l->min);
            x->max = max(x->max, x->l->max);
        }
        if (x->r) {
            Lazy(x->r);
            x->sum += x->r->sum;
            x->cnt += x->r->cnt;
            x->min = min(x->min, x->r->min);
            x->max = max(x->max, x->r->max);
        }
    }
    void Find_kth (int k) {
        Node* x = tree;
        for (;1;) {
            for (;x->l && x->l->cnt>k;) {
                x = x->l;
                Lazy(x);
            }
            if (x->l) k -= x->l->cnt;
            if (!k--) break;
            x = x->r;
            Lazy(x);
        }
        Splay(x);
    }
    void Init (int n) {
        n+=2;
        size = n;
        Node* x;
        tree = ptr[0] = x = new Node;
        x->l=x->r=x->p=NULL;
        x->cnt = n;
        x->value=x->sum=0;
        for (int i=1;i<n;i++) {
            ptr[i] = x->r = new Node;
            x->r->p = x;
            x = x->r;
            x->l = x->r = NULL;
            x->cnt = n-i;
            x->sum = x->value = 0;
        }
    }
    void Add1 (int i, ll v) {
        Find_kth(i);
        tree->sum += v;
        tree->value += v;
    }
    void Add2 (int l, int r, ll v) {
        Interval(l,r);
        Node* x = tree->r->l;
        x->sum += x->cnt*v;
        x->lazy += v;
    }
    void Interval (int l, int r) {
        Find_kth(l-1);
        Node *x = tree;
        tree = x->r;
        tree->p = NULL;
        Find_kth(r-l+1);
        x->r = tree;
        tree->p = x;
        tree = x;
    }
    ll Sum (int l, int r) {
        Interval(l, r);
        return tree->r->l->sum;
    }
    void Lazy(Node *x) {
        if (x->lazy) {
            x->value += x->lazy;
            if (x->l) {
                x->l->lazy += x->lazy;
                x->l->sum += x->l->cnt*x->lazy;
            }
            if (x->r) {
                x->r->lazy += x->lazy;
                x->r->sum += x->r->cnt*x->lazy;
            }
            x->lazy = 0;
        }
        if (x->inv) {
            swap(x->l,x->r);
            x->inv = false;
            if (x->l) x->l->inv^=1;
            if (x->r) x->r->inv^=1;
        }

    }
    void Reverse (int l, int r) {
        Interval(l,r);
        Node* x = tree->r->l;
        x->inv = !x->inv;
    }
    void Shift (int l, int r, int k) {
        k = (k%(r-l+1)+r-l+1)%(r-l+1);
        if (!k) return;
        Reverse(l,r);
        Reverse(l,l+k-1);
        Reverse(l+k,r);
    }
    int Index (int value) {
        Splay(ptr[value]);
        return tree->l?tree->l->cnt:0;
    }

    void InsertKth (int k, int v) {
        size++;
        Find_kth(k);
        Node *x = new Node;
        tree->cnt++;
        x->l = tree->l;
        x->r = NULL;
        x->l->p = x;
        x->p = tree;
        tree->l = x;
        x->cnt = x->l->cnt+1;
        x->value = v;
        Update(x);
        Update(x->p);
        Splay(x);
    }
    void DeleteKth (int k) {
        if (size<=2) return;
        size--;
        Find_kth(k);
        Node* p = tree;
        if (p->l&&p->r) {
            int temp = tree->r->cnt;
            tree = p->l;
            tree->p = NULL;

            Node* x = tree;
            for (;x->r;) {
                x->cnt += temp;
                x = x->r;
            }
            x->r = p->r;
            p->r->p = x;
            delete p;
            for (;x->p;) {
                Update(x);
                x = x->p;
            }
            return;
        }

        if (p->l) {
            tree = p->l;
            tree->p = NULL;
            delete p;
            return;
        }

        if (p->r) {
            tree = p->r;
            tree->p = NULL;
            delete p;
            return;
        }

        delete p;
        tree = NULL;
    }
};
// Not Complete Code
struct LinkCutTree : SplayTree{
    void Access (Node* x) {
        Splay(x);
        Update(x);
        if (x->r) {
            x->r->pp=x;
            x->r->p=NULL;
            x->r=NULL;
        }
        Lazy(x);
        for (;x->pp;) {
            Node* y= x->pp;
            Splay(y);
            Update(x);
            if (y->pp) {
                y->r->pp=x;
                y->r->p=NULL;
                y->r=NULL;
            }
            y->r=x;
            x->p=y;
            x->pp=NULL;
            Lazy(x);
            Splay(x);
        }
    }
    
    void Link (Node* p, Node* c) {
        Access(p);
        Access(c);
        p->l=c;
        c->p=p;
    }
    void Cut (Node* p) {
        Access(p);
        if (p->l) {
            p->l->p=NULL;
            p->l=NULL;
        }
    }
    Node* FindRoot (Node* x) {
        Access(x);
        for (;x->l;) x=x->l;
        Access(x);
        return(x);
    }
    void FindParent (Node* x) {}
    Node* LCA (Node* u, Node* v) {
        Access(u);
        Access(v);
        Splay(u);
        return u->pp?u->pp:u;
    }
};

struct UnionFind {
    ll p[444444];
    stack<tuple<int,int,int>> s;
    UnionFind () {
        memset(p, -1, sizeof(p));
    }
    int find (int x) {
        if (p[x]<0) return x;
        return find(p[x]);
    }
    bool uni (int x, int y) {
        x=find(x),y=find(y);
        if (x==y) return 0;
        if (p[x]<p[y]) swap(x,y);
        s.push({x,y,p[x]});
        p[y]+=p[x];
        p[x]=y;
        return 1;
    }
    void rollback () {
        int x = get<0>(s.top()), y = get<1>(s.top()), sz = get<2>(s.top());
        p[y] -= sz;
        p[x] = sz;
        s.pop();
    }
};

struct UnionFindAmortized {
    ll p[10001]={};
    int find (int x) {
        if (!p[x]) return x;
        p[x] = find(p[x]);
        return p[x];
    }
    bool uni (int x, int y) {
        x=find(x),y=find(y);
        if (x==y) return 0;
        p[x]=y; return 1;
    }
};

void solve(){
    int v,e,a,b,c,ans=0;
    cin>>v>>e;
    vector<tuple<int,int,int>> edge;
    for (int i=0;i<e;i++) {
        cin>>a>>b>>c;
        edge.push_back({c,a,b});
    }

    sort(edge.begin(), edge.end(),[](tuple<int,int,int> x, tuple<int,int,int> y)->bool{return get<0>(x)<get<0>(y);});
    UnionFindAmortized UF;
    for (int i=0;i<e;i++) {
        if (UF.uni(get<1>(edge[i]),get<2>(edge[i]))) {
            ans+=get<0>(edge[i]);
        }
    }
    cout<<ans;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    ll t=1;
    //cin>>t;
    while(t--)solve();
}