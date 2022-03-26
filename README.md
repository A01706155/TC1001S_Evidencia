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
    2. Modificar la velocidad de los fantasmas.

## Memory - Flavio, A01367631
* Memory es un juego de memoria donde poco a poco vas desarrollando una imagen.
* Para ejecutarlo se debe usar `python memory.py`
* Los cambios realizados en el juego fueron:
    1. Crear un contador de cuantos taps hay. (se imprime en consola)
    2. Saber cuándo termina el juego. (se imprime en consola)

## Tic-Tac-Toe - Diego, A01704492
* Tic-Tac-Toe es un juego de gato común donde debes ganarle a otra persona al crear una línea de tres.
* Para ejecutarlo se debe usar `python tictactoe.py`
* Los cambios realizados en el juego fueron:
    1. Cambiar el tamaño de las X, las O y centrarlos.
    2. Validar si una casilla ya se encuentra ocupada.
