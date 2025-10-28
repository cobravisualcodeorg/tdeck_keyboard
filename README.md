🧩 TDeckKeyboard — Librería para control de pantalla y teclado en LilyGO T-Deck

TDeckKeyboard es una librería desarrollada en MicroPython que facilita la integración y control del teclado I2C y la pantalla TFT ST7789 del dispositivo LilyGO T-Deck.
Permite mostrar texto, manejar entrada de usuario en tiempo real y crear interfaces interactivas directamente desde el microcontrolador.


⚙️ Características principales

.Inicialización completa de la pantalla TFT (SPI) y el teclado (I2C).

.Lectura de teclas mediante comunicación I2C con control de errores integrado.

.Entrada de texto interactiva, con visualización en pantalla tipo terminal.

.Funciones de dibujo de texto (draw_text, draw_input_line) con control de color, posición y fondo.

.Gestión del cursor y limpieza de área para mantener una visualización ordenada.

🛠️ Métodos principales


-init_display()	Inicializa y enciende la pantalla.

-draw_text(text, x, y, color, bg)	Muestra texto en la pantalla en una posición específica.

-draw_input_line(text)	Actualiza la línea de entrada del usuario.

-get_key()	Lee una tecla del teclado vía I2C. Devuelve None si no hay entrada.

-get_input(prompt="Ingresa texto:")	Solicita texto al usuario mostrando un prompt y lo retorna al presionar Enter.
