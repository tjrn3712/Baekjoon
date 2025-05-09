#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

struct SplayTree {
    struct Node {
        Node *l,*r,*p,*pp=NULL;
        int key=0;
        ll cnt=1;
        ll left=0,right=0,ans=0;
        ll sum=0, value=0, lazy=0, min=-1, max=2;
        bool inv=false;
    };
    int size=0;
    Node *tree = NULL;

    void Rotate (Node *x) {
        Node* p = x->p;
        Node* b = NULL;

        if (!p) return;
        Lazy(p);
        Lazy(x);

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
        x->ans=x->left=x->right=x->value;
        if (x->l&&x->r) {
            x->left=x->l->left+(x->l->left==x->l->cnt&&x->value?x->r->left+1:0);
            x->right=x->r->right+(x->r->right==x->r->cnt&&x->value?x->l->right+1:0);
            x->ans=max(x->r->ans,x->l->ans);
            if (x->value) x->ans=max(x->ans,x->l->right+x->r->left+1);
            x->ans=max({x->ans,x->left,x->right,x->l->right+x->value,x->r->left+x->value});
        } else if (x->l) {
            x->left=(x->l->left==x->l->cnt?x->l->cnt+x->value:x->l->left);
            x->right=(x->value?x->l->right+1:0);
            x->ans=max({x->l->ans,x->value,x->l->right+x->value,x->left,x->right});
        } else if (x->r) {
            x->left=(x->value?x->r->left+1:0);
            x->right=(x->r->right==x->r->cnt?x->r->cnt+x->value:x->r->right);
            x->ans=max({x->r->ans,x->value,x->r->left+x->value,x->left,x->right});
        }
    }
    void Find_kth (int k) {
        Node* x = tree;
        Lazy(x);
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
        size = n;
        Node* x;
        tree = x = new Node;
        x->l=x->r=x->p=NULL;
        x->cnt = n;
        x->value=x->sum=0;
        Update(x);
        for (int i=1;i<n;i++) {
            x->r = new Node;
            x->r->p = x;
            x = x->r;
            x->l = x->r = NULL;
            x->cnt = n-i;
            x->sum = x->value = 0;
            Update(x);
        }
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
            swap(x->left,x->right);
            x->inv = false;
            if (x->l) x->l->inv^=1;
            if (x->r) x->r->inv^=1;
        }
    }
    void Reverse (int l, int r) {
        Node* x = tree;
        if (l==0&&r==size-1) x = tree;
        else if (l==0) {
            Find_kth(r+1);
            x = tree->l;
        } else if (r==size-1) {
            Find_kth(l-1);
            x = tree->r;
        } else {
            Interval(l,r);
            x = tree->r->l;
        }
        x->inv^=1;
        for (;x;) {
            Update(x);
            x=x->p;
        }
    }
};


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n,a,m,l,r;
    cin>>n;
    SplayTree s;
    s.Init(n);
    for (int i=0;i<n;i++) {
        cin>>a;
        s.Find_kth(i);
        s.tree->value=a;
        s.Update(s.tree);
    }

    cin>>m;
    for (int i=0;i<m;i++) {
        cin>>a;
        if (a==1) {
            cin>>l>>r;
            s.Reverse(l-1,r-1);
        }
        else {
            cin>>l>>r;
            if (l==1&&r==n) {
                s.Find_kth(n/2);
                cout<<s.tree->ans<<'\n';
            } else if (l==1) {
                s.Find_kth(r);
                cout<<s.tree->l->ans<<'\n';
            } else if (r==n) {
                s.Find_kth(l-2);
                cout<<s.tree->r->ans<<'\n';
            } else {
                s.Interval(l-1,r-1);
                cout<<s.tree->r->l->ans<<'\n';
            }
        }
    }
}