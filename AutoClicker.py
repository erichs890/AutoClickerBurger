import pyautogui as py
from time import sleep
from pynput import mouse

screen_width, screen_height = py.size()
center_x = screen_width // 2
center_y = screen_height // 2
running_clicar = True
running_alimentar = True

def on_right_click(x, y, button, pressed):
    global running_clicar, running_alimentar
    if button == mouse.Button.right and pressed:
        print("Botão direito do mouse clicado, interrompendo o loop.")
        running_clicar = False
        running_alimentar = False
        return False

def clicarInfinitamente():
    py.hotkey('alt', 'tab')
    sleep(1)

    py.moveTo(center_x, center_y)
    global running_clicar
    running_clicar = True
    py.PAUSE = 0  
    intervalo = 0.0232  

    listener = mouse.Listener(on_click=on_right_click)
    listener.start()

    while running_clicar:
        py.click(center_x, center_y, interval=intervalo)
    
    listener.join()

def moverParaEsquerdaBaixo():
    py.moveTo(439, 550)

def alimentarGato():
    py.hotkey('alt', 'tab')
    sleep(1)

    py.moveTo(center_x, center_y)
    global running_alimentar
    running_alimentar = True
    py.PAUSE = 0  
    intervalo = 0.0232  

    listener = mouse.Listener(on_click=on_right_click)
    listener.start()

    while running_alimentar:
        moverParaEsquerdaBaixo()
        py.click(interval=intervalo)
    listener.join()