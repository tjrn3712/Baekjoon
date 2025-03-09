/*   /\_/\
*   (# ._.)
*   / >  \>
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
struct Edge {
    int v, rev;
    ll cap;
};
// 구조체 push-relabel, worst: O(V^3)
// PushRelabel p(N, S, T), p.add_edge(from, to, cap), p.flow()
struct PushRelabel {
    int n, s, t;
    vector<vector<Edge>> adj;    // 각 노드의 인접 리스트
    vector<int> height;          // 각 노드의 높이
    vector<int> count;           // 각 높이를 가진 노드의 수 (gap relabeling에 사용)
    vector<ll> excess;           // 각 노드에 쌓인 과잉 유량
    vector<int> cur;             // 각 노드에서 현재 검사 중인 간선의 인덱스
    deque<int> active;         // 과잉 유량이 남은 활성 노드들

    // 생성자: 노드 수 n, source s, sink t (0-indexed)
    PushRelabel(ll n, ll s, ll t) : n(n), s(s), t(t) {
        adj.resize(n);
        height.assign(n, 0);
        count.assign(2 * n, 0);
        excess.assign(n, 0);
        cur.assign(n, 0);
    }
    
    // u에서 v로 용량 cap인 간선을 추가 (역간선은 초기 용량 0)
    void add_edge(ll u, ll v, ll cap) {
        Edge a = {v, (int)adj[v].size(), cap};
        Edge b = {u, (int)adj[u].size(), 0};
        adj[u].push_back(a);
        adj[v].push_back(b);
    }
    
    // push 연산: u에서 인접 노드 v로 가능한 만큼 유량을 밀어냄냄
    void push(int u, int i) {
        Edge &e = adj[u][i];
        int v = e.v;
        ll d = min(excess[u], e.cap);
        if(d > 0 && height[u] == height[v] + 1) {
            e.cap -= d;
            adj[v][e.rev].cap += d;
            excess[u] -= d;
            excess[v] += d;
            if(v != s && v != t && excess[v] == d)
                active.push_back(v);
        }
    }
    
    // relabel 연산: u에서 더 이상 밀어낼 간선이 없을 때 
	// 인접 노드들 중 남은 용량이 있는 최소 높이에 1을 더한 값으로 높이를 갱신함
    void relabel(int u) {
        int d = 2 * n;
        for(auto &e : adj[u]) {
            if(e.cap > 0)
                d = min(d, height[e.v]);
        }
        int old = height[u];
        height[u] = d + 1;
        count[old]--;
        count[height[u]]++;

        // gap relabeling 최적화: 만약 old 높이를 가진 노드가 없으면
        // old보다 큰 높이를 가진 모든 노드의 높이를 n+1로 올려 활성화함함
        if(count[old] == 0)
            for (int i = 0; i < n; i++) {
                if(height[i] > old && height[i] < n) {
                    count[height[i]]--;
                    height[i] = n + 1;
                    count[height[i]]++;
                    if(i != s && i != t && excess[i] > 0)
                        active.push_back(i);
                }
            }
    }
    
    // discharge 연산: u의 남은 과잉 유량을 모두 인접 노드로 밀어냄냄
    void discharge(int u) {
        while(excess[u] > 0) {
            if(cur[u] < (int)adj[u].size()) {
                push(u, cur[u]);
                if(excess[u] == 0) break;
                cur[u]++;
            } else {
                relabel(u);
                cur[u] = 0;
            }
        }
    }
    
    // flow 함수: 초기 preflow를 설정한 후 활성 노드를 처리하면서 최대 유량을 계산
    ll flow() {
        // 초기화: source의 높이를 n으로 설정하고 preflow 전송
        height[s] = n;
        count[0] = n - 1;
        count[n] = 1;
        for(auto &e : adj[s]) {
            if(e.cap > 0) {
                ll f = e.cap;
                e.cap = 0;
                adj[e.v][e.rev].cap += f;
                excess[e.v] += f;
                excess[s] -= f;
                if(e.v != s && e.v != t)
                    active.push_back(e.v);
            }
        }
        // 활성 노드들을 순차적으로 처리(discharge)
        while(!active.empty()) {
            int u = active.front();
            active.pop_front();
            if(u != s && u != t)
                discharge(u);
        }
        // source에서 보낸 유량은 역간선에 저장된 유량의 합으로 계산됨됨
        ll flowVal = 0;
        for(auto &e : adj[s])
            flowVal += adj[e.v][e.rev].cap;
        return flowVal;
    }
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

    void add_edge(ll v, ll u, long long cap) {
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

	ll n,m,k,t,a,job[1001]={};
	//cin>>n>>m>>k;
	cin>>n>>m;
	PushRelabel dn(2003, 0, 2002);
	dn.add_edge(0,2001,n);
	for (int i=1;i<=n;i++){
		cin>>t;
		dn.add_edge(0,i,1);
		dn.add_edge(2001,i,1);
		while(t--) {
			cin>>a;
			job[a]=1;
			dn.add_edge(i,1000+a,1);
		}
	}
	for (int i=0;i<=1000;i++) if (job[i]) dn.add_edge(i+1000,2002,1);
	ll ans = dn.flow();
	cout<<ans;
    return;
}

int main(){
    ll t=1;
    //cin>>t;
    while(t--)solve();
}