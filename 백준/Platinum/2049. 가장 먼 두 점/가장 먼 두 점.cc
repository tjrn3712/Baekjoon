#include <bits/stdc++.h>
using namespace std;
using ll=long long;

struct Point {ll x,y;};
ll ccw(Point a, Point b, Point c) {
    return (b.x-a.x)*(c.y-a.y)-(b.y-a.y)*(c.x-a.x);
}
Point pivot = {-998244353,-998244353};
bool cmp (Point a, Point b) {
    ll c = ccw(pivot,a,b);
    if (c==0) {
        if (a.y==b.y) return a.x<b.x;
        return a.y<b.y;
    }
    return c>0;
}
ll dist2 (Point a, Point b) {
    return (a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y);
}

void solve() {
    int n;
    cin>>n;
    vector<Point> a(n);
    vector<Point> h;
    for (int i=0;i<n;i++) cin>>a[i].x>>a[i].y;
    int idx=0;
    for (int i=0;i<n;i++) if (a[i].y<a[idx].y||(a[i].y==a[idx].y&&a[i].x<a[idx].x)) idx=i;
    swap(a[idx],a[0]);
    pivot=a[0];
    sort(a.begin()+1,a.end(),cmp);
    h.push_back(a[0]);
    h.push_back(a[1]);
    for (int i=2;i<n;i++) {
        for (;h.size()>=2&&ccw(h[h.size()-2],h.back(),a[i])<=0;) h.pop_back();
        h.push_back(a[i]);
    }
    int nh=h.size();
    ll dd;
    ll d = -998244353;
    int j=1;
    Point ans1=h[0],ans2=h[1];
    for (int i=0;i<nh;i++) {
        int ni=(i+1)%nh;
        for (;;) {
            int nj=(j+1)%nh;
            if (llabs(ccw(h[i],h[ni],h[j]))<llabs(ccw(h[i],h[ni],h[nj]))) j=nj;
            else break;
        }
        dd=dist2(h[i],h[j]);
        if (dd>d) d=dd,ans1=h[i],ans2=h[j];
        dd=dist2(h[ni],h[j]);
        if (dd>d) d=dd,ans1=h[ni],ans2=h[j];
    }
    cout<<d;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t=1;
    //cin>>t;
    for (;t--;solve());
}