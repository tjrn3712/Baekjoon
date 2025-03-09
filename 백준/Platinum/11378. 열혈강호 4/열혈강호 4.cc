/*   /\_/\
*   (# ._.)
*   / >  \>
*/
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;

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

	ll n,m,k,A[1001],B[1001],t,a,ans=0,ans2=0;
	vector<ll> adj[1001];
	fill(A,A+1001,-1);
	fill(B,B+1001,-1);
	cin>>n>>m>>k;

	for (int i=1;i<=n;i++){
		cin>>t;
		while(t--) {
			cin>>a;
			adj[i].push_back(a);
		}
	}
	bool visited[1001] = {false};
	for (int i=1;i<=n;i++){
		fill(visited, visited+1001, false);
		if (bipartate_matching(adj,A,B,i,visited)) ans++;
	}
	bool chk=true,chk2=true;
	while (chk&chk2){
		chk2 = false;
		for (int i=1;i<=n;i++){
			fill(visited, visited+1001, false);
			if (bipartate_matching(adj,A,B,i,visited)) {chk2=true;ans2++;}
			if (ans2==k){chk=false;break;}
		}
	}
	cout<<ans+ans2;
    return;
}

int main(){
    ll t=1;
    //cin>>t;
    while(t--)solve();
}