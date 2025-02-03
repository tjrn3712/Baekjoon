#include <bits/stdc++.h>
#define fastio cin.tie(0)->sync_with_stdio(0)
using namespace std;

constexpr int inf = 1 << 30;

int main() {
	fastio;
	int n; cin >> n;
	vector v(n, 0);
	for (int i = 0; i < n; i++) cin >> v[i];
	int sum = 0, mn = 0, ret = -inf;
	for (int i = 0; i < n; i++) {
		sum += v[i];
		ret = max(ret, sum - mn);
		mn = min(mn, sum);
	}
	cout << ret << '\n';
}