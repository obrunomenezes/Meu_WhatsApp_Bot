#primeira coisa  é instalar a biblioteca keyboard pywhatkit

#importar as bibliotecas nescessárias 


import pywhatkit
from datetime import datetime
import time
import keyboard
import pyautogui

contatos = ['+552197000000'] #Aqui vc coloca os números dos contatos que irão receber a mensagem 

while len(contatos) >= 1:
    hora_atual = datetime.now().hour
    minuto_atual = datetime.now().minute + 1

    pywhatkit.sendwhatmsg(contatos[0], 'Teste de mensagem 2', hora_atual, minuto_atual, wait_time=30)  # Aumente o wait_time se necessário

    time.sleep(15)  # Aguarda 10 segundos após o envio da mensagem

    keyboard.press_and_release('enter')  # Simula a pressão da tecla Enter

    pyautogui.hotkey('ctrl', 'w')  # Simula o atalho de teclado para fechar a aba do navegador
    

    del contatos[0]

    if not contatos:  # Verifica se a lista de contatos está vazia
        break

print("Mensagens enviadas para todos os contatos. O programa será encerrado.")