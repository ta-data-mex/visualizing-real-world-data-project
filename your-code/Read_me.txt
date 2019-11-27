Proyecto de Visualizaci�n de Datos
		
		Ramiro Maravilla


En este proyecto quiero explorar la relaci�n entre pobreza y desigualdad ind�gena.
Me parece que este proyecto es importante en el contexto en el que el presidente
Andr�s Manuel L�pez Obrador declar� que bajar�a la edad de retiro de los ind�genas 
de 68 a 65 a�os. Ante estas declaraciones varios usuarios en redes sociales salieron
a acusar al presidente de racista.

Frente a estas declaraciones, quiero visualizar los datos para responder a la siguiente
pregunta: �Es justificable disminuir la edad de retiro de las personas ind�genas en M�xico
de 68 a 65 a�os?

A diferencia de otros estudios, no parto de una hip�tesis respecto a si es justificable o no.
Espero que la visualizaci�n de datos responda mi pregunta de investigaci�n

Los datos con los que trabajo corresponden a las cifras de Pobreza de los Censos del 
Consejo Nacional para la Evaluaci�n de la Pol�tica de Desarrollo Social (CONEVAL).

A continuaci�n, se describe el proceso por el que realice este ejercicio de visualizaci�n:

Visualizaci�n de ingreso por deciles:
1. Descargu� la base de Coneval de ingreso por decil y la cargu� usando pandas
2. Examin� la informaci�n para observar sus variables. 
3. Transpuse la base de datos en la variable "Decil".
4. Limpi� la base de dato quitando columnas que no me serv�an para el an�lisis. 
5. Realic� varias gr�ficas para mostrar los ingresos por decil. Decid� que me conven�a
	hacer una gr�fica de burbujas que mostrara la media de ingresos de cada decil.

Visualizaci�n Pobreza en M�xico
1. Cargamos base
2. Hacemos una gr�fica de lineas con dos subplots que muestre la evoluci�n de pobreza 
	en t�rminos absolutos y relativos de 2008 a 2018.

Visualizaci�n Boxplots de comparaci�n pobreza ind�gena y no ind�gena
1. Cargamos la base.
2. Renombramos las variables para tenerlas m�s cortas y poderlas graficar mejor
3. Utilizamos seaborn y hacemos una gr�fica de boxplot que muestre la distribuci�n de la pobreza
	indigena y no indigena. Esta misma gr�fica tambi�n muestra la pobreza extrema no indigena
	y no indigena. 
4. Adicionalmente, se hizo una gr�fica de barras con tres subplots que graficaran la evaluaci�n
	de 2008 a 2018 de pobreza indigena y no indigena, pobreza moderada indigena y no indigea,
	pobreza extrema indigena y no indigena.

Visualizaci�n de dispersi�n. Relaci�n de pobreza con carencias en derechos sociales b�sicos.
1. Se carg� una base de datos con la dispersi�n de pobreza por estado en 2012, 2014, 2016 y 2018.
2. Se agreg� poblaci�n de personas viviendo con carencia por rezago educativo, acceso a salud,
	sin seguridad social, servicios b�sicos de vivienda.
3. Se hizo una gr�fica con cuatro subplots que muestra la relaci�n positiva entre pobreza y todas esas 
	carencias. 

Visalizaci�n de pairplot
1. Finalmente se hizo una relaci�n pairplot de todas las variables estatales que se tienen con las carencias
	exploradas en las gr�ficas anteriores y el indice de pobreza.

Estas gr�ficas demuestran que la poblaci�n ind�gena es m�s vulnerable a la pobreza y por lo tanto merece
un trato diferenciado de la poblaci�n no indigena. 

Estas gr�ficas se presentan en un power point. 

