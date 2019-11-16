from sympy import *
import matplotlib.pyplot as plt
from sympy.plotting import plot
from sympy.solvers import solve
import math
import numpy as np
from sympy import Heaviside, DiracDelta
i=sqrt(-1)
class Anacom:
    def __init__():
        pass

    def unitstep(t):
        x=Heaviside(t)
        plot(x)
        return x

    def diracdelta(t):
        k=DiracDelta(t)
        plot(k)
        return k

    def signum(t):
        x=sign(t)
        plot(x)
        return x

    def sawtooth(t):
        saw=symbols('saw')
        saw=t-floor(t)
        plot(saw)
        return saw

    def ramp(t):
        ram=symbols('ram')
        ram=t*Heaviside(t)
        plot(ram)
        return ram

    def cdf(pdf,lower_lim,Upper_lim):
        S = symbols('S')
        S = integrate(pdf, (x, lower_lim,Upper_lim))
        return S

    def pdf(cdf):
        S = diff(cdf,x)
        return S

    def absIntegrablewithoutPeriod(g,t):
        if (integrate(g,(t,-oo,oo))<oo) and (integrate(g,(t,-oo,oo))>-oo):
            return True
        else:
            print("Doesn't satisfy Dirchilit's Conditions")
            return False

    def fTrans(g,t):
        G,f=symbols('G f')
        G=integrate(g*exp(-1*2*pi*f*t*i),(t,-oo,oo))
        return G

    def fTransVal(G,freq):
        f=symbols('f')
        return G.subs(f,freq)

    def invfTrans(G,f):
        pi=3.14159
        g=symbols('g')
        g=integrate(G*exp(2*pi*f*t*i),(f,-oo,oo))
        return g

    def invfTransVal(g,time):
        return g.subs(t,time)

    def ampmod(ms,m,c):
        s=(1+m*ms)*c
        plt.subplot(312)
        plt.plot(s)
        return s

    def demod(s,c,r):
        x=s*c
        dmod_sig=np.convolve(x,r)/100
        plt.subplot(313)
        plt.plot(dmod_sig)
        return dmod_sig

    def ssbscmod(am,fm,ac,fc):
        t=np.linspace(0,1,1000)
        s=((am*ac)/2)*np.cos(2*np.pi*(fc+fm)*t)
        plt.plot(s)
        return s

    def dsbscmod(ms,c):
        s=ms*c
        plt.plot(s)
        return s

    def fremod(Ac,Fc,Kf,Fm,Am):
        T,t=symbols('T t')
        x = 2*pi*Fm*t
        m = Am*cos(x)
        Z=integrate(m,(t,0,.5))
        y = 2*pi*Fc*t+(2*pi*Kf)*Z
        S=Ac*cos(y)
        plot(S)
        return S

    def PhaseMod(Ac,Kp,k):
        fc=1/2
        s=symbols('s')
        s=Ac*cos(2*pi*fc*t+Kp*k)
        plot(s)

    def pwm(k,t):
        st=symbols('st')
        st=t-floor(t)
        pwm=symbols('pwm')
        x=k-st
        pwm=sign(x)
        plot(pwm)
        return pwm

    
