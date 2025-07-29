#include <bits/stdc++.h>
using namespace std;

struct Node {
    int value,cnt=0;
    Node *zero=NULL,*one=NULL;
};

Node* root = new Node();
void insert (int x) {
    Node* cur = root;
    cur->cnt++;
    for (int i=30;i>-1;i--) {
        int b=(x>>i)&1;
        if (b) {
            if (!cur->one) cur->one=new Node();
            cur=cur->one;
        } else {
            if (!cur->zero) cur->zero=new Node();
            cur=cur->zero;
        }
        cur->cnt++;
    }
}
void del (int x) {
    Node* cur = root;
    cur->cnt--;
    for (int i=30;i>-1;i--) {
        int b=(x>>i)&1;
        cur=(b?cur->one:cur->zero);
        cur->cnt--;
    }
}
int MAXXOR (int x) {
    Node* cur = root;
    int ans=0;
    for (int i=30;i>-1;i--) {
        int b=(x>>i)&1;
        if (b) {
            if (cur->zero&&cur->zero->cnt>0) {
                cur=cur->zero;
                ans+=(1<<i);
            } else cur=cur->one;
        } else {
            if (cur->one&&cur->one->cnt>0) {
                cur=cur->one;
                ans+=(1<<i);
            } else cur=cur->zero;
        }
    }
    return ans;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int m,a,x;
    cin>>m;
    insert(0);

    for (;m--;) {
        cin>>a>>x;
        if (a==1) insert(x);
        else if (a==2) del(x);
        else cout<<MAXXOR(x)<<'\n';
    }
}