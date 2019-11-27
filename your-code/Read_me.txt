Proyecto de Visualización de Datos
		
		Ramiro Maravilla


En este proyecto quiero explorar la relación entre pobreza y desigualdad indígena.
Me parece que este proyecto es importante en el contexto en el que el presidente
Andrés Manuel López Obrador declaró que bajaría la edad de retiro de los indígenas 
de 68 a 65 años. Ante estas declaraciones varios usuarios en redes sociales salieron
a acusar al presidente de racista.

Frente a estas declaraciones, quiero visualizar los datos para responder a la siguiente
pregunta: ¿Es justificable disminuir la edad de retiro de las personas indígenas en México
de 68 a 65 años?

A diferencia de otros estudios, no parto de una hipótesis respecto a si es justificable o no.
Espero que la visualización de datos responda mi pregunta de investigación

Los datos con los que trabajo corresponden a las cifras de Pobreza de los Censos del 
Consejo Nacional para la Evaluación de la Política de Desarrollo Social (CONEVAL).

A continuación, se describe el proceso por el que realice este ejercicio de visualización:

Visualización de ingreso por deciles:
1. Descargué la base de Coneval de ingreso por decil y la cargué usando pandas
2. Examiné la información para observar sus variables. 
3. Transpuse la base de datos en la variable "Decil".
4. Limpié la base de dato quitando columnas que no me servían para el análisis. 
5. Realicé varias gráficas para mostrar los ingresos por decil. Decidí que me convenía
	hacer una gráfica de burbujas que mostrara la media de ingresos de cada decil.

Visualización Pobreza en México
1. Cargamos base
2. Hacemos una gráfica de lineas con dos subplots que muestre la evolución de pobreza 
	en términos absolutos y relativos de 2008 a 2018.

Visualización Boxplots de comparación pobreza indígena y no indígena
1. Cargamos la base.
2. Renombramos las variables para tenerlas más cortas y poderlas graficar mejor
3. Utilizamos seaborn y hacemos una gráfica de boxplot que muestre la distribución de la pobreza
	indigena y no indigena. Esta misma gráfica también muestra la pobreza extrema no indigena
	y no indigena. 
4. Adicionalmente, se hizo una gráfica de barras con tres subplots que graficaran la evaluación
	de 2008 a 2018 de pobreza indigena y no indigena, pobreza moderada indigena y no indigea,
	pobreza extrema indigena y no indigena.

Visualización de dispersión. Relación de pobreza con carencias en derechos sociales básicos.
1. Se cargó una base de datos con la dispersión de pobreza por estado en 2012, 2014, 2016 y 2018.
2. Se agregó población de personas viviendo con carencia por rezago educativo, acceso a salud,
	sin seguridad social, servicios básicos de vivienda.
3. Se hizo una gráfica con cuatro subplots que muestra la relación positiva entre pobreza y todas esas 
	carencias. 

Visalización de pairplot
1. Finalmente se hizo una relación pairplot de todas las variables estatales que se tienen con las carencias
	exploradas en las gráficas anteriores y el indice de pobreza.

Estas gráficas demuestran que la población indígena es más vulnerable a la pobreza y por lo tanto merece
un trato diferenciado de la población no indigena. 

Estas gráficas se presentan en un power point. 

