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

// 벌캠
const int mod = 998244353;
using lint = long long;
lint ipow(lint x, lint p, ll mod){
	lint ret = 1, piv = x;
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
		lint t = 0;
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
		lint k = -(x[i] - t) * ipow(ld, mod - 2, mod) % mod;
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
int get_nth(vector<int> rec, vector<int> dp, lint n){
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
	lint ret = 0;
	for(int i=0; i<m; i++) ret += 1ll * s[i] * dp[i] % mod;
	return ret % mod;
}
int guess_nth_term(vector<int> x, lint n){
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
lint det(int n, vector<elem> M){
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

// pushrelabel에서 쓰는 간선 구조체
template <class T> struct Edge {
    int from, to, index;
    T cap, flow;

    Edge(int from, int to, T cap, T flow, int index): from(from), to(to), cap(cap), flow(flow), index(index) {}
};
// 구조체 push-relabel, worst: O(V^3)
// PushRelabel p(N, S, T), p.add_edge(from, to, cap), p.flow()
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
        if (from == to) {
            adj[from].back().index++;
        }
        adj[to].push_back(Edge <T>(to, from, 0, 0, adj[from].size() - 1));

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
        for (auto e: adj[v]) if (e.cap - e.flow > 0) {
            dist[v] = min(dist[v], dist[e.to] + 1);
        }
        count[dist[v]]++;
        Enqueue(v);
    }

    void Discharge(int v) {
        for (auto &e: adj[v]) {
            if (excess[v] > 0) {
                Push(e);
            } else {
                break;
            }
        }

        if (excess[v] > 0) {
            if (count[dist[v]] == 1) {
                Gap(dist[v]); 
            } else {
                Relabel(v);
            }
        }
    }

    T flow (int s, int t) {
        dist = vector <int>(n, 0), excess = vector<T>(n, 0), count = vector <int>(n + 1, 0), active = vector <bool>(n, false), B = vector <vector <int>>(n), b = 0;
        
        for (auto &e: adj[s]) {
            excess[s] += e.cap;
        }

        count[0] = n;
        Enqueue(s);
        active[t] = true;
        
        while (b >= 0) {
            if (!B[b].empty()) {
                int v = B[b].back();
                B[b].pop_back();
                active[v] = false;
                Discharge(v);
            } else {
                b--;
            }
        }
        return excess[t];
    }

    T GetMinCut (int s, int t, vector <int> &cut);
};

// 디닉에서 쓰는 간선 구조체
struct FlowEdge {
    int v, u;
    long long cap, flow = 0;
    FlowEdge(int v, int u, long long cap) : v(v), u(u), cap(cap) {}
};
// 구조체 디닉
// Dinic d(N, S, T), d.add_edge(from, to, cap), d.flow()
struct Dinic {
    const long long flow_inf = 1e18;
    vector<FlowEdge> edges;
    vector<vector<ll>> adj;
    ll n, m = 0;
    ll s, t;
    vector<ll> level, ptr;
    queue<ll> q;

    Dinic(ll n, ll s, ll t) : n(n), s(s), t(t) {
        adj.resize(n);
        level.resize(n);
        ptr.resize(n);
    }

    void add_edge(ll v, ll u, long long cap=1) {
        edges.emplace_back(v, u, cap);
        edges.emplace_back(u, v, 0);
        adj[v].push_back(m);
        adj[u].push_back(m + 1);
        m += 2;
    }

    bool bfs() {
        while (!q.empty()) {
            ll v = q.front();
            q.pop();
            for (int id : adj[v]) {
                if (edges[id].cap == edges[id].flow)
                    continue;
                if (level[edges[id].u] != -1)
                    continue;
                level[edges[id].u] = level[v] + 1;
                q.push(edges[id].u);
            }
        }
        return level[t] != -1;
    }

    long long dfs(ll v, long long pushed) {
        if (pushed == 0)
            return 0;
        if (v == t)
            return pushed;
        for (ll& cid = ptr[v]; cid < (int)adj[v].size(); cid++) {
            ll id = adj[v][cid];
            ll u = edges[id].u;
            if (level[v] + 1 != level[u])
                continue;
            long long tr = dfs(u, min(pushed, edges[id].cap - edges[id].flow));
            if (tr == 0)
                continue;
            edges[id].flow += tr;
            edges[id ^ 1].flow -= tr;
            return tr;
        }
        return 0;
    }

    long long flow() {
        long long f = 0;
        while (true) {
            fill(level.begin(), level.end(), -1);
            level[s] = 0;
            q.push(s);
            if (!bfs())
                break;
            fill(ptr.begin(), ptr.end(), 0);
            while (long long pushed = dfs(s, flow_inf)) {
                f += pushed;
            }
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
    return abs(area)/2.0;
}




void solve(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

	int n,p,u,v;
	cin>>n>>p;

	PushRelabel<int> dn(n+1);
	for (int i=1;i<=p;i++){
		cin>>u>>v;
		dn.add_edge(u,v,1);
	}
	cout<<dn.flow(1,2);

    return;
}

int main(){
    ll t=1;
    //cin>>t;
    while(t--)solve();
}