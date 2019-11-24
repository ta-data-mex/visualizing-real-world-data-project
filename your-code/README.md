![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Project: Visualizing Real World Data

## Overview

Con base en una hipótesis analizar una base de datos y de manera visual presentar
las conclusiones de ésta.

## Base de datos

La base de datos elegida fue un concentrado de los personajes aparecidos en la saga
de Harry Potter, ésta fue obtenida de kaggle:

https://www.kaggle.com/gulsahdemiryurek/harry-potter-dataset

Datos:

 - Personajes,género,Patronus,Trabajo,Pureza de sangre,Casa,Lealtad,nacimiento,muerte


## Proceso

-Importar librerias necesarias
-Observar el data set y los tipos de variables
-Visualizar los nulls, o Nans
-Visualizar frecuencias en los datos
-Frustración al darte cuenta que todos los datos son categóricos y complica un poco el proceso.
-Agrupar los tipos de pureza en la sangre en 7 para analizarlos.
-creación de columnas con booleanos para poder graficar
(Género y lealtad)
-Frustración al darte cuenta que tu muestra no es representantiva, ésto debido a que la base
se compone por los personajes aparecidos en la historia y no es una población ya que podemos
observar que la población de mujeres representa la mitad de la población masculina(WTF JK?),
adicional la agrupación por casas se concentra en las dos principales debido a la historia.

-Graficar por casas por tipo de sangre para observar la concentración.
-Al tener datos de las muertes se grafica el acumulado de éstas por año, debido a la historia
se concluye que los picos en los años (1970-1980) representan el inicial régimen de Voldemort 
y la lucha que existió entre la primer órden del fénix, el segundo pico es (1998) éste representa
la segunda lucha entre el army del señor tenebroso y la generación de Harry.

## Para una mejor visualización y entendimiento de esta base, se deberán utilizar pesos para
poder eliminar el sesgo que existe y así presentar datos representativos.

