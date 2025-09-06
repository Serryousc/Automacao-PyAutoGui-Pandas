import pyautogui
import pandas as pd 
from time import sleep 

arqui = pd.read_csv("AdNoturno.csv",sep=";", encoding='latin-1')  # Using pandas, read the .csv file/ Usando pandas para ler o arquivo CSV
matriculas = arqui.drop(columns=['NOME','QUANTIDADE']).T          # Remember to add a columns call 'VALOR' for cases that the Prodata System is not able to calculate the current benefit
                                                                  # Lembra de adicionar a coluna 'VALOR' para os casos que não é possivel para o sistema prodata calcular o valor do beneficio (ex:Horas extras)

for matricula in matriculas: #For each matricula in matriculas /Para cada matricula em matriculas
    matri1 = str(arqui.loc[matricula,'MATRICULA'])  #Transform matricula in a string /Pega a matricula e transforma em uma string
    quant1 = str(arqui.loc[matricula,'QUANTIDADE']) #Transform quantidade in a string /Pega a quantidade e transforma em uma string
    #valor1 = str(arqui.loc[matricula,'VALOR'])     #Transform valor in a string /Pega o valor e transforma em uma string

    def automacao(matricula,quantidade,): #sequencia of click to insert data to the prodata system/ Sequencia de clicks para inserir os dados no sistema prodata
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
