#Librerías

import matplotlib.pyplot
import numpy
import matplotlib


#Constantes

SB = 5.67*10**(-8)               #Constante de Stefan Boltzmann
a = 0.3                         #Emisividad de la atmósfera
Rad_Solar = 1353                #Watts por unidad de area que llegan a la tierra desde el sol conocida como constante solar
r_Tierra = 6.371*10**6         #Radio de la Tierra en metros
r_Atmosfera = 6.371*10**6       #La altura de la atmosfera es despreciable respecto al radio del planeta entero                #Capacidad calorifica volumetrica suponiendo que la Tierra es un bola de tierra seca.
c_Atmosfera = 1214                 #Capacidad calorífica volumetrica del aire
Temp_Tierra = 200                   #valores iniciales
Temp_Atmospera = 150               #valores iniciales
dt = 900                     #15 minutos en segundo

#Construcción del planeta Tierra
latitud = numpy.arange(-90,91,10)
longitud = numpy.arange(0,361,10)
Temp_Tierra = numpy.zeros((len(latitud),len(longitud))) + 200
Temp_Atmospera = numpy.zeros((len(latitud),len(longitud))) + 200
f,ax = matplotlib.pyplot.subplots(2)
ax[0].contourf(Temp_Tierra)
ax[1].contourf(Temp_Atmospera)
matplotlib.pyplot.ion()
matplotlib.pyplot.show()

#Construcción de continentes y oceanos
c_Tierra = numpy.zeros((len(latitud),len(longitud))) + 4.18*10**6 #oceanos
#Continentes
c_Tierra[1:16,5:10] = 2763000 #América
c_Tierra[13:17,11:14] = 2763000 #Groenlandia (No es un continente pero es una masa de tierra bastante grande)
c_Tierra[12:17,18:34] = 2763000 #Europa y Asia del Norte
c_Tierra[1:11,18:25] = 2763000 #Africa
c_Tierra[2:5,29:34] = 2763000 #Australia (No es un continente pero es una masa de tierra bastante grande)


#Clima
while True:
    for i in range(len(latitud)):
        for j in range(len(longitud)):
            Temp_Tierra[i,j]  = Temp_Tierra[i,j] + dt*(Rad_Solar*numpy.cos(latitud[i]*numpy.pi/180)*(numpy.pi*r_Tierra**2)+(a*SB*Temp_Atmospera[i,j]**4)*(4*numpy.pi*r_Tierra**2)-SB*Temp_Tierra[i,j]**4*(4*numpy.pi*r_Tierra**2))/(c_Tierra[i,j]*(4*numpy.pi*r_Tierra**2))
            Temp_Atmospera[i,j] = Temp_Atmospera[i,j] + dt*(-(2*a*SB*Temp_Atmospera[i,j]**4*4*numpy.pi*r_Atmosfera**2)+(a*SB*Temp_Tierra[i,j]**4*4*numpy.pi*r_Atmosfera**2))/(c_Atmosfera*4*numpy.pi*r_Atmosfera**2)
    ref_barra = ax[0].contourf(Temp_Tierra)
    #Visualización del Clima
    ax[1].contourf(Temp_Atmospera)
    ax[0].set_title('Temperatura Superficial')
    ax[1].set_title('Temperatura Atmosférica')
    matplotlib.pyplot.pause(0.1)
    f.subplots_adjust(right=0.8)
    cbar_ax = f.add_axes([0.85, 0.15, 0.05, 0.7])
    matplotlib.pyplot.pause(0.01)
    ax[0].cla()
    ax[1].cla()
    barra = f.colorbar(ref_barra , cax=cbar_ax)
    barra.outline.set_visible(False) #Esto es para evitar fallos estéticos conocidos