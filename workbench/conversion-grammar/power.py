import numpy as np
from scipy.optimize import curve_fit
rng=np.random.default_rng(1)
def r2(y,yh):
    return 1-np.sum((y-yh)**2)/np.sum((y-np.mean(y))**2)
def beta_like(x,N,a,b):
    x=np.clip(x,1e-9,1-1e-9); return N*x**a*(1-x)**b
xs=np.linspace(0.02,0.98,40)
def frac_win(gen, thr=0.99, N=500):
    g=0
    for _ in range(N):
        ys=gen()
        ys=(ys-ys.min())/(ys.max()-ys.min()+1e-12)
        try:
            p,_=curve_fit(beta_like,xs,ys,p0=[1,.5,.5],maxfev=20000)
            if r2(ys,beta_like(xs,*p))>thr: g+=1
        except Exception: pass
    return g/N
# genuinely SMOOTH random monotone curves = logistic with random center/steepness
def logi(): 
    c=rng.uniform(.2,.8); k=rng.uniform(3,15); return 1/(1+np.exp(-k*(xs-c)))
# smooth random single-humped (density-like, A's class)
def hump():
    a=rng.uniform(-0.9,1.5); b=rng.uniform(0.5,3); return xs**(a if a>0 else a)* (1-xs)**b
# random power saturations (C's class)
def powsat():
    A=rng.uniform(.2,.9); c=rng.uniform(1.2,5); return 1-A*(1-xs)**c
print(f"beta R2>0.99 on smooth logistic (monotone) curves : {frac_win(logi):.2%}")
print(f"beta R2>0.99 on power-saturation curves (C-class)  : {frac_win(powsat):.2%}")
print(f"beta R2>0.99 on single-humped density curves       : {frac_win(hump):.2%}")
