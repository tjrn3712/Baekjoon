#include <bits/stdc++.h>
using namespace std;
using ll = long long;

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
        Push(x);
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
        Update(x);
    }
    
    void Lazy (Node* x) {
        if (!x) return;
        Update(x, x->value+x->lazy);
        if (x->l) x->l->lazy+=x->lazy;
        if (x->r) x->r->lazy+=x->lazy;
        x->lazy=0;
        if (x->inv) {
            swap(x->l, x->r);
            if (x->l) x->l->inv^=1;
            if (x->r) x->r->inv^=1;
            x->inv^=1;
        }
    }

    void Push (Node* x) {
        static Node* st[303030];
        int top=0;
        Node*y = x;
        st[top++]=y;
        for (;!isRoot(y);st[top++]=y) y=y->p;
        for (;top;) Lazy(st[--top]);
    }
    Node* Access(Node* x) {
        Node* t = NULL;
        for (Node*y = x;y;y=y->p) {
            Splay(y);
            y->r=t;
            Update(y);
            t=y;
        }
        Splay(x);
        return t;
    }

    void Link (Node* u, Node* v) {
        MakeRoot(u);
        if (FindRoot(v)!=u) u->p=v;
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
    Node* FindRoot (int x) {
        return FindRoot(&ptr[x]);
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
    ll VQuery (int x, int y) {
        return VQuery(ptr+x,ptr+y);
    }
    void VUpdate (Node* x, ll v) {
        Splay(x);
        x->value = v;
        Update(x);
    }
    void VUpdate (int i, ll v) {
        VUpdate(ptr+i,v);
    }
    void PUpdate (Node* x, Node* y, ll v) {
        Node* root = FindRoot(x);
        MakeRoot(x);
        Access(y);
        
        // x, y를 chain 하나로 묶어줌요
        Splay(x);
        x->lazy+=v;
        Lazy(x);
        
        MakeRoot(root); // rerooting
    }
    ll PQuery (Node* x, Node* y) {
        Node* l = LCA (x, y);
        ll ret = l->value;
        Access(x);
        Splay(l);

        if (l->r) ret += l->r->sum;
        Access(y);
        Splay(l);

        if (l->r) ret += l->r->sum;
        return ret;
    }

}tree;

int a[30001];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    string q;
    int n,m,x,y;
    cin>>n;
    LinkCutTree LCT;
    for (int i=1;i<=n;i++) cin>>LCT.ptr[i].value;
    cin>>m;
    for (;m--;) {
        cin>>q>>x>>y;
        if (q=="bridge") {
            if (LCT.FindRoot(x)!=LCT.FindRoot(y)) {
                LCT.Link(x,y);
                cout<<"yes"<<'\n';
            }
            else cout<<"no"<<'\n';
        } else if (q=="penguins") {
            LCT.VUpdate(x, y);
        } else {
            if (LCT.FindRoot(x)==LCT.FindRoot(y)) cout<<LCT.VQuery(x,y)<<'\n';
            else cout<<"impossible"<<'\n';
        }
        cout.flush();
    }
}