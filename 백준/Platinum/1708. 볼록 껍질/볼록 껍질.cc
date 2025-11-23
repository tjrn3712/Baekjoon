#include <bits/stdc++.h>
using namespace std;
using ll=long long;

struct Point{ll x,y;};
ll ccw(Point a, Point b, Point c) {
    return (b.x-a.x)*(c.y-a.y)-(b.y-a.y)*(c.x-a.x);   
}

Point pivot = {-100000,-100000};
bool cmp (Point a, Point b) {
    ll c = ccw(pivot,a,b);
    if (c==0) {
        if (a.y==b.y) return a.x<b.x;
        else return a.y<b.y;
    }
    return c>0;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin>>n;
    vector<Point> a(n);
    for (int i=0;i<n;i++) {
        cin>>a[i].x>>a[i].y;
    }

    int idx=0,x=998244353,y=998244353;
    for (int i=0;i<n;i++) {
        int p=a[i].x,q=a[i].y;
        if (q<y) {
            x=p,y=q;
            idx=i;
        } else if (q==y) {
            if (p<x) {
                x=p,y=q;
                idx=i;
            }
        }
    }
    swap(a[idx],a[0]);
    pivot=a[0];
    sort(a.begin()+1,a.end(),cmp);
    vector<Point> h;
    h.push_back(a[0]);
    h.push_back(a[1]);
    for (int i=2;i<n;i++) {
        for (;h.size()>=2;) {
            Point p2=h.back();
            h.pop_back();
            Point p1=h.back();
            if (ccw(p1,p2,a[i])>0) {
                h.push_back(p2);
                break;
            }
        }
        h.push_back(a[i]);
    }
    cout<<h.size()<<'\n';
}