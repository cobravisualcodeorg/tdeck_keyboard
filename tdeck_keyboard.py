import machine, time, st7789, font8x8 as font

class TDeckKeyboard:
    def __init__(self,
                 # Configuración de la pantalla:
                 spi_id=1,
                 baudrate=8000000,
                 sck_pin=40,
                 mosi_pin=41,
                 miso_pin=38,
                 dc_pin=11,
                 cs_pin=12,
                 bl_pin=42,
                 rotation=1,
                 # Configuración del teclado:
                 i2c_scl_pin=8,
                 i2c_sda_pin=18,
                 i2c_freq=400000,
                 i2c_timeout=50000,
                 keyboard_addr=0x55,
                 # Configuración de posiciones en pantalla:
                 y_input=50,
                 prompt_offset=20):
        # --- Inicialización de la pantalla ---
        self.spi = machine.SPI(spi_id,
                               baudrate=baudrate,
                               sck=machine.Pin(sck_pin),
                               mosi=machine.Pin(mosi_pin),
                               miso=machine.Pin(miso_pin))
        self.DC  = machine.Pin(dc_pin, machine.Pin.OUT)
        self.CS  = machine.Pin(cs_pin, machine.Pin.OUT)
        self.BL  = machine.Pin(bl_pin, machine.Pin.OUT)
        self.tft = st7789.ST7789(self.spi, 240, 320,
                                  dc=self.DC, cs=self.CS,
                                  backlight=self.BL,
                                  rotation=rotation)
        # --- Inicialización del teclado ---
        self.i2c = machine.SoftI2C(scl=machine.Pin(i2c_scl_pin),
                                   sda=machine.Pin(i2c_sda_pin),
                                   freq=i2c_freq,
                                   timeout=i2c_timeout)
        self.KEYBOARD_ADDR = keyboard_addr

        # --- Variables para entrada de texto ---
        self.input_text = ""
        self.Y_INPUT = y_input          # Línea donde se escribe el texto
        self.Y_PROMPT = y_input - prompt_offset  # Línea donde se muestra el prompt

    def init_display(self):
        """Inicializa y enciende la pantalla."""
        self.tft.init()
        self.tft.on()

    def draw_text(self, text, x, y, color=st7789.WHITE, bg=st7789.BLACK, width=240, height=16):
        """Dibuja un bloque de texto en la pantalla limpiando el área indicada."""
        self.tft.fill_rect(x, y, width, height, bg)
        self.tft.text(font, text, x, y, color, bg)

    def draw_input_line(self, text):
        """Dibuja la línea de entrada de texto."""
        self.draw_text(text, 0, self.Y_INPUT)

    def get_key(self):
        """Intenta leer una tecla vía I2C. Devuelve None si no se lee nada válido."""
        try:
            ch = self.i2c.readfrom(self.KEYBOARD_ADDR, 1)
            if ch is None or ch == b'\x00':
                return None
            return ch
        except Exception:
            return None

    def get_input(self, prompt="Ingresa texto:"):
        """
        Solicita al usuario una entrada de texto.
        Muestra el prompt en la pantalla y actualiza en tiempo real la línea de entrada.
        Retorna el texto ingresado al presionar Enter ('\r').
        """
        self.input_text = ""
        self.draw_text(prompt, 0, self.Y_PROMPT)
        self.draw_input_line(self.input_text)
        while True:
            key = self.get_key()
            if key:
                try:
                    ch = chr(key[0])
                except Exception:
                    ch = ''
                if ch == '\r':  # Enter finaliza la entrada
                    break
                elif ch == '\b':  # Backspace elimina el último carácter
                    self.input_text = self.input_text[:-1]
                else:
                    self.input_text += ch
                self.draw_input_line(self.input_text)
            time.sleep(0.1)
        return self.input_text
    
    """
Explicación
La librería (tdeck_keyboard.py):

Se crea una clase TDeckKeyboard que inicializa tanto la pantalla TFT como el teclado vía I2C.
Se incluyen métodos para dibujar texto en la pantalla (draw_text), actualizar la línea de entrada (draw_input_line) y leer teclas (get_key).
El método get_input se encarga de solicitar y capturar la entrada del usuario mostrando un prompt.
Uso en el programa principal:

Se importa la clase TDeckKeyboard y se instancia.
Se muestra un mensaje inicial y se espera a que el usuario presione Enter para comenzar.
Se solicita un comando al usuario y, mediante un diccionario de comandos, se ejecuta la función correspondiente, pasándole la instancia de TDeckKeyboard para que pueda actualizar la pantalla.
"""
#creado por kevin nazario ruiz para cobravisualcode.org 
