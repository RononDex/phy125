# ---------------------------------------------------------------------------
# Solves a differential equation numerically
#
# Modul:   PHY125
# Author:  Tino Heuberger
# Email:   tino.heuberger@uzh.ch
# ---------------------------------------------------------------------------

from pylab import *

x0=array([13,0.5,1,5])
t=linspace(0,30,1000)
w=0.5
ep=2

lx2=[]

def F(X,t):
    return array([-sin(X[2])-ep*sin(X[2]-X[3]),ep*sin(X[2]-X[3]),X[0],w])


def RongaKuta(F,x0,t):
    x=x0
    dt=dt=t[2]-t[1]
    for i in t:
        x=x+dt*(1/2)*(F(x,t)+F(x+dt*F(x,t),t))
        lx2.append(x)


RongaKuta(F,x0,t)

# 
p=[x0[0]]
P=[x0[1]]
q=[x0[2]]
Q=[x0[3]]
for i in lx2:
    p.append(i[0])
    P.append(i[1])
    q.append(i[2])
    Q.append(i[3])


H=[]
for i in range(len(t)):
    h=1/2*p[i]**2+w*P[i]-cos(q[i])-ep*cos(q[i]-Q[i])
    H.append(h)

print(H)
plot(t,H,'oc')
axis([-1,12,80,90])
show()