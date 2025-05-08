#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

struct SplayTree {
    struct Node {
        Node *l,*r,*p,*pp;
        int key=0;
        int cnt=1;
        ll sum=0, value=0, lazy=0, min=LLONG_MAX, max=LLONG_MIN;
        bool inv=false;
        char c;
    };
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
        tree = x = new Node;
        x->l=x->r=x->p=NULL;
        x->cnt = n;
        x->value=x->sum=0;
        for (int i=1;i<n;i++) {
            x->r = new Node;
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
    /*
    int Index (int value) {
        Splay(ptr[value]);
        return tree->l?tree->l->cnt:0;
    }
    */
    void InsertKth (int k, char v) {
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
        x->c = v;
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
    
    int n,m,q,a,i,l,r;
    char c;
    cin>>n>>q;
    SplayTree S;
    S.Init(n);
    string s;
    cin>>s;
    
    for (int i=1;i<=n;i++) {
        S.Find_kth(i);
        S.tree->c=s[i-1];
    }
    for (int ii=0;ii<q;ii++) {
        cin>>a;
        switch (a) {
            case 1:
            cin>>c>>i;
            S.InsertKth(i, c);
            break;

            case 2:
            cin>>l>>r;
            for (int j=0;j<r-l+1;j++) {
                S.Find_kth(l);
                cout<<S.tree->c;
                S.DeleteKth(l);
            }
            cout<<'\n';
            break;
        }
    }
}