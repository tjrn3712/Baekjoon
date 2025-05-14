#include <bits/stdc++.h>
using namespace std;

struct Node {
    Node *l,*r,*p;
    int cnt=1;
    int value=0;
    bool inv=false;
};
Node *tree = NULL;
void Rotate(Node* x);
void Splay(Node* x);
void Update(Node* x);
void Lazy(Node* x);
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


void Update (Node *x) {
    x->cnt = 1;
    if (x->l) {
        x->cnt += x->l->cnt;
    }
    if (x->r) {
        x->cnt += x->r->cnt;
    }
}
void Find_kth (int k) {
    Node* x = tree;
    for (;;) {
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
    tree = x = new Node;
    x->l=x->r=x->p=NULL;
    x->cnt = n;
    x->value=0;
    Update(x);
    for (int i=1;i<n;i++) {
        x->r = new Node;
        x->r->p = x;
        x = x->r;
        x->l = x->r = NULL;
        x->cnt = n-i;
        x->value = i;
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
    if (x->inv) {
        Node *t = x->l;
        x->l=x->r;
        x->r=t;
        x->inv = false;
        if (x->l) x->l->inv^=1;
        if (x->r) x->r->inv^=1;
    }
}
void Reverse (int l, int r) {
    Interval(l,r);
    Node* x = tree->r->l;
    x->inv = !x->inv;
    // for (;x;x=x->p) Update(x);
}
void Shift (int l, int r, int k) {
    k = (k%(r-l+1)+r-l+1)%(r-l+1);
    if (!k) return;
    Reverse(l,r);
    Reverse(l,l+k-1);
    Reverse(l+k,r);
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    Node* temp;
    int i,a,x,y,m,r,l;
    int n,q;
    
    cin>>n>>q;
    Init(n);
    for (;q--;) {
        cin>>a>>x>>y;
        m=y-x+1;
        r=(m+1)>>1;
        switch (a) {
        case 1:
        Shift(1,y,m);
        break;
        case 2: 
        Shift(x,n,-m);
        break;
        case 3:
        Interval(x,y);
        temp=tree->r->l;

        vector<int> v;
        function<void(Node*)> dfs = [&](Node* x) {
            Lazy(x);
            if (x->l) dfs(x->l);
            v.push_back(x->value);
            if (x->r) dfs(x->r);
        };
        dfs(temp);

        vector<int> v2(m);
        l=0;
        for (i=0;i<m;i++) {
            if (i&1) v2[i]=v[r++];
            else v2[i]=v[l++];
        }

        i=0;
        function<void(Node*)> dfss = [&](Node* x) {
            Lazy(x);
            if (x->l) dfss(x->l);
            x->value=v2[i++];
            if (x->r) dfss(x->r);
        };
        dfss(temp);

        break;
        }
        /*
        for (i=1;i<=n;i++) {
            Find_kth(i);
            cout<<tree->value<<' ';
        }
        cout<<'\n';
        */
    }

    for (i=1;i<=n;i++) {
        Find_kth(i);
        cout<<tree->value<<' ';
    }
}