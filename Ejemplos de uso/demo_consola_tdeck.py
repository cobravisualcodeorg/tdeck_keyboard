import time
from tdeck_keyboard import TDeckKeyboard

tdeck = TDeckKeyboard()
tdeck.init_display()

tdeck.draw_text("Sistema iniciado", 0, 0)
time.sleep(1)

comando = tdeck.get_input("Comando: ")
tdeck.draw_text(f"Ejecutando: {comando}", 0, 70)
