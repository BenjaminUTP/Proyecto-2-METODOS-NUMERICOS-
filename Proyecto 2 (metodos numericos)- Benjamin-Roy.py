#NOMBRES DE LOS ESTUDIANTES: ROY CARRINGTON Y BENJAMIN RODRIGUEZ
from multiprocessing.sharedctypes import Value
from sympy import *
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np
#ACTUALIZACION PARA CAMBIAR GIT
#---------------------Funciones---------------------
def f5(x):
    return - 0.5* x ** 2 + 2.5 * x - 4.5
#Variables
vx=[]
list=[]
resp=1
x=0
i=0
a1 = -1           
b1 = 10           
n1 = 50  
es=0.05
ea=2*es
x1=0        
#Cuerpo del programa--------------------------------
while(resp==1 or resp==2):
    while True:
        try:
            resp=int(input("Introduzca la opcion que desee (1 metodo abierto) (2 metodo cerrado) (Cualquier otra tecla para salir):"))
            break
        except ValueError:
            print("Introduzca un numero valido")

    if resp==1:
        x=Symbol('x')
        f=input("Ingrese la funcion:")
        fx=lambda x:eval(f)
        df=input("Ingrese la derivada de esa funcion: ")
        dfx=lambda x: eval(df)
        registro="{:<20} {:<15.2f} {:<15.2f} {:<15.2f} {:<15} {:<15} ".format(i, x1, fx(x1) , dfx(x1), "--", "--")
        list.append(registro)
        vx.append(0)
        i=1
        while ea>es:
            x1 = x1- fx(x1)/dfx(x1)
            vx.append(x1)
            f1=fx(x1)
            f2=dfx(x1)

            if x1 != 0:
                ea = abs((vx[i] - vx[i-1]))
                er=abs((vx[i]-vx[i-1])/vx[i])*100

            if i>=20:
                print("No es posible encontrar la solucion")
                break
            registro="{:<20} {:<15.2f} {:<15.2f} {:<15.2f} {:<15.2f} {:<15.2f} ".format(i, x1, f1 , f2, ea, er)
            list.append(registro)
            i=i+1

        print("Metodo Newton-Raphson")
        print("{:<20} {:<15} {:<15} {:<15} {:<15} {:15}".format('Iteracion', 'X', 'f(x)', 'df(x)','ea','er(%)'))
        for l in list:
            print(l)
        k1 = np.linspace(a1, b1, n1)
        fxx=fx(k1)
        print("Grafica de la funcion")
        plt.figure(figsize=(8, 6))
        plt.plot(k1,fxx , label=("fx"))
        plt.plot(k1, np.zeros(len(k)), 'k:', label=("0"))
        plt.plot(x1, fx(x1), 'ko', label=("Raiz Newton"))
        plt.xlabel("x")            
        plt.ylabel("y")            
        plt.title("Grafica fx") 
        plt.legend()                   
        plt.show()                      
        list.clear()
        
    elif (resp== 2):
        a = int(input("Valor de a ="))
        b = int(input("Valor de b ="))
        n = int(input("Cuantas iteraciones desea?: "))
        if f5(a)*f5(b)>1000:
            print("error")
        else:
            k=1
            while(k<=n):
                c=(a+f5(b)-b*f5(a))/(f5(b)-f5(a))
                if f5(a)+f5(b)<0:
                    b=c
                else:
                    a=c
                print("El valor de la raíz es",c, "en la iteración", k)
                k=k+1
    else:
        print('Error')