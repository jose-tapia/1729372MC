dir="C:\\Users\\jossi\\Desktop\\datosParaGraficar.txt"
dir2="C:\\Users\\jossi\\Desktop\\datosParaGraficar2.txt"
datos=read.csv(dir,sep=" ")
datos2=read.csv(dir2,sep=" ")

plot(x=datos$Lenght, y=datos$Insertion, type="l", col="dark green",xlab="Longitud del arreglo",ylab="Cantidad de operaciones",main="Prueba de algoritmos de ordenamiento")
lines(x=datos$Lenght,y=datos$Bubble, col="dark red")
lines(x=datos$Lenght,y=datos$Selection, col="blue")
lines(x=datos$Lenght,y=datos$Quick, col="red")
lines(x=datos$Lenght,y=datos$Lenght**2,col="gray")
lines(x=datos$Lenght,y=datos$Lenght,col="orange")

boxplot(datos2$Bubble~datos2$Lenght,col="dark red",xlab="Longitud del arreglo",ylab="Cantidad de operaciones",main="Diagrama de BubbleSort")
boxplot(datos2$Insertion~datos2$Lenght,col="dark green",xlab="Longitud del arreglo",ylab="Cantidad de operaciones",main="Diagrama de InsertionSort")
boxplot(datos2$Selection~datos2$Lenght,col="blue",xlab="Longitud del arreglo",ylab="Cantidad de operaciones",main="Diagrama de SelectionSort")
boxplot(datos2$Quick~datos2$Lenght,col="red",xlab="Longitud del arreglo",ylab="Cantidad de operaciones",main="Diagrama de QuickSort")
