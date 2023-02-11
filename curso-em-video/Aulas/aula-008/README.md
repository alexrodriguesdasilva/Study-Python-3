#Aula 008 - Utilizando Módulos
###O que são Módulos:
Por padrão quando instalado o python, varias "bibliotecas padrão Python" em seu "Módulos Padrão" já vem disponiveis para a gente utilizar.
Mas conseguimos utilizar outras bibliotecas e modulos em nossos programas, e até mesmo criar os nossos proprios modulos.

Por exemplo temos a Biblioteca "math" que é uma bibliocata com modulos voltados a matematica, e possui os seguintes modulos:
ceil
floor
trunc
pow
sqrt
factorial
Mais informaçoes sobre a biblioteca math podemos encontrar na documentação:
https://docs.python.org/3/library/math.html

###Para importar uma biblioteca, devemos utilizar o comando import, exemplo:
import math

###Caso você queira importar um ou mais modulos expecifico de uma biblioteca, devemos fazer da seguinte forma:
from math import ceil
from math import ceil, floor