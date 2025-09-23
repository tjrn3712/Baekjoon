#include <bits/stdc++.h>
using namespace std;
using ll=long long;

struct LinkCutTree {
    struct Node {
        Node *l=NULL,*r=NULL,*p=NULL;
        ll sz=1,value=0,sum=0,lazy=0;
        bool inv=false;
    };
    LinkCutTree::Node ptr[123456];
    bool isRoot (Node* x) {
        return !x->p||(x!=x->p->l&&x!=x->p->r);
    }
    bool isLeft (Node* x) {
        return x==x->p->l;
    }

    void Update (Node* x) {
        x->sz = 1, x->sum = x->value;
        if (x->l) x->sz+=x->l->sz, x->sum+=x->l->sum;
        if (x->r) x->sz+=x->r->sz, x->sum+=x->r->sum;
    }
    void Update (Node* x, ll v) {
        x->value =  v;
        Update(x);
    }
    void Rotate (Node* x) {
        if (isLeft(x)) {
            if (x->r) x->r->p = x->p;
            x->p->l = x->r;
            x->r = x->p;
        } else {
            if (x->l) x->l->p = x->p;
            x->p->r = x->l;
            x->l = x->p;
        }
        if (!isRoot(x->p)) (isLeft(x->p)?x->p->p->l:x->p->p->r) = x;
        Node* t = x->p;
        x->p = t->p;
        t->p = x;
        Update(t);
        Update(x);
    }
    void Splay (Node* x) {
        for (;!isRoot(x);) {
            Node* p = x->p;
            Node* g = p->p;
            if (!isRoot(p)) Lazy(g);
            Lazy(p);
            Lazy(x);
            if (!isRoot(x->p)) {
                if (isLeft(x)==isLeft(p)) Rotate(p);
                else Rotate(x);
            }
            Rotate(x);
        }
        Lazy(x);
    }
    
    void Lazy (Node* x) {
        if (x->inv) {
            swap(x->l, x->r);
            if (x->l) x->l->inv^=1;
            if (x->r) x->r->inv^=1;
            x->inv^=1;
        }
    }

    void Access(Node* x) {
        Splay(x);
        x->r = NULL;
        for(;x->p;) {
            Splay(x->p);
            x->p->r=x;
            Splay(x);
        }
    }

    void Link (Node* u, Node* v) {
        Access(u);
        Access(v);
        u->l=v;
        v->p=u;
        Update(u);
    }
    void Link (int p, int c) {
        Link(ptr+p, ptr+c);
    }
    void Cut (Node* p) {
        Access(p);
        if (p->l) {
            p->l->p=NULL;
            p->l=NULL;
            Update(p);
        }
    }
    void Cut (int p) {
        Cut(ptr+p);
    }
    Node* FindRoot (Node* x) {
        Access(x);
        for (;x->l;) {
            x=x->l;
            Lazy(x);
        }
        Access(x);
        return x;
    }
    Node* FindParent (Node* x) {
        Access(x);
        if (!x->l) return NULL;
        x=x->l;
        Lazy(x);
        for (;x->l;) {
            x=x->r;
            Lazy(x);
        }
        Access(x);
        return x;
    }
    int Depth (Node* x) {
        Access(x);
        return x->l?x->l->sz:0;
    }
    Node* LCA (Node* u, Node* v) {
        Access(u);
        Access(v);
        Splay(u);
        return u->p?u->p:u;
    }
    int LCA (int u, int v) {
        return LCA(ptr+u, ptr+v)-ptr;
    }
    void MakeRoot (Node* x) {
        Access(x);
        Splay(x);
        x->inv^=1;
    }
    ll VQuery (Node* x, Node* y) {
        Node* t = LCA(x, y);
        ll ret = t->value;

        Access(x);
        Splay(t);
        if (t->r) ret=ret+t->r->sum;
        
        Access(y);
        Splay(t);
        if (t->r) ret=ret+t->r->sum;
        return ret;
    }
    void VUpdate (Node* x, ll v) {
        Splay(x);
        x->value = v;
        Update(x);
    }
    void PUpdate (Node* x, Node* y, ll v) {
        Node* root = FindRoot(x);
        MakeRoot(x);
        Access(y);
        Splay(x);
        x->lazy+=v;
        
        MakeRoot(root);
    }
}tree;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n,m,q,u,v;
    cin>>n>>m;
    LinkCutTree LCT;
    for (;m--;) {
        cin>>q;
        if (q==1) {
            cin>>u>>v;
            LCT.Link(u, v);
        } else if (q==2) {
            cin>>v;
            LCT.Cut(v);
        } else {
            cin>>u>>v;
            cout<<LCT.LCA(u, v)<<'\n';
        }
    }
}