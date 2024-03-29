#####################################################
##    Mecanismo de Came - Ângulo de Pressão Exato  ##
##    Código desenvolvido por José Maria Bezerra   ##
##    Uso exclusivo alunos Mecanismos UFPE/DEMEC   ##
#####################################################

from sympy import *
#from IPython.display import HTML
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')

θ = symbols('theta',real=True)

def GetElev(curva, h, β):
    if (curva == 'harmonica'):
        u = 0.5*h*( 1 - cos(pi*θ/β) )
    elif (curva == 'cicloide'):
        u = h*( θ/β - (1/(2*pi))*sin(2*pi*θ/β) )
    elif (curva == 'duplaharmonica'):
        u = 0.5*h*( 1 - cos(pi*θ/β) - 0.25*(1 - cos(2*pi*θ/β)) )
    elif (curva == 'duplacicloide'):
        u = (4*h/3)*( θ/β - 0.5*(1/pi)*sin(2*pi*θ/β) - 0.25*(θ/β - 0.25*(1/pi)*sin(4*pi*θ/β)) )
    elif (curva[0] in ['2','3','4']):
        curva = curva.replace('-',"")
        k = [int(i) for i in curva]
        if (len(k) == 2):
            a,b = k[0],k[1]
            u = h*(b*(θ/β)**a - a*(θ/β)**b)
        elif (len(k) == 3):
            a,b,c = k[0],k[1],k[2]
            u = 0.5*h*(b*c*(θ/β)**a - 2*a*c*(θ/β)**b + a*b*(θ/β)**c)
        elif (len(k) == 4):
            a,b,c,d = k[0],k[1],k[2],k[3]
            u = 0.5*h*( (1/3)*b*c*d*(θ/β)**a - a*c*d*(θ/β)**b + a*b*d*(θ/β)**c - (1/3)*a*b*c*(θ/β)**d )
    else:
        print('ERRO --> função '+curva+' inexistente')
        return 0
    return u

def PrimeCircle(curva, h, β, φ, ε=0):
    if (curva == 'harmonica'):
        K = sqrt( 1 + (pi/(β*tan(φ)))**2 )
        Rₚ = 0.5*h*(K-1)
        θₒ = (β*acos(1/K))/pi
    elif (curva == 'cicloide'):
        K = 2*pi/(β*tan(φ))
        Rₚ = (h/pi)*(K - atan(K))
        θₒ = (β*atan(K))/pi
    elif (curva == 'duplaharmonica'):
        K = sqrt( 1 + 3*(pi/(β*tan(φ)))**2 )
        Rₚ = h*(3*(K-1)**2)/(8*K-4)
        θₒ = 2*β*atan( β*(K-1)*tan(φ)/pi )/pi
    elif (curva == 'duplacicloide'):
        K = sqrt( 1 + 16*(pi/(β*tan(φ)))**2 )
        Rₚ = h/(2*pi)*( 1/(3*sqrt(K**2-1))*(K**4 - 8*K**2 - 18*K**(-2) + 26) - acos(1 - 2/K**2)  )
        θₒ = (β/2*pi)*acos(1-2/K**2)
    elif (curva == '3-4-5'):
        K = 4/( β*tan(φ) ) - sqrt( 1 + ( 4/( β*tan(φ) ) )**2 )
        Rₚ = h*( (K+1)**3 / (64*K) ) * (3*K**3 - 9*K**2 + 13*K - 15)
        θₒ = 0.5*β*(1+K)
    elif (curva == '4-5-6'):
        K = 5/( β*tan(φ) ) - sqrt( 1 + (5/(β*tan(φ)))**2 - 2/( β*tan(φ) ) )
        Rₚ = h*( (K+1)**4 / (160*K-32) ) * (5*K**3 - 15*K**2 + 21*K - 19)
        θₒ = 0.5*β*(1+K)
    elif (curva == '3-4-5-6'):
        K = 5/(β*tan(φ)) - sqrt( 1 + (5/(β*tan(φ)))**2 + 2/(β*tan(φ)) )
        Rₚ = -h*( (K+1)**3/(160*K+32) )*(5*K**4 - 20*K**3 + 36*K**2 - 48*K + 51)
        θₒ = 0.5*β*(1+K)
    elif (curva == '4-5-6-7'):
        K = 6/(β*tan(φ)) - sqrt( 1 + (6/(β*tan(φ)))**2 )
        Rₚ = -h*( (K+1)**4 / (192*K) ) * (5*K**4 - 20*K**3 + 36*K**2 - 44*K + 35)
        θₒ = 0.5*β*(1+K)
    else:
        print('ERRO --> função '+curva+' inexistente')
        return 0

    u = GetElev(curva, h, β)
    v = diff(u,θ); uₜ = Lambda( θ, u ); vₜ = Lambda( θ, v )

    φₘₐₓ = atan( vₜ(θₒ)/( uₜ(θₒ)+Rₚ ) )
    Rᵢ = uₜ(θₒ)+Rₚ

    print('Rₚ = '+str(N(Rₚ,5))+'\nRᵢ = '+str(N(Rᵢ,5))+'\nθₒ = '+str(N(θₒ,5))+' rad\nφₘₐₓ = '+str(N(φₘₐₓ,5))+' rad')
    plot( atan(v/(u+Rₚ)), (θ,0,β), title='Ângulo de Pressão no intervalo [0,β]', xlabel='θ', ylabel='φ' )
    return 180*θₒ/pi, 180*φₘₐₓ/pi