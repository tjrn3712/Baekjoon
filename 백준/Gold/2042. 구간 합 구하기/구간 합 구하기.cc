#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

struct Node {
    Node *l,*r,*p;
    int key;
    int cnt;
    ll sum, value;
};
struct SplayTree {
    int size=0;
    Node *tree = NULL;

    void Rotate (Node *x) {
        Node* p = x->p;
        Node* b = NULL;

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

        /////Update
        Update(p);
        Update(x);
    }
    void Splay (Node* x) {
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
        if (x->l) {
            x->sum += x->l->sum;
            x->cnt += x->l->cnt;
        }
        if (x->r) {
            x->sum += x->r->sum;
            x->cnt += x->r->cnt;
        }
    }

    void Find_kth (int k) {
        Node* x = tree;
        for (;1;x=x->r) {
            for (;x->l && x->l->cnt>k;) x = x->l;
            if (x->l) k -= x->l->cnt;
            if (!k--) break;
        }
        Splay(x);
    }

    void Init (int n) {
        n++;
        Node* x;
        tree = x = new Node;
        x->l=x->r=x->p=NULL;
        x->cnt = n;
        x->value=x->sum=0;

        for (int i=1;i<=n;i++) {
            x->r = new Node;
            x->r->p = x;
            x = x->r;
            x->l = x->r = NULL;
            x->cnt = n-i;
            x->sum = x->value = 0;
        }
    }

    void Add (int i, int v) {
        Find_kth(i);
        tree->sum += v;
        tree->value += v;
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
};


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n,m,k,a,b;
    ll t,c;
    cin>>n>>m>>k;
    SplayTree st;
    st.Init(n);
    for (int i=1;i<=n;i++) {
        cin>>t;
        st.Find_kth(i);
        st.tree->sum = t;
        st.tree->value = t;
    }

    for (int i=0;i<m+k;i++) {
        cin>>a>>b>>c;
        if (a&1) {
            st.Find_kth(b);
            st.tree->sum += c-st.tree->value;
            st.tree->value = c;
        } else {
            cout<<st.Sum(b,c)<<'\n';
        }
    }
}