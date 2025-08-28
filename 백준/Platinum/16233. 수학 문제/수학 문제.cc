#include <bits/stdc++.h>
using namespace std;

int s(int x) {
    int t=0;
    for (;x;) {
        t+=x%10;
        x/=10;
    }
    return t;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t,n,k,tmp,lim,a,b,c,x,y;
    cin>>t;
    for (;t--;) {
        cin>>n;
        if (n%9) {cout<<-1<<" "; continue;}
        for (k=0,tmp=n;tmp;k++) tmp/=10;
        lim=9*k+9;
        x=n,a=-1,b=s(x);
        for (int i=0;i<=lim;i++,x++) {
            if (b==i) {a=x; break;}
            for (y=x,c=0;y%10==9;c++) y/=10;
            b+=1-9*c;
        }
        cout<<a<<" ";
    }
}