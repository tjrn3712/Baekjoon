#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll ipow(ll x, ll p, ll mod=((ll)1<<32)){
	unsigned int ret = 1;
    ll piv = x;
	while(p){
		if(p & 1) ret = ret * piv % mod;
		piv = piv * piv % mod;
		p >>= 1;
	}
	return ret;
}

unsigned int comb[11][11];
struct Node {
    Node *l,*r,*p;
    int key;
    int cnt;
    ll sum, value, lazy, min=LLONG_MAX, max=LLONG_MIN;
    bool inv=false;
    unsigned int ans[11] = {};
    Node() : l(NULL), r(NULL), p(NULL), key(0), cnt(1), sum(0), value(0), lazy(0), min(LLONG_MAX), max(LLONG_MIN), inv(false) {}
};
struct SplayTree {
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
        for (int i=0;i<11;i++) x->ans[i] = x->value*ipow((x->l?x->l->cnt+1:1), i);
        if (x->l) {
            Lazy(x->l);
            x->sum += x->l->sum;
            x->cnt += x->l->cnt;
            x->min = min(x->min, x->l->min);
            x->max = max(x->max, x->l->max);
            for (int i=0;i<11;i++) x->ans[i] += x->l->ans[i];
        }
        if (x->r) {
            Lazy(x->r);
            x->sum += x->r->sum;
            x->cnt += x->r->cnt;
            x->min = min(x->min, x->r->min);
            x->max = max(x->max, x->r->max);
            for (int i=0;i<11;i++) for (int j=0;j<=i;j++) x->ans[i] += x->r->ans[j]*ipow(x->l?x->l->cnt+1:1, i-j)*comb[i][j];
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
    void Add1 (int i, int v) {
        Find_kth(i);
        tree->sum += v;
        tree->value += v;
    }
    void Add2 (int l, int r, int v) {
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
            Node *t = x->l;
            x->l = x->r;
            x->r = t;
            x->inv = false;
            if (x->l) x->l->inv = !x->l->inv;
            if (x->r) x->r->inv = !x->r->inv;
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


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    for (int i=0;i<11;i++) for (int j=0;j<=i;j++) comb[i][j] = (j==0||j==i ? 1:comb[i-1][j-1]+comb[i-1][j]);
    int n,l,r,k,m,a;
    unsigned int p,v,t;
    cin>>n;
    SplayTree ST;
    ST.Init(n);
    for (int i=1;i<=n;i++) {
        cin>>t;
        ST.Find_kth(i);
        ST.tree->value = ST.tree->sum = t;
        for (int j=0;j<11;j++) ST.tree->ans[j] = t;
        ST.Update(ST.tree);
    }

    cin>>m;
    for (int i=0;i<m;i++) {
        cin>>a;
        
        /*
        for (int j=1;j<=ST.size-2;j++) {
            ST.Find_kth(j);
            int k = ST.tree->value;
            cout<<k<<' ';
        }
        cout<<'\n';*/
        
        switch (a) {
            case 1: {
            cin>>p>>v;
            p++;
            ST.InsertKth(p, v);
            break;
            }

            case 2: {
            cin>>p;
            ST.DeleteKth(++p);
            break;
            }

            case 3: {
            cin>>p>>v;
            p++;
            ST.Find_kth(p);
            ST.tree->value = v;
            ST.Update(ST.tree);
            break;
            }

            case 4: {
            cin>>l>>r>>k;
            l++;r++;
            ST.Interval(l,r);
            /*for (int j=0;j<11;j++) {
                cout<<ST.tree->r->l->ans[j]<<' ';
            }*/
            cout<<ST.tree->r->l->ans[k]<<'\n';
            break;
            }
        }
    }
}