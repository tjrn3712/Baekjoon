#include <bits/stdc++.h>
using namespace std;

struct Node {
    vector<Node*> edge = {};
    bool visited = false;
    Node *st[20] = {};
    int depth = 0;
    int key = 0;
};

Node *ptr[100001] = {};

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    for (int i=0;i<100001;i++) {
        Node *x = new Node;
        ptr[i] = x;
        x->key = i;
    }

    int n,m,a,b,ii,jj,u,v;
    cin>>n;
    for(int i=0;i<n-1;i++){
        cin>>u>>v;       
        ptr[u]->edge.push_back(ptr[v]);
        ptr[v]->edge.push_back(ptr[u]);
    }

    queue<Node*> q;
    ptr[1]->visited = true;
    q.push(ptr[1]);
    for (;!q.empty();) {
        Node *u = q.front();
        q.pop();
        for (Node* v:u->edge) {
            if (!v->visited) {
                v->visited = true;
                v->st[0] = u;
                v->depth = u->depth+1;
                q.push(v);
            }
        }
    }

    for (int k=1;k<20;k++) {
        for (int i=1;i<=n;i++) {
            Node *temp = ptr[i]->st[k-1];
            ptr[i]->st[k] = temp ? temp->st[k-1]:NULL;
        }
    }

    cin>>m;
    for (;m--;) {
        cin>>ii>>jj;
        Node *u = ptr[ii], *v = ptr[jj];

        if (u->depth<v->depth) {
            swap(u,v);
            swap(ii,jj);
        }

        int d = u->depth-v->depth;
        for (int k=0;k<20;k++) if (d&(1<<k)) u=u->st[k];
        if (u==v) cout<<u->key<<'\n';
        else {
            for (int k=19;k>=0;k--) {
                if (u->st[k]&&u->st[k]!=v->st[k]) {
                    u = u->st[k];
                    v = v->st[k];
                }
            }
            cout<<u->st[0]->key<<'\n';
        }
    }
}
