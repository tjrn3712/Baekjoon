#include<bits/stdc++.h>
using namespace std;using w=int;
struct T{struct N{N*l,*r,*p,*q;w c,L,R,A,v,f;}*t;w n;
void Z(N*x){if(x->f){swap(x->l,x->r);swap(x->L,x->R);x->f=0;if(x->l)x->l->f^=1;if(x->r)x->r->f^=1;}}
void U(N*x){x->c=1;if(x->l){Z(x->l);x->c+=x->l->c;}if(x->r){Z(x->r);x->c+=x->r->c;}x->A=x->L=x->R=x->v;if(x->l&&x->r){x->L=x->l->L+(x->l->L==x->l->c&&x->v?x->r->L+1:0);x->R=x->r->R+(x->r->R==x->r->c&&x->v?x->l->R+1:0);x->A=max(x->r->A,x->l->A);if(x->v)x->A=max(x->A,x->l->R+x->r->L+1);x->A=max({x->A,x->L,x->R,x->l->R+x->v,x->r->L+x->v});}else if(x->l){x->L=(x->l->L==x->l->c?x->l->c+x->v:x->l->L);x->R=(x->v?x->l->R+1:0);x->A=max({x->l->A,x->v,x->l->R+x->v,x->L,x->R});}else if(x->r){x->L=(x->v?x->r->L+1:0);x->R=(x->r->R==x->r->c?x->r->c+x->v:x->r->R);x->A=max({x->r->A,x->v,x->r->L+x->v,x->L,x->R});}}
void R(N*x){N*p=x->p,*b;if(!p)return;Z(p);Z(x);if(x==p->l)p->l=b=x->r,x->r=p;else p->r=b=x->l,x->l=p;x->p=p->p,p->p=x;if(b)b->p=p;(x->p?p==x->p->l?x->p->l:x->p->r:t)=x;U(p);U(x);}
void S(N*x){Z(x);for(;x->p;){N*p=x->p,*g=p->p;if(g){if((x==p->l)==(p==g->l))R(p);else R(x);}R(x);}}
void K(w k){N*x=t;Z(x);for(;;){while(x->l&&x->l->c>k)x=x->l,Z(x);if(x->l)k-=x->l->c;if(!k--)break;x=x->r,Z(x);}S(x);}
void G(w m){n=m;N*x;t=x=new N;x->l=x->r=x->p=NULL;x->c=m;U(x);while(--m){x->r=new N;x->r->p=x;x=x->r;x->l=x->r=NULL;x->c=m;U(x);}}
void I(w l,w r){K(l-1);N*x=t;t=x->r;t->p=NULL;K(r-l+1);x->r=t;t->p=x;t=x;}
void B(w l,w r){N*x=t;if(l||r!=n-1){if(!l){K(r+1);x=t->l;}else if(r==n-1){K(l-1);x=t->r;}else{I(l,r);x=t->r->l;}}x->f^=1;for(;x;){U(x);x=x->p;}}
};
w main(){ios::sync_with_stdio(0);cin.tie(0);
w n,m,a,l,r;cin>>n;T s;s.G(n);for(w i=0;i<n;i++){cin>>a;s.K(i);s.t->v=a;s.U(s.t);}cin>>m;while(m--){cin>>a>>l>>r;if(a==1)s.B(l-1,r-1);else{if(l==1&&r==n){s.K(n/2);cout<<s.t->A<<"\n";}else if(l==1){s.K(r);cout<<s.t->l->A<<"\n";}else if(r==n){s.K(l-2);cout<<s.t->r->A<<"\n";}else{s.I(l-1,r-1);cout<<s.t->r->l->A<<"\n";}}}}