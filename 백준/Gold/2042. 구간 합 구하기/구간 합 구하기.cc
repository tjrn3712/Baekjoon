#import<iostream>
#define _ std::cin
long n,i,s['力'],b,c;main(){for(_>>n>>b>>c;i<n;_>>s[n+i++]);for(;--i;s[i]=s[i*2]+s[i*2+1]);for(;_>>i>>b>>c;)if(b+=~-n,~----i){for(c+=n;b<c;b/=2,c/=2)i+=b&1?s[b++]:0,i+=c&1?s[--c]:0;std::cout<<i<<' ';}else for(c-=s[b];s[b]+=c,b/=2;);}