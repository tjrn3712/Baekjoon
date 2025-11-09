#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ld = long double;

ll curx, cury;
void move_step (ll s, ld ux, ld uy) {
    ld d=sqrt(ux*ux+uy*uy);
    ux/=d;
    uy/=d;

    ll dx=llround(ux*(ld)s);
    ll dy=llround(uy*(ld)s);
    curx+=dx;
    cury+=dy;

    cout<<curx<<' '<<cury<<'\n';
    cout.flush();
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>curx>>cury;

    int n=0;
    ld R=1.0L;

    for (int a[6];;) {
        for (int i=0;i<6;i++) cin>>a[i];

        bool take=false;
        if (n<4) {
            ll sum=0;
            for (int i=0;i<6;i++) sum+=a[i];
            if (sum>=44444) {
                take=true;
                n++;
                int mx=*max_element(a,a+6);
                R+=(ld)mx;
            }
        }

        cout<<(take?"take":"pass")<<'\n';
        cout.flush();

        ll s;
        cin>>s;

        ld D=sqrt((ld)curx*curx+(ld)cury*cury);
        if (D==0.0L) {
            move_step(s, 1.0L, 0.0L);
            continue;
        }
        if (fabsl(D-(ld)s)<1.0L-1e-6L) {
            cout<<"0 0\n";
            cout.flush();
            return 0;
        }

        ld ux, uy;
        if (n<4) {
            ux=-(ld)curx/D;
            uy=-(ld)cury/D;
        } else {
            ld sld=(ld)s;
            ld C=(D*D+sld*sld-R*R)/(2.0L*D*sld);

            ld urx=-(ld)curx/D;
            ld ury=-(ld)cury/D;
            ld utx=-ury;
            ld uty=urx;

            ld S=sqrt(max(0.0L,1.0L-C*C));
            ux=C*urx+S*utx;
            uy=C*ury+S*uty;
        }

        move_step(s, ux, uy);
    }
}
