# Passo a passo do projeto

# 1 Abrir o sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login

#para instalar: Ctrl+J > Prompt command> pip install pyautogui (para fazer automações no teclado, mouse)

#biblioteca para automatação
import pyautogui

#biblioteca que tem o comando para pausar o código em determinados lugares do código
import time

#pausa entra cada comando
pyautogui.PAUSE = 0.5

#pyautogui.click   clicar com o mouse
#pyautogui.write   escrever um texto
#pyautogui.press   pressionar uma tecla
#pyautogui.hotkey  pressionar um conjunto de teclas (Ctrl+c, Ctrl+v)

#abrir o navegador (Chrome)
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

time.sleep(2)

#entrar no site do sistema
pyautogui.write("virtualif.iftm.edu.br")
pyautogui.press("enter")

#aqui pode ser que ele demore alguns segundos para carregar o site, por isso damos uma pausa maior
time.sleep(3)

# 2 Fazer login
pyautogui.click(x=665, y=511)
#pode personalizar a quantidade de cliques "clicks", se é com o botão direito ou esquerdo do mouse button="left/right" 
pyautogui.write("usuario")
pyautogui.press("tab") #passou para o campo de senha
pyautogui.write("senha")
pyautogui.press("tab") #passou para o botão de logar
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(4)

