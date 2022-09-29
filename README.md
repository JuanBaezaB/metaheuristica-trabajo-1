# Algoritmo genético para el problema de las n-reinas
El programa presenta una solución estocástica llamada algoritmo genético para la resolución del problema de las n reinas.
Para el correcto funcionamiento de este se deben considerar los siguientes puntos:
## Instalación
Para instalar la aplicación se deben seguir los siguientes pasos:
- Para bajar el programa haga click en el siguiente [link](https://github.com/JuanBaezaB/metaheuristica-trabajo-1/archive/refs/heads/main.zip)
- La aplicación funciona sobre python 3.10.5 o superior
- Instalar la biblioteca ``numpy`` con el siguiente comando:
```
pip install numpy
```
## Ejecución
- Para ejecutar se debe ejecutar el comando 
```
python ./n-reinas.py seed tamaño_tabl tamaño_pobl prob_cruza prob_mut num_ite
```
- Donde:
  - **seed** es un valor entero positivo
  - **tamaño_tabl** representa el tablero n x n con n entero mayor o igual a 4
  - **tamaño_pobl** es un valor entero positivo igual o mayor a 2 que representa el número de poblaciones
  - **prob_cruza** es un valor decimal entre 0.0 y 1.0 que representa la probabiliad de que se crucen 2 poblaciones
  - **prob_mut** es un valor decimal entre 0.0 y 1.0 que representa la probabiliad de mutar una población
  - **num_ite** es el número máximo de iteraciones que realiza el programa que toma valores mayores o iguales a 1
- Un ejemplo de entrada es la siguiente:
```
python ./n-reinas.py 10 10 100 0.95 0.1 100
```

Este programa fue desarrollado en [Github](https://github.com/JuanBaezaB/metaheuristica-trabajo-1)
## Autores
- Juan Baeza Baeza / jbaeza@ing.ucsc.cl / [JuanBaezaB](https://github.com/JuanBaezaB)
- Fernando Cabezas Herrera / fcabezas@ing.ucsc.cl / [FernandoProg](https://github.com/FernandoProg)