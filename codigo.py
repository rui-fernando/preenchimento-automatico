'''
primeiro passo: entrar no sistema da empresa https://dlp.hashtagtreinamentos.com/python/intensivao/login
segundo passo: fazer login
terceiro passo: importar a base de dados
quarto passo: cadastrar 1 produto
quinto passo: repetir para todos os produtos do bd
'''

import pyautogui #fazer automações
import time
import pandas as pd

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar na tela
# pyautogui.hotkey -> combinação de teclas

pyautogui.PAUSE = 0.7 #pequena pausa entre os cmds

#abrir o navegador Microsoft Edge
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

#entrar no link digitando o url
pyautogui.click(x=301, y=65)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3) #espera um tempo de 3 segundos 

#fazer login
pyautogui.click(x=823, y=449) #verifica e seleciona a posição do campo na tela

pyautogui.write("pythonimpressionador@gmail.com") #email do usuário
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("minha_senha@") #senha do usuário
pyautogui.click(x=959, y=651) # clique no login
time.sleep(3)

tabela = pd.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    
    pyautogui.click(x=699, y=317)

    #cadastrando um (01) produto por vez
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(10000)