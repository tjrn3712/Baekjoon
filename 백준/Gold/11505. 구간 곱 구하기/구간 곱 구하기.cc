#include <iostream>
using namespace std;
#include <vector>

vector<long long> a;
vector<long long> tree;

void init(vector<long long> &a, vector<long long> &tree, int node, int start, int end) {
    if (start == end) {
        tree[node] = a[start];
    } else {
        init(a, tree, node*2, start, (start+end)/2);
        init(a, tree, node*2+1, (start+end)/2+1, end);
        tree[node] = tree[node*2] * tree[node*2+1] % 1000000007;
    }
}

long long query(vector<long long> &tree, int node, int start, int end, int left, int right) {
    if (left > end || right < start) {
        return 1;
    }
    if (left <= start && end <= right) {
        return tree[node];
    }
    long long lsum = query(tree, node*2, start, (start+end)/2, left, right);
    long long rsum = query(tree, node*2+1, (start+end)/2+1, end, left, right);
    return lsum * rsum % 1000000007;
}

void update(vector<long long> &tree, int node, int start, int end, int index, long long diff) {
    if (index < start || index > end) return;
    if (start == end){
        tree[node] = diff;
        return;
    }
    if (start != end) {
        update(tree,node*2, start, (start+end)/2, index, diff);
        update(tree,node*2+1, (start+end)/2+1, end, index, diff);
        tree[node] = tree[node<<1] * tree[node<<1|1] % 1000000007;
    }
}
void update(vector<long long> &a, vector<long long> &tree, int n, int index, long long val) {
    long long diff = val;
    update(tree, 1, 0, n-1, index, diff);
}

int main()
{   
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n, m, k; cin >> n >> m >> k;
    long long temp, a1, b, c;
    for(int i=0; i<n;i++){
        cin >> temp;
        a.push_back(temp);
    }
    tree.resize(n<<2);
    init(a, tree, 1, 0, n-1);

    for(int i=0; i<m+k;i++){
        cin >> a1 >> b >> c;
        if(a1==1){
            update(a, tree, n, b-1, c);
        }
        if(a1==2){
            cout << query(tree, 1, 0, n-1, b-1, c-1) << '\n';
        }

    }
}