#include <bits/stdc++.h>
using namespace std;
typedef long long ll;


struct Node {
    Node *l,*r,*p;
    int key;
    int cnt;
    ll sum, value, lazy, min=LLONG_MAX, max=LLONG_MIN;
    bool inv=false;
    Node() : l(NULL), r(NULL), p(NULL), key(0), cnt(1), sum(0), value(0), lazy(0), min(LLONG_MAX), max(LLONG_MIN), inv(false) {}
};
Node *ptr[2000002];
struct SplayTree {
    int size=0;
    Node *tree = NULL;

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
};


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n,q,t,l,r,j,x;
    cin>>n>>q;
    SplayTree st;
    st.Init(n);
    for (int i=1;i<=n;i++) {
        st.Find_kth(i);
        st.tree->value=i;
        st.tree->sum=i;
        st.tree->key=i;
    }
    for (int i=0;i<q;i++) {
        cin>>t;
        switch (t) {
            case 1: 
            cin>>l>>r;
            st.Interval(l,r);
            cout<<st.tree->r->l->min<<' '<<st.tree->r->l->max<<' '<<st.tree->r->l->sum<<'\n';
            st.Reverse(l,r);
            break;
            
            case 2:
            cin>>l>>r>>x;
            st.Interval(l,r);
            cout<<st.tree->r->l->min<<' '<<st.tree->r->l->max<<' '<<st.tree->r->l->sum<<'\n';
            st.Shift(l,r,x);
            break;

            case 3:
            cin>>j;
            st.Find_kth(j);
            cout<<st.tree->value<<'\n';
            break;

            case 4:
            cin>>x;
            st.Splay(ptr[x]);
            cout<<(st.tree->l ? st.tree->l->cnt:1)<<'\n';
            break;

            st.Interval(1,n-2);
        }
        /*
        for (int i=1;i<=n;i++) {
            st.Find_kth(i);
            cout<<st.tree->value<<' ';
        }
        cout<<'\n';
        */
    }
    for (int i=1;i<=n;i++) {
        st.Find_kth(i);
        cout<<st.tree->value<<' ';
    }
}