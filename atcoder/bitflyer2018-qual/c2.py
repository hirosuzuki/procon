import bisect

N,D=map(int,input().split())
X=[int(x) for x in input().split()]
ds=[0 for x in range(N+1)]
for i in range(N):
 ds[i]=bisect.bisect_left(X,X[i]+D+1)

ans=0
for i in range(N):
 a=ds[i]
 ans += sum(ds[j] for j in range(i,a))
 ans-=ds[i]*(a-i)
print(ans)
