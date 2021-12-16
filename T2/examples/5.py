import sys
readline=sys.stdin.readline

mod=202753
def NTT(polynomial1,polynomial2):
    prim_root=10
    prim_root_inve=60826
    def DFT(polynomial,n,inverse=False):
        dft=polynomial+[0]*((1<<n)-len(polynomial))
        if inverse:
            for bit in range(1,n+1):
                a=1<<bit-1
                x=pow(prim_root,mod-1>>bit,mod)
                U=[1]
                for _ in range(a):
                    U.append(U[-1]*x%mod)
                for i in range(1<<n-bit):
                    for j in range(a):
                        s=i*2*a+j
                        t=s+a
                        dft[s],dft[t]=(dft[s]+dft[t]*U[j])%mod,(dft[s]-dft[t]*U[j])%mod
            x=pow((mod+1)//2,n)
            for i in range(1<<n):
                dft[i]*=x
                dft[i]%=mod
        else:
            for bit in range(n,0,-1):
                a=1<<bit-1
                x=pow(prim_root_inve,mod-1>>bit,mod)
                U=[1]
                for _ in range(a):
                    U.append(U[-1]*x%mod)
                for i in range(1<<n-bit):
                    for j in range(a):
                        s=i*2*a+j
                        t=s+a
                        dft[s],dft[t]=(dft[s]+dft[t])%mod,U[j]*(dft[s]-dft[t])%mod
        return dft

    n=(len(polynomial1)+len(polynomial2)-2).bit_length()
    ntt=[x*y%mod for x,y in zip(DFT(polynomial1,n),DFT(polynomial2,n))]
    ntt=DFT(ntt,n,inverse=True)[:len(polynomial1)+len(polynomial2)-1]
    return ntt

lS,lT,K=map(int,readline().split())
S=readline().rstrip()
T=readline().rstrip()
cnt=[0]*lS
for s in "ACGT":
    lstS=[0]*lS
    lstT=[0]*lT
    for i in range(lT):
        if T[i]==s:
            lstT[lT-1-i]+=1
    for i in range(lS):
        if S[i]==s:
            lstS[max(0,i-K)]+=1
            if i+K+1<lS:
                lstS[i+K+1]-=1
    for i in range(1,lS):
        lstS[i]+=lstS[i-1]
    for i in range(lS):
        if lstS[i]:
            lstS[i]=1
    lst=NTT(lstS,lstT)[lT-1:]
    for i in range(lS):
        cnt[i]+=lst[i]
ans=cnt.count(lT)
print(ans)