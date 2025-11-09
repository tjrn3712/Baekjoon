#include <bits/stdc++.h>
using namespace std;
using ll=long long;

struct Point {
    long long x, y;
    int idx;
};
ll ccw (Point a, Point b, Point c) {
    ll cp = (b.x-a.x)*(c.y-a.y)-(b.y-a.y)*(c.x-a.x);
    if (cp>0) return 1;
    else if (cp<0) return -1;
    else return 0;
}
Point a0;
bool cmp (Point a, Point b) {
    ll c = ccw(a0,a,b);
    if (c==0) {
        if (a.y==b.y) return a.x<b.x;
        return a.y<b.y;
    }
    return c>0;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n,p=0,m,t;
    cin>>n;
    vector<Point> a;
    for (int i=0;i<n;i++) {
        ll x,y;
        cin>>x>>y;
        a.push_back({x,y,i});
    }
    cin>>m;
    for (int i=n;i<m+n;i++) {
        ll x,y;
        cin>>x>>y;
        a.push_back({x,y,n});        
    }
    t=m+n;
    for (int i=1;i<t;i++) if (a[i].y < a[p].y || (a[i].y == a[p].y && a[i].x < a[p].x)) p=i;
    swap(a[p],a[0]);
    a0=a[0];
    sort(a.begin()+1,a.begin()+t,cmp);
    int i=t-1;
    for (;i>1&&ccw(a0,a[i-1],a[i])==0;i--);
    reverse(a.begin()+i,a.begin()+t);

    vector<Point> ch;
    ch.push_back(a[0]);
    ch.push_back(a[1]);
    for (int i=2;i<t;i++) {
        for (;ch.size()>=2&&ccw(ch[ch.size()-2],ch.back(),a[i])<0;ch.pop_back());
        ch.push_back(a[i]);
    }

    int s = ch.size();
    int cnt = 0;
    for (int i=0;i<s;i++) {
        int j = (i+1)%s;
        int u = ch[i].idx;
        int v = ch[j].idx;
        if (u==n||v==n) continue;
        if ((u+1)%n==v||(v+1)%n==u) cnt++;
    }
    cout<<cnt;
}