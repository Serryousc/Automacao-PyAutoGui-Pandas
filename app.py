import pyautogui
import pandas as pd 
from time import sleep 

arqui = pd.read_csv("AdNoturno.csv",sep=";", encoding='latin-1') # Horas Extras
matriculas = arqui.drop(columns=['NOME','QUANTIDADE']).T #Lembra de Add, 'VALOR' caso seja necessario 


for matricula in matriculas:
                                                    #para cada matricula em matriculas:
    matri1 = str(arqui.loc[matricula,'MATRICULA'])  #pega a matricula e transforma em uma string
    quant1 = str(arqui.loc[matricula,'QUANTIDADE']) #pega a quantidade e transforma em uma string
    #valor1 = str(arqui.loc[matricula,'VALOR'])      #pega o valor e transforma em uma string


    def automacao(matricula,quantidade,):
        pyautogui.doubleClick(1350,335, duration=1.5) #click for Matricula
        pyautogui.press('del')
        pyautogui.write(matricula)

        pyautogui.doubleClick(2252,334, duration=1.5) #click for Quantidade
        pyautogui.press('del')
        pyautogui.write(quantidade)

        #pyautogui.doubleClick(1949,402, duration=1.5) 
        #pyautogui.press('del')
        #pyautogui.write(valor)

        pyautogui.click(1363,607,duration=1.5) #click for Add
    automacao(matri1,quant1)





# click for Matricula: 1350,335
# click for Quantidade: 2252,334
# click for Valor: 1949,402
# click for Adicionar e Limpar: 1363,607
#
