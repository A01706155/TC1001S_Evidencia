# TC1001S_Evidencia
Repositorio de evidencias para la materia "Herramientas computacionales: el arte de la programación".

## ¿Cómo correr los juegos?
### Visual Studio Code:
Primero, se debe descargar [Visual Studio Code](https://code.visualstudio.com/Download), una vez descargado se debe instalar. Todavia no se debe de abrir.

### Python:
Se debe descargar [Python](https://www.python.org/downloads/) y al instalarlo marcar la opción de "Añadir a la ruta del sistema". 

### Git:
Para poder clonar el repositorio es necesario descargar [Git](https://git-scm.com/downloads) e instalarlo con las opciones por defecto en cada paso.

### Configuración:
1. Abrir Visual Studio Code
    * Dentro de visual, abrir una terminar y clonar el repositorio
    * En la parte izquierda del programa, hacer click en extensiones e instalar Python
    * Cuando se instale la extensión de Python seguir los pasos de configuración que salen automáticamente
2. Descarga de paquetes de pip
    * Para poder ejecutar los juegos y revisar el estandar de código hay que ingresar los siguientes comandos en la terminal
    * ``` pip install flake8 ```
    * ``` pip install freegames ```

### Corriendo los juegos:
Para correr los juegos simplemente hay que utilizar este comando en la terminal
``` python nombreJuego.py ```

#### Juegos incluídos en esta evidencia
Estos son los casos posibles:
* ``` python pacman.py ```
* ``` python memory.py ```
* ``` python tictactoe.py ```

## Pacman - Manolo, A01706155
* Pacman es un juego clásico de namco y ha sido recreado en Python mediante la librería de turtle.
* Para ejecutarlo se debe usar `python pacman.py`
* Los cambios realizados en el juego fueron:
    1. Cambiar el tablero del juego.
        * Para esto se realizó un cambio en el array del tablero modificando 1's y 0's
    2. Modificar la velocidad de los fantasmas.
        * Para esto se realizo un cambio en el movimiento vectorial de inicio y de cambio en los valores del fantasma.

## Memory - Flavio, A01367631
* Memory es un juego de memoria donde poco a poco vas desarrollando una imagen.
* Para ejecutarlo se debe usar `python memory.py`
* Los cambios realizados en el juego fueron:
    1. Crear un contador de cuantos taps hay. (se imprime en consola y en el juego)
        * Para esto se utilizó una variable que almacena los toques y los imprime en pantalla mediante el método write especificando tamaño y fuente de letra así como una posición.
    2. Saber cuándo termina el juego. (se imprime en consola)
        * Para esto sólamente se añadió una función que comprueba cuando ya no hay más tiles e imprime en consola cuando se termina el juego como tal.

## Tic-Tac-Toe - Diego, A01704492
* Tic-Tac-Toe es un juego de gato común donde debes ganarle a otra persona al crear una línea de tres.
* Para ejecutarlo se debe usar `python tictactoe.py`
* Los cambios realizados en el juego fueron:
    1. Cambiar el tamaño de las X, las O y centrarlos.
        * Para esto se cambió manualmente la forma de vectores que se dibujaban.
    2. Validar si una casilla ya se encuentra ocupada.
        * Para esto se revisaba si ya existia la casilla ocupada en base a la posición y a un array que registraba cada uno.
