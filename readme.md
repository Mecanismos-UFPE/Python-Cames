## elevdiagram.py
> ## **Funções:**
>
> **GetElev**, **GetRet**, **PlotCurv** e **PlotDiagrams**
>
> Formas de Uso:
>
> ~~~
> curv = GetElev('Curva', h, β)
> curv = GetRet('Curva', h, β)
> PlotCurv(curv)
> PlorCurv(curv, AcelTrue)
> ~~~

>
> **Argumentos:**
>
> *Funçao GetElev e GetRet:*
> ~~~
> 'harmonica'
> 'cicloide'
> 'duplaharmonica'
> 'duplacicloide'
> '3-4' ou '4-5'
> '3-4-5' ou '4-5-6'
> '3-4-5-6' ou '4-5-6-7'
>
> h - Valor que representa a altura de elevação
> β - Ângulo de elevação, sempre em radianos
> ~~~

> *Funçao PlotCurv:*
>
> ~~~
> curv     - Valor obtido na função GetElev ou GetRet
> AcelTrue - Argumento, não obrigatório, se presente, com valor
>            diferente de zero, não plota o gráfico da aceleração segunda.
> ~~~

> *Funçao PlotDiagrams:*
>
> ~~~
> f  - Valor obtido da função GetElev.
> βs - Ângulo de repouso superior (se não houver, deixe zero)
> g  - Valor obtido da função GetRet.
> βi - Ângulo de repouso inferior (se não houver, deixe zero)
> ~~~

**Forma de uso do Código**
~~~
from elevdiagram import *

f = GetElev('duplacicloide', 2, pi/2)
g = GetElev('duplahamonica', 2, 2*pi/3)
PlotCurv(f,1)
PlotCurv(g)
PlotDiagrams(f, pi/2, g, pi/3)
~~~